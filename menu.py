from datetime import datetime, time

from BestBusCompany import BestBusCompany
from exceptions import *


def select_option(msg: str, num_options: int):
    while True:
        select = int(input(msg))
        if select < 1 or select > num_options:
            raise OutOfRangeError(select)
        return select

def manager_authentication(my_password):
    print("--------------- manager ---------------")
    i = 0
    while i < 3:
        password = input("please insert your password: ").strip()
        if password == my_password:
            print("log in")
            return True
        i += 1
        if i != 3:
            print("wrong password, try again - ")
    print("Wrong password, please approach your manager")
    return False

def manager_menu():
        print(" ----- manager menu -----:\n"
          "     1 - add route\n"
          "     2 - delete route\n"
          "     3 - update route\n"
          "     4 - add scheduled ride\n"
            "     5 - exit"
                   "")

def passenger_menu():
    print("------------ Passenger ------------\n"
            "please select the action you would like:\n"
            "     1 - search route\n"
            "     2 - report delay\n"
            "     3 - exit")


