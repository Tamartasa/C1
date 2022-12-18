from datetime import datetime
from random import randint, random
from ScheduledRide import ScheduledRide

class BusRoute:


    def __init__(self, line_number: int, origin_stop: str, destination_stop: str):
        self.__route_number = line_number
        # while not self.route_number:
        #     route_number = randint(1, 200)
        #     if route_number not in BusRoute.ROUTE_SET:
        #         BusRoute.ROUTE_SET.add(route_number)
        #         self.route_number = route_number
        self._origin_stop = origin_stop
        self._destination_stop = destination_stop
        self._list_of_ordered_stops = []
        self._scheduled_rides: dict[int: ScheduledRide] = {}
        #dict schedule id to ScheduleRide

    def __str__(self):
        return f"LINE {self.__route_number}\n from {self._origin_stop} to {self._destination_stop}\n stops: {self._list_of_ordered_stops}\n scheduled rides: {self._scheduled_rides}\n -------------------------------------"

    def __repr__(self):
        return self.__str__()

    def get_origin_stop(self):
        return self._origin_stop

    def get_destination_stop(self):
        return self._destination_stop

    def get_list_of_ordered_stop(self):
        return self._list_of_ordered_stops

    def get_scheduled_ride(self):
        return self._scheduled_rides

    def set_origin_stop(self, origin: str):
        self._origin_stop = origin

    def set_destination_stop(self, destination: str):
        self._destination_stop = destination

    def set_list_of_stops(self, list_of_stops: list):
        self._list_of_ordered_stops = list_of_stops

    def add_scheduled_ride(self, origin_time: datetime, destination_time: datetime, driver_name: str):
        new_ride = ScheduledRide(origin_time, destination_time, driver_name)
        self._scheduled_rides[new_ride._id] = new_ride
        print("schedule added")

    def report_ride_delay(self, schedule_id):
        if schedule_id not in self._scheduled_rides:
            print("wrong schedule ID")
            return False
        self._scheduled_rides[schedule_id].add_delay()
        print("delay had been reported")
        # add delay to counter of specific ScheduleRide

    def display_schedule(self):
        print(self._scheduled_rides)

    #  ------------------------------------------------------------------------------------------------

    # def display_route(self):
    #     print(f"-------------------------------\n"
    #           f"line number: {self.route_number}\n"
    #           f"from {self.origin_stop} to {self.destination_stop}\n"
    #           f"stops: {self.list_of_ordered_stops}\n"
    #           f"schedule: {self.scheduled_rides}\n"
    #           f"-------------------------------")

