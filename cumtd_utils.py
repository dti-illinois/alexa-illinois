import json

from cumtd_consts import device_dict, device_id_my_pc
from cumtd_api import CUMTD

mtd = CUMTD()

def get_stop_name(device_id):
    return device_dict[device_id]['name']

def get_routes_by_stop(device_id):
    stop_id = device_dict[device_id]['id']
    routes = mtd.get_routes_by_stop(stop_id)['routes']
    print(json.dumps(routes, indent=4))
    routes = _parse_routes(routes)
    return routes

def _parse_routes(routes):
    result = []
    for route in routes:
        result.append(route['route_id'])
    return result

get_routes_by_stop(device_id_my_pc)
