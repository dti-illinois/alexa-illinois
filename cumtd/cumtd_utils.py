import json
import datetime

from cumtd_consts import device_dict, device_id_my_pc
from data.cumtd_api import CUMTD

mtd = CUMTD()
with open('data/CUMTD_stops_id_key.json', 'r') as f:
    stops_id_key = json.load(f)['stops']

def get_stop_info(device_id):
    stop_info = device_dict[device_id]
    return stop_info['name'], stop_info['id']

def get_routes_on_service(stop_id):
    all_routes = _get_all_routes_by_stop(stop_id)
    calendar_today = _get_calendar_by_today()
    for route in all_routes.keys():
        trips = _get_trips_by_routes(route)
        for trip in trips:
            if trip in calendar_today:
                all_routes[route] = True
    result = []
    for k, v in all_routes.items():
        if v:
            result.append(k)
    return result

def _get_all_routes_by_stop(stop_id):
    routes = mtd.get_routes_by_stop(stop_id)['routes']
    routes = _parse_routes(routes)
    return routes

def _get_trips_by_routes(route_id):
    trips = mtd.get_trips_by_route(route_id)['trips']
    services = []
    for trip in trips:
        services.append(trip['service_id'])
    return list(set(services))

def _get_calendar_by_today():
    date = datetime.datetime.now().strftime('%Y%m%d')
    services_today = mtd.get_calendar_by_date(date)['calendar_dates']
    services = []
    for service_today in services_today:
        services.append(service_today['service_id'])
    return list(set(services))

def get_route_on_service_by_date(route_id, date):
    trips = _get_trips_by_routes(route_id)
    calendar = _get_calendar_by_date(date)
    for trip in trips:
        if trip in calendar.keys():
            return 'on service'
    return 'not on service'

def _get_calendar_by_date(date):
    date = date.replace('-','')
    calendar = mtd.get_calendar_by_date(date)['calendar_dates']
    result = {}
    for item in calendar:
        result[item['service_id']] = True
    return result

def get_remaining_time(stop_id, route_id):
    departures = mtd.get_departures_by_stop(stop_id=stop_id, route_id=route_id)['departures']
    result = []
    for departure in departures:
        result.append({
        'headsign': departure['headsign'],
        'time': departure['expected_mins']
        })
    return sorted(result, key=lambda x: x['time'])

def get_planned_trip(origin_stop_id, destination_stop_id):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    itineraries = mtd.get_planned_trips_by_stops(origin_stop_id=origin_stop_id,
        destination_stop_id=destination_stop_id)['itineraries']
    planned_trips = []
    for itinerary in itineraries:
        planned_trips.append(_parse_itinerary(itinerary))
    return planned_trips

def _parse_itinerary(itinerary):
    travel_time = itinerary['travel_time']
    result = {}
    w, s = [], []
    for leg in itinerary['legs']:
        type = leg['type']
        if type == 'Walk':
            walk = _parse_walk(leg['walk'])
            w.append(walk)
        elif type == 'Service':
            services = _parse_services(leg['services'])
            s.append(services)
    result['time'] = travel_time
    result['walk'] = w
    result['services'] = s
    return result

def _parse_walk(walk):
    result = {}
    result['directional'] = walk['direction']
    result['distance'] = walk['distance']
    result['start'] = walk['begin']['name']
    result['end'] = walk['end']['name']
    return result

def _parse_services(services):
    result = []
    for service in services:
        tmp = {}
        tmp['start'] = stops_id_key[service['begin']['stop_id']]
        tmp['end'] = stops_id_key[service['end']['stop_id']]
        tmp['route'] = service['route']['route_long_name']
        result.append(tmp)
    return result

def _parse_routes(routes):
    result = {}
    for route in routes:
        result[route['route_id']] = False
    return result

#print(json.dumps(get_remaining_time('PLAZA:4', 'yellow'), indent=4))
#get_planned_trip('PLAZA:4', 'UWALMART:2')
#print(get_routes_on_service_by_date('GOLD','2018-07-15'))
