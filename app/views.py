from functools import wraps
from app import app, db
from flask import jsonify, request, abort
from .models import Region, City, Users
import json


def create_region(name):
    region = Region(name)
    db.session.add(region)
    db.session.commit()

def create_city(name, region):
    city = City(name, region)
    db.session.add(city)
    db.session.commit()


def make_serializable_list_from_query(query_list):
    '''Return list that can be serialized to json'''
    elements_list = []
    for element in query_list:
        element_dic = {}
        element_dic['name'] = element.name
        element_dic['id'] = element.id
        elements_list.append(element_dic)
    return elements_list


def need_authentication(func):
    '''Decorator used when authentication is needed'''
    wraps(func)
    def decorated_func(*args, **kwargs):
        username = request.headers.get('username')
        password = request.headers.get('password')
        if not username or not password:
            abort(401)
        user = db.session.query(Users).filter_by(username=username).first()
        if not user:
            abort(401)
        if not user.check_password(password):
            abort(401)
        return func(*args, **kwargs)
    decorated_func.__name__ = func.__name__
    return decorated_func


@app.route('/api/regions')
def get_regions():
    '''Return all regions list'''
    regions_list = make_serializable_list_from_query(db.session.query(Region).all())
    return jsonify({'regions': regions_list})


@app.route('/api/cities/<int:region_id>')
def get_cities(region_id):
    '''Return paricular region' cities list'''
    cities_list = make_serializable_list_from_query(db.session.query(City).filter_by(region_id=region_id))
    return jsonify({'cities': cities_list})


@app.route('/api/add_region', methods=['POST'])    
@need_authentication
def add_region():
    '''Create region in database'''
    request_data = request.data.decode()
    if request_data == '':
        return jsonify({'error': 'Empty request'}), 400
    request_data_dic = json.loads(request.data)
    region_name = request_data_dic.get('name')
    if not region_name:
        return jsonify({'error': 'No region name given'}), 400
    if len(db.session.query(Region).filter_by(name=region_name).all()) != 0:
        return jsonify({'error': 'Region already exists'}), 400
    create_region(region_name)
    return jsonify({'status': 'success'}), 200


@app.route('/api/add_city', methods=['POST'])
@need_authentication
def add_city():
    '''Create city in given region in database'''
    request_data = request.data.decode()
    if request_data == '':
        return jsonify({'error': 'Empty request'}), 400
    request_data_dic = json.loads(request_data)
    region_id = request_data_dic.get('region_id')
    city_name = request_data_dic.get('city_name')
    if not region_id or not city_name:
        return jsonify({'error': 'No region id or city name given'}), 400
    if len(db.session.query(Region).filter_by(id=region_id).all()) == 0:
        return jsonify({'error': 'Wrong region id'}), 400
    if len(db.session.query(City).filter_by(region_id=region_id, name=city_name).all()) != 0:
        return jsonify({'error': 'City in that region already exists'}), 400
    create_city(city_name, region_id)    
    return jsonify({'status': 'success'}), 200


@app.route('/api/change_region', methods=['PUT'])
@need_authentication
def change_region():
    '''Updates region in database'''
    request_data = request.data.decode()
    if request_data == '':
        return jsonify({'error': 'Empty request'}), 400
    request_data_dic = json.loads(request_data)
    region_id = request_data_dic.get('region_id')
    region_name = request_data_dic.get('region_name')
    if not region_id or not region_name:
        return jsonify({'error': 'No region id or region name given'}), 400
    region = db.session.query(Region).filter_by(id=region_id).first()
    if not region:
        return jsonify({'error': 'Wrong region id'}), 400
    region.name = region_name
    db.session.commit()
    return jsonify({'status': 'success'}), 200
    

@app.route('/api/change_city', methods=['PUT'])
@need_authentication
def change_city():
    '''Updates geven city'''
    request_data = request.data.decode()
    if request_data == '':
        return jsonify({'error': 'Empty request'}), 400
    request_data_dic = json.loads(request_data)
    city_id = request_data_dic.get('city_id')
    if not city_id:
        return jsonify({'error': 'No city id given'}), 400
    city = db.session.query(City).filter_by(id=city_id).first()
    if not city:
        return jsonify({'error': 'Wrong city id'}), 400
    city.name = request_data_dic.get('city_name', city.name)
    region_id = request_data_dic.get('region_id')
    if region_id:
        region = db.session.query(Region).filter_by(id=region_id).first()
        if not region:
            return jsonify({'error': 'Wrong region id'}), 400
        city.region_id = region_id
    db.session.commit()
    return jsonify({'status': 'success'}), 200


@app.route('/api/delete_region', methods=['DELETE'])
@need_authentication
def delete_region():
    '''Delete region from database'''
    request_data = request.data.decode()
    if request_data == '':
        return jsonify({'error': 'Empty request'}), 400
    request_data_dic = json.loads(request_data)
    region_id = request_data_dic.get('region_id')
    if not region_id:
        return jsonify({'error': 'No region id given'}), 400
    region = db.session.query(Region).filter_by(id=region_id).first()
    if not region:
        return jsonify({'error': 'Wrong region id'}), 400
    db.session.delete(region)
    db.session.commit()
    return jsonify({'status': 'success'}), 200


@app.route('/api/delete_city', methods=['DELETE'])
@need_authentication
def delete_city():
    '''Delete city from database'''
    request_data = request.data.decode()
    if request_data == '':
        return jsonify({'error': 'Empty request'}), 400
    request_data_dic = json.loads(request_data)
    city_id = request_data_dic.get('city_id')
    if not city_id:
        return jsonify({'error': 'No city id given'}), 400
    city = db.session.query(City).filter_by(id=city_id).first()
    if not city:
        return jsonify({'error': 'Wrong city id'}), 400
    db.session.delete(city)
    db.session.commit()
    return jsonify({'status': 'success'}), 200