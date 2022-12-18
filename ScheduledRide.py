from datetime import datetime


class ScheduledRide:
    ID = 100

    def __init__(self, origin_time: datetime, destination_time: datetime, driver_name: str):
        self._id = ScheduledRide.ID
        ScheduledRide.ID += 1
        self._origin_time = origin_time
        self._destination_time = destination_time
        self.__driver_name = driver_name
        self._delays: dict[datetime: int] = {}
        #day and count of delays reports

    def __str__(self):
        return f"scheduled ID.{self._id}\n" \
               f"origin_time: {self._origin_time}, destination_time: {self._destination_time}\n" \
               f"delays: {self._delays}"

    def __repr__(self):
        # return f"ID {self.ID}, origin time: {datetime.strftime(self.origin_time, '%H:%S')}, destination time: {datetime.strftime(self.destination_time,  '%H:%S')}, delays: {self.delays}"
        return self.__str__()

    def add_delay(self):
        delay_date = datetime.today().date().strftime("%d/%m/%y")
        if delay_date not in self._delays:
            self._delays[delay_date] = 0
        self._delays[delay_date] += 1


