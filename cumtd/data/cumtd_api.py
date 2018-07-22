import requests

BASE_URL = 'https://developer.cumtd.com/api/'
API_VERSION = 'v2.2'
KEY = '5dffc40cd2534eb58fa3e984699befe1'

class CUMTD:

    def __init__(self):
        self.key = KEY
        self.base_url = BASE_URL
        self.api_version = API_VERSION
        self.format = 'json'
        self.url = self.base_url + self.api_version + '/' + self.format + '/'

    def get_calendar_by_date(self, date):
        return self._make_request('GetCalendarDatesByDate', locals())

    def get_calendar_by_service(self, service_id):
        return self._make_request('GetCalendarDatesByService', locals())

    def get_departures_by_stop(self, stop_id, route_id=None, pt=30, count=None):
        return self._make_request('GetDeparturesByStop', locals())

    def get_route(self, route_id):
        if type(route_id) is list:
            route_id = ''.join(route_id, ';')
        return self._make_request('GetRoute', locals())

    def get_routes(self):
        return self._make_request('GetRoutes', locals())

    def get_routes_by_stop(self, stop_id):
        return self._make_request('GetRoutesByStop', locals())

    def get_stop(self, stop_id):
        if type(stop_id) is list:
            stop_id = ''.join(stop_id, ';')
        return self._make_request('GetStop', locals())

    def get_stops(self):
        return self._make_request('GetStops', locals())

    def get_stops_by_search(self, query, count=None):
        return self._make_request('GetStopsBySearch', locals())

    def get_trips_by_route(self, route_id):
        return self._make_request('GetTripsByRoute', locals())

    def get_planned_trips_by_stops(self, origin_stop_id, destination_stop_id):
        return self._make_request('GetPlannedTripsByStops', locals())

    def _make_request(self, func, args):
        params = { 'key': self.key }
        for k, v in args.items():
            if v is not None and k != 'self':
                params[k] = v
        url = self.url + func.lower()
        r = requests.get(url, params=params)
        return r.json()
