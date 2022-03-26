# Geos
Демо версия HTTP-сервера для предоставления информации по географическим объектам. Данные берутся из географической базы данных [GeoNames](http://download.geonames.org/export/dump/RU.zip).
## Реализованные методы
- Поиск информации о городе по идентификатору **geonameid**
- Вывод списка городов с заданной страницы
- Вывод информации о двух конкретных городах
- Вывод подсказки названия города по части его имени
## Поиск информации о городе по идентификатору geonameid
Метод принимает идентификатор geonameid и возвращает информацию о городе
#### Запрос вида
`GET /geo_data/api_v1/city/<int:geonameid>`
#### Пример запроса
`GET /geo_data/api_v1/city/7609871`
#### Ответ
```json
{
  "7609871": {
    "admin1 code": "52", 
    "admin2 code": "", 
    "admin3 code": "", 
    "admin4 code": "", 
    "alternatenames": "Krutec,Krutets,\u041a\u0440\u0443\u0442\u0435\u0446", 
    "asciiname": "Krutets", 
    "cc2": "", 
    "country code": "RU", 
    "dem": "39", 
    "elevation": "", 
    "feature class": "P", 
    "feature code": "PPLQ", 
    "geonameid": 7609871, 
    "latitude": "57.9537", 
    "longitude ": "31.8887", 
    "modification date": "2012-01-21", 
    "name": "Krutets", 
    "population": 0, 
    "timezone": "Europe/Moscow"
  }
}
```
## Вывод списка городов с заданной страницы
Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией.

**Параметры** :
- `page` - номер страницы
- `count` - количество городов на странице
#### Запрос вида
`GET /geo_data/api_v1/city/`
#### Пример запроса
`GET /geo_data/api_v1/city/?page=109&count=3`
#### Ответ
```json
{
  "Page: 109": [
    {
      "admin1 code": "77", 
      "admin2 code": "", 
      "admin3 code": "", 
      "admin4 code": "", 
      "alternatenames": "Churikovo,\u0427\u0443\u0440\u0438\u043a\u043e\u0432\u043e", 
      "asciiname": "Churikovo", 
      "cc2": "", 
      "country code": "RU", 
      "dem": "169", 
      "elevation": "", 
      "feature class": "P", 
      "feature code": "PPL", 
      "geonameid": 452072, 
      "latitude": "57.0922", 
      "longitude ": "34.90569", 
      "modification date": "2012-01-16", 
      "name": "Churikovo", 
      "population": 0, 
      "timezone": "Europe/Moscow"
    }, 
    {
      "admin1 code": "77", 
      "admin2 code": "", 
      "admin3 code": "", 
      "admin4 code": "", 
      "alternatenames": "Churikovo,\u0427\u0443\u0440\u0438\u043a\u043e\u0432\u043e", 
      "asciiname": "Churikovo", 
      "cc2": "", 
      "country code": "RU", 
      "dem": "207", 
      "elevation": "", 
      "feature class": "P", 
      "feature code": "PPL", 
      "geonameid": 452073, 
      "latitude": "56.91273", 
      "longitude ": "34.93842", 
      "modification date": "2012-01-16", 
      "name": "Churikovo", 
      "population": 0, 
      "timezone": "Europe/Moscow"
    }, 
    {
      "admin1 code": "77", 
      "admin2 code": "", 
      "admin3 code": "", 
      "admin4 code": "", 
      "alternatenames": "Chuprovo,\u0427\u0443\u043f\u0440\u043e\u0432\u043e", 
      "asciiname": "Chuprovo", 
      "cc2": "", 
      "country code": "RU", 
      "dem": "174", 
      "elevation": "", 
      "feature class": "P", 
      "feature code": "PPL", 
      "geonameid": 452074, 
      "latitude": "57.16758", 
      "longitude ": "34.60455", 
      "modification date": "2012-01-16", 
      "name": "Chuprovo", 
      "population": 0, 
      "timezone": "Europe/Moscow"
    }
  ]
}
```
## Вывод информации о двух конкретных городах
Метод принимает названия двух городов (на русском языке) и возвращает :
- информация о найденных городах 
- какой из них расположен севернее
- одинаковая ли у них временная зона (когда несколько городов имеют одно и то же название, берётся город с большим населением; если население совпадает, выбирается первый из их)
#### Запрос вида
`GET /geo_data/api_v1/city/<city_one>&<city_two>`
#### Пример запроса
`GET /geo_data/api_v1/city/Отделение Совхоза Тселинный Номер Три&Урочище Иссиргужи`
#### Ответ
```json
{
  "Otdeleniye Sovkhoza Tselinnyy Nomer Tri and Urochishche Issirguzhi": [
    {
      "admin1 code": "55", 
      "admin2 code": "", 
      "admin3 code": "", 
      "admin4 code": "", 
      "alternatenames": "Otdelenie Sovkhoza Celinnyj Nomer Tri,Otdeleniye Nomer Tri Sovkhoza Tselinnyy,Otdeleniye Sovkhoza Tselinnyy Nomer Tri,\u041e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0421\u043e\u0432\u0445\u043e\u0437\u0430 \u0426\u0435\u043b\u0438\u043d\u043d\u044b\u0439 \u041d\u043e\u043c\u0435\u0440 \u0422\u0440\u0438", 
      "asciiname": "Otdeleniye Sovkhoza Tselinnyy Nomer Tri", 
      "cc2": "", 
      "country code": "RU", 
      "dem": "268", 
      "elevation": "", 
      "feature class": "S", 
      "feature code": "FRM", 
      "geonameid": 453654, 
      "latitude": "51.2174", 
      "longitude ": "59.7682", 
      "modification date": "2012-02-01", 
      "name": "Otdeleniye Sovkhoza Tselinnyy Nomer Tri", 
      "population": 0, 
      "timezone": "Asia/Yekaterinburg"
    }, 
    {
      "admin1 code": "55", 
      "admin2 code": "", 
      "admin3 code": "", 
      "admin4 code": "", 
      "alternatenames": "Urochishche Issirguzhi,Urochishhe Issirguzhi,\u0423\u0440\u043e\u0447\u0438\u0449\u0435 \u0418\u0441\u0441\u0438\u0440\u0433\u0443\u0436\u0438", 
      "asciiname": "Urochishche Issirguzhi", 
      "cc2": "", 
      "country code": "RU", 
      "dem": "239", 
      "elevation": "", 
      "feature class": "L", 
      "feature code": "AREA", 
      "geonameid": 453641, 
      "latitude": "51.273", 
      "longitude ": "59.1997", 
      "modification date": "2012-01-16", 
      "name": "Urochishche Issirguzhi", 
      "population": 0, 
      "timezone": "Asia/Yekaterinburg"
    }
  ], 
  "Time difference": 0, 
  "Timezone": "identical", 
  "To the north is ": "Urochishche Issirguzhi"
}
```
## Вывод подсказки названия города по части его имени
Метод принимает часть названия города (на русском языке) и возвращает подсказку с возможными вариантами продолжений.
#### Запрос вида
`GET /geo_data/api_v1/city/<city_one>`
#### Пример запроса
`GET /geo_data/api_v1/city/Курса`
#### Ответ
```json
{
  "Possible variants of the name": [
    "Kursa-Yuryakh", 
    "Kursak", 
    "Kursay", 
    "Kursanovka", 
    "Kursakovskiye Vershiny", 
    "Kursakovo-Markovo", 
    "Kursamagitlar", 
    "Kursavka"
  ]
}
```