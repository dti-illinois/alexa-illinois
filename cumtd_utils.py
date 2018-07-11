import json
import datetime

from cumtd_consts import device_dict, device_id_my_pc
from cumtd_api import CUMTD

mtd = CUMTD()

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
    for itinerary in itineraries:

def _parse_itinerary(itinerary):
    travel_time = itinerary['travel_time']
    for leg in legs:
        type = leg['type']
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

def _parse_routes(routes):
    result = {}
    for route in routes:
        result[route['route_id']] = False
    return result

get_planned_trip('PLAZA:4', 'UWALMART:2')
