from flask import Flask, jsonify, request,make_response
from service import InfoCity

app = Flask(__name__)
obj = InfoCity()

@app.errorhandler(404)
def not_found(error):
# Ответ при ошибке 404
    return make_response(jsonify({'Error': 'Not found'}), 404)

@app.route('/geo_data/api_v1/city/<int:geonameid>', methods = ['GET'])
def get_city(geonameid):
# Поиск по geonameid
    city = obj.city_geonameid(geonameid)

    if not city:
        return jsonify({f'Error': 'Not found'})
    else:
        return jsonify({f'{geonameid}': city})

@app.route('/geo_data/api_v1/city/', methods = ['GET'])
def get_list_cities():
# Поиск по странице и количеству городов
    try:
        page = int(request.args.get('page'))
        count = int(request.args.get('count'))
        page_with_city = obj.city_page_and_count(page,count)

        if not page_with_city:
            return jsonify({f'Error': 'Not found'})
        else:
            return jsonify({f'Page: {page}': page_with_city})
    except:
        return jsonify({f'Error': 'Not found'})

@app.route('/geo_data/api_v1/city/<city_one>&<city_two>', methods = ['GET'])
def two_city(city_one,city_two):
# Поиск двух городов, сравнение временых зон и разницы во времени
    city_list = obj.two_city(city_one,city_two)

    if not city_list[0] and not city_list[1]:
        return jsonify({'Error': 'Localities are missing in the database'})

    elif not city_list[0]:
        return jsonify({'Error': 'First city not found'})

    elif not city_list[1]:
        return jsonify({'Error': 'Second city not found'})

    else:
        city_north = obj.city_north(city_list)
        return jsonify({f'{city_list[0]["asciiname"]} and {city_list[1]["asciiname"]}': city_list,'To the north is ':city_north[0],'Timezone':city_north[1][0],'Time difference':city_north[1][1]})

@app.route('/geo_data/api_v1/city/<city_one>', methods = ['GET'])
def part_of_name(city_one):
# Поиск возможных названий городов по началу его имени на русском
    possible_names = obj.list_name_cities(city_one)

    if not possible_names:
        return jsonify({'Error': 'Not found'})

    else:
        return jsonify({'Possible variants of the name': possible_names})