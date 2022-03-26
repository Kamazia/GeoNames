from os.path import dirname,abspath
from pytz import timezone,utc
from datetime import datetime

class InfoCity:
    def __init__(self):
        self.path = f'{dirname(abspath(__file__))}\\data\\Ru.txt'
        self.slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh',
      'ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'','ы':'y','ь':'\'','э':'e',
      'ю':'u','я':'ya',' ': ' ','-':'-'}

    def selection_attribute(self,line) -> dict:
        '''### Метод выделения атрибутов города из строки
        Принимает строку ``line`` - информацию о городе.\n
        Возвращает словарь состоящий из поэлементно разбитой строки.
        '''

        city = line.split('\t')

        city_attribute = {
            'geonameid': int(city[0]),
            'name': city[1],
            'asciiname': city[2],
            'alternatenames': city[3],
            'latitude': city[4],
            'longitude ': city[5],
            'feature class': city[6],
            'feature code': city[7],
            'country code': city[8],
            'cc2': city[9],
            'admin1 code': city[10],
            'admin2 code': city[11],
            'admin3 code': city[12],
            'admin4 code': city[13],
            'population': int(city[14]),
            'elevation': city[15],
            'dem': city[16],
            'timezone': city[17],
            'modification date': city[18].split('\n')[0]
        }
        
        return city_attribute

    def translite(self,old_name) -> str|None:
        '''### Метод перевода кирилицы в транслит
        Принимает строку ``old_name`` - название населенного пункта на русском.\n
        Возвращает строку - преобразованное в транслит название.\n
        ``е, ё`` - заменяется на ``ye`` в начале слова, после гласных и знаков ъ и ь; в остальных случаях - ``e``
        '''
        old_name = old_name.split()
        new_name = []
        try:
            for word in old_name:
                count = 0
                for letter in word:

                    if (count == 0 and letter == 'е'):
                        word = word.replace('е','ye',1)
                        count = count + 2
                
                    elif (letter == 'е' and (word[count-1] == 'e' or word[count-1] == 'u' or word[count-1] == 'a' or word[count-1] == 'i' or word[count-1] == 'o' or word[count-1] == 'y' or word[count-1] == '\'')):
                        word = word.replace('е','ye',1)
                        count = count + 2

                    else:
                        new_latter = self.slovar[letter]
                        word = word.replace(letter,new_latter,1)
                        count = count + len(new_latter)

                new_name.append(word)
            new_name =' '.join(new_name)
        except KeyError:
            return None
        
        return new_name

    def city_north(self,cities):
        '''### Метод определящий какой город севернее
        Принимает список из двух словарей с инфо о городах.\n
        Возвращает кортеж с названием более северного города и их разницу во времени.
        '''
        if cities[0] and cities[1]:

            if cities[0]['latitude'] > cities[1]['latitude']:
                    return cities[0]['asciiname'],self.timezone(cities)

            else:
                return cities[1]['asciiname'],self.timezone(cities)

    def timezone(self,cities):
        '''### Метод определения идентичности часовых поясов и определения разницы между ними
        Принимает список из двух словарей с инфо о городах.\n
        Возвращает кортеж со строкой ``'different/'identical'`` и int разницей во времени 
        '''
        if cities[0]['timezone'] == cities[1]['timezone']:
            return 'identical', 0
        else:
            now_utc = utc.localize(datetime.utcnow())
            now_first_city= now_utc.astimezone(timezone(cities[0]['timezone'])).replace(tzinfo=None)
            now_second_city = now_utc.astimezone(timezone(cities[1]['timezone'])).replace(tzinfo=None)

            if now_first_city > now_second_city:
                difference = now_first_city - now_second_city
            else:
                difference = now_second_city - now_first_city
                
            return 'different', int(difference.total_seconds()/3600) 

    def get_cities(self) -> list:
        '''### Метод считывания всех городов из файла
        Считывает файл по пути ``self.path``\n
        Возвращает список, содержащий словари с информацией о городах.
        '''
        cities = []

        with open (self.path,'r',encoding = 'utf-8') as file:
            for i in file:
                cities.append(self.selection_attribute(i))

        return cities

    def city_geonameid(self,geonameid):
        '''### Метод получения города по значению geonameid
        Принимает ``int geonameid``.\n
        Возвращает словарь с информацией о городе.
        '''
        with open (self.path,'r',encoding = 'utf-8') as file:
            for i in file:
                if i.split('\t')[0] == str(geonameid):
                    return self.selection_attribute(i)

    def city_page_and_count(self,page,count):
        ''' ### Метод получения страницы с заданным количеством городов
        Принимает ``int page`` - номер страницы, ``int count`` - количество отображаемых городов на странице\n
        Возвращает список городов с заданной страницы.\n
        Если выбрана последняя страница и количество городов на ней меньше запрашиваемого количества,
        то будет возращено оставшееся количество городов на странице.
        '''
        all_cities = self.get_cities()
        cities_on_page = []

        if page == 1:
            start = 0
            end = start + count
            for line in range(start,end):
                cities_on_page.append(all_cities[line])

            return cities_on_page

        elif page > 1:
            if ((page - 1) * count) > len(all_cities):
                return None

            start = (page - 1) * count
            if start + count > len(all_cities):
                end = len(all_cities)
            else:
                end = start + count

            for line in range(start,end):
                cities_on_page.append(all_cities[line])

            return cities_on_page

    def two_city(self,city_one,city_two) -> list:
        '''### Метод получения информации о двух конкретных городах
        Принимает две строки - название первого города и второго города.\n
        Возвращает список состоящий из двух словарей, в каждом из которых информация о городе если такие найдены.\n
        Если найдено более одного города с одинаковым названием, выбирается тот у которого больше население.
        '''
        all_cities = self.get_cities()
        cities = (self.translite(city_one.lower()),self.translite(city_two.lower()))
        city_one_out = []
        
        for i in cities:
            buffer = []
            for city in all_cities:
                if city['asciiname'].lower() == i:
                    if not buffer:
                        buffer = city
                    elif buffer ['population'] < city['population']:
                        buffer = city

            city_one_out.append(buffer)

        return city_one_out

    def list_name_cities(self,city_one):
        '''### Метод поиска названия города по начальной части его названия
        Принимает строку - часть названия города на русском.\n
        Возвращает список городов подходящих по полученной начальной части названия
        '''
        name_city = self.translite(city_one.lower())
        all_cities = self.get_cities()

        name_cities = []

        if name_city:
            for name in all_cities:
                if name ['asciiname'].lower().find(name_city,0,len(name_city)) != -1:
                    name_cities.append(name['asciiname'])

            return list(set(name_cities))

        else: 
            return None