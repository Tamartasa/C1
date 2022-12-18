from datetime import datetime

from BusRoute import BusRoute
from ScheduledRide import ScheduledRide
from exceptions import RouteNotInCompanyError


class BestBusCompany:

    def __init__(self):
        self._line2routes: dict[int: BusRoute] = {}
        #dictionary with origin stop to list of dict num to route as BusRoute, can be more than one line
        self._origin2route: dict[str: list[{int: BusRoute}]] = {}
        # dictionary with destination to list of dict num to route as BusRoute, can be more than one line
        self._destination2route: dict[str: list[{int: BusRoute}]] = {}
        # dictionary with name of stop to list of dict num to route as BusRoute, can be more than one line
        self._stop2route: dict[str: list[{int: BusRoute}]] = {}

    def get_routes(self):
        return self._stop2route

    def add_route(self, line_number: int, origin: str, destination: str, list_of_stops: list):
        if line_number in self._line2routes:
            print("there's already line with this number")
            return False
        #if we entered here, we have already checked there's no line number with the same number and
        #inputs are correct

        new_route = BusRoute(line_number, origin, destination)
        new_route.list_of_ordered_stops = list_of_stops
        self._line2routes[line_number] = new_route
        if origin not in self._origin2route:
            self._origin2route[origin] = []
        self._origin2route[origin].append({line_number: new_route})
        if destination not in self._destination2route:
            self._destination2route[destination] = []
        self._destination2route[destination].append({line_number: new_route})
        for stop in list_of_stops:
            if stop not in self._stop2route:
                self._stop2route[stop] = []
            self._stop2route[stop].append({line_number: new_route})
        print(f"line number {line_number} added")
        return True

    def display_route_from_routes(self, line_number):
        if line_number in self._line2routes:
            print(self._line2routes[line_number])

# ---------update --------------------
    def update_route_origin(self, line_number, new_origin):
        if line_number not in self._line2routes:
            print("no line with this number")
            return False
        self._line2routes[line_number].set_origin_stop(new_origin)
        print("route updated")

    def update_route_destination(self, line_number, new_destination):
        if line_number not in self._line2routes:
            print("no line with this number")
            return False
        self._line2routes[line_number].set_destination_stop(new_destination)
        print("route updated")

    def update_route_stops_list(self, line_number, new_stops_list):
        if line_number not in self._line2routes:
            return False
        self._line2routes[line_number].set_list_of_stops(new_stops_list)
        print("route updated")

    #  ---search ----------------------------------------------------------------------
    def search_route_by_line(self, line_number):
        if line_number not in self._line2routes:
            print("no line with this number")
            return False
        print(self._line2routes[line_number])

    def search_route_by_origin(self, origin):
        if origin not in self._origin2route:
            print("no route with this origin stop")
            return False
        print(f"routes from {origin}: {self._origin2route[origin]}")

    def search_route_by_destination(self, destination):
        if destination not in self._destination2route:
            print("no route with this destination stop")
            return False
        print(f"routes arrived to {destination}: {self._destination2route[destination]}")

    def search_route_by_stop(self, stop):
        if stop not in self._stop2route:
            print("no route with this stop")
            return False
        print(f"routes pass in {stop}: {self._stop2route[stop]}")

    # ---- delete -------------------------------------------------------------------------
    def delete_route(self, line_number):
        if line_number not in self._line2routes:
            # ther's no line with this number:
            print("there's no route with this number, hadn't been deleted")
            return False
        self._line2routes.pop(line_number)
        # delete from origin dict:
        for origin, dict in self._origin2route.items():
            if line_number in dict:
                self._origin2route[origin].remove(dict)
        # delete from destination dict:
        for destination, dict in self._destination2route.items():
            if line_number in dict:
                self._destination2route[destination].remove(dict)
        # delete from stop dict:
        for stop, dict in self._stop2route.items():
            if line_number in dict:
                self._stop2route[stop].remove(dict)
        print(f"line number {line_number} has been deleted")
        return True

# ------ scheduled rides-----------------------------------------------------------------------
    def display_route_scheduled(self, line_number):
        if line_number not in self._line2routes:
            return False
        print(self._line2routes[line_number]._scheduled_rides)
        return True

    def add_scheduled_ride_for_route(self, line_number, origin_time: datetime, destination_time: datetime, driver_name: str):
        if line_number not in self._line2routes:
            print("no route with this line number")
            return False
        self._line2routes[line_number].add_scheduled_ride(origin_time, destination_time, driver_name)
        return True

# ----- delays ------------------------------------------------------------------------------

    def report_delay(self, line_number, schedule_id):
        # line number from the route the user search - the system already found the line (it's exist)
        self._line2routes[line_number].report_ride_delay(schedule_id)

# -----------------------------------------------------------------------------------
#     def valid_line(self, line_number):
#         if line_number not in self._line2routes:
#             raise RouteNotInCompanyError(line_number)





