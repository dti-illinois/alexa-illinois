import json
import datetime

from cumtd_consts import CUMTDConsts
from data.cumtd_api import CUMTDAPI

class CUMTDSkill():

    def __init__(self):
        self.mtd = CUMTDAPI()
        with open('data/CUMTD_stops_id_key.json', 'r') as f:
            self.stops_id_key = json.load(f)['stops']

    def get_stop_info(self, device_id):
        stop_info = CUMTDConsts.device_dict[device_id]
        return stop_info['name'], stop_info['id']

    def get_routes_on_service(self, stop_id):
        all_routes = self._get_all_routes_by_stop(stop_id)
        calendar_today = self._get_calendar_by_today()
        for route in all_routes.keys():
            trips = self._get_trips_by_routes(route)
            for trip in trips:
                if trip in calendar_today:  all_routes[route] = True
        result = []
        for k, v in all_routes.items():
            if v:   result.append(k)
        return result

    def _get_all_routes_by_stop(self, stop_id):
        routes = self.mtd.get_routes_by_stop(stop_id)['routes']
        return self._parse_routes(routes)

    def _get_trips_by_routes(self, route_id):
        trips = self.mtd.get_trips_by_route(route_id)['trips']
        services = []
        for trip in trips:
            services.append(trip['service_id'])
        return list(set(services))

    def _get_calendar_by_today(self):
        date = datetime.datetime.now().strftime('%Y%m%d')
        services_today = self.mtd.get_calendar_by_date(date)['calendar_dates']
        services = []
        for service_today in services_today:
            services.append(service_today['service_id'])
        return list(set(services))

    def _parse_routes(self, routes):
        result = {}
        for route in routes:
            result[route['route_id']] = False
        return result

    def get_route_on_service_by_date(self, route_id, date):
        trips = self._get_trips_by_routes(route_id)
        calendar = self._get_calendar_by_date(date)
        for trip in trips:
            if trip in calendar.keys(): return 'on service'
        return 'not on service'

    def _get_calendar_by_date(self, date):
        date = date.replace('-','')
        calendar = self.mtd.get_calendar_by_date(date)['calendar_dates']
        result = {}
        for item in calendar:
            result[item['service_id']] = True
        return result

    def get_remaining_time(self, stop_id, route_id):
        departures = self.mtd.get_departures_by_stop(stop_id=stop_id, route_id=route_id)['departures']
        result = []
        for departure in departures:
            result.append({
            'headsign': departure['headsign'],
            'time': departure['expected_mins']
            })
        return sorted(result, key=lambda x: x['time'])

    def get_planned_trip(self, origin_stop_id, destination_stop_id):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        itineraries = self.mtd.get_planned_trips_by_stops(origin_stop_id=origin_stop_id,
            destination_stop_id=destination_stop_id)['itineraries']
        planned_trips = []
        for itinerary in itineraries:
            planned_trips.append(self._parse_itinerary(itinerary))
        return planned_trips

    def _parse_itinerary(self, itinerary):
        travel_time = itinerary['travel_time']
        result = {}
        w, s = [], []
        for leg in itinerary['legs']:
            type = leg['type']
            if type == 'Walk':
                walk = self._parse_walk(leg['walk'])
                w.append(walk)
            elif type == 'Service':
                services = self._parse_services(leg['services'])
                s.append(services)
        result['time'] = travel_time
        result['walk'] = w
        result['services'] = s
        return result

    def _parse_walk(self, walk):
        result = {}
        result['directional'] = walk['direction']
        result['distance'] = walk['distance']
        result['start'] = walk['begin']['name']
        result['end'] = walk['end']['name']
        return result

    def _parse_services(self, services):
        result = []
        for service in services:
            tmp = {}
            tmp['start'] = self.stops_id_key[service['begin']['stop_id']]
            tmp['end'] = self.stops_id_key[service['end']['stop_id']]
            tmp['route'] = service['route']['route_long_name']
            result.append(tmp)
        return result
