import json
from cumtd_api import CUMTD

mtd = CUMTD()
stops = mtd.get_stops()['stops']
routes = mtd.get_routes()['routes']

def write_routes_to_file():
    result = {}
    for route in routes:
        result[route['route_id']] = ''
    with open('CUMTD_route_name2short.json', 'w') as f:
        json.dump({'routes': result}, f, indent=4)

def write_routes_to_slot():
    result = []
    for route in routes:
        result.append({'name': {'value': route['route_id']}})
    with open('CUMTD_routes_slot.json', 'w') as f:
        json.dump({'values': result}, f, indent=4)

def write_stops_to_file1():
    result = []
    for stop in stops:
        stop_points = stop['stop_points']
        for stop_point in stop_points:
            id = stop_point['stop_id']
            name = stop_point['stop_name']
            name = _reformat_name(name)
            result.append({
            'id': id,
            'name': name
            })
    with open('CUMTD_stops_no_key.json', 'w') as f:
        json.dump({'stops': result}, f, indent=4)

def write_stops_to_file2():
    result = {}
    for stop in stops:
        stop_points = stop['stop_points']
        for stop_point in stop_points:
            id = stop_point['stop_id']
            name = stop_point['stop_name']
            name = _reformat_name(name)
            result[id] = name
    with open('CUMTD_stops_id_key.json', 'w') as f:
        json.dump({'stops': result}, f, indent=4)

def write_stops_to_file3():
    result = {}
    for stop in stops:
        stop_points = stop['stop_points']
        for stop_point in stop_points:
            id = stop_point['stop_id']
            name = stop_point['stop_name']
            name = _reformat_name(name)
            result[name] = id
    with open('CUMTD_stops_name_key.json', 'w') as f:
        json.dump({'stops': result}, f, indent=4)

def write_stops_to_slots():
    result = []
    for stop in stops:
        stop_points = stop['stop_points']
        for stop_point in stop_points:
            name = stop_point['stop_name']
            name = _reformat_name(name)
            result.append({'name': {'value': name}})
    with open('CUMTD_stops_slot.json', 'w') as f:
        json.dump({'values': result}, f, indent=4)

def _reformat_name(name):
    r = name.replace('(', '').replace(')', '')
    return r
