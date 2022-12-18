from unittest import TestCase


class BestBusCompanyException(Exception):
    pass

class RouteNotInCompanyError(BestBusCompanyException):
    def __init__(self, line_num):
        super().__init__(f"no route with this line number: {line_num}")

class OutOfRangeError(BestBusCompanyException):
    def __init__(self, num):
        super().__init__(f"{num} is out of range")

class StringError(BestBusCompanyException):
    def __init__(self):
        super().__init__("must be a string")

class InsertError(BestBusCompanyException):
    def __init__(self):
        super().__init__("must be letters")

class InsertNotNumber(BestBusCompanyException):
    def __init__(self):
        super().__init__("must be number")

class LineAlredyExist(BestBusCompanyException):
    def __init__(self):
        super().__init__("line already exist in system")

