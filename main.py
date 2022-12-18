import os
import pickle
from datetime import datetime, time

from BestBusCompany import BestBusCompany
from exceptions import *
from menu import *


#  ------insert functions------------------------------------------------------------------------
def insert_origion_or_destination(msg):
    while True:
        orig_or_dest_input = input(msg).strip()
        orig_or_dest = "".join(orig_or_dest_input.split(" "))
        # if there is space in input
        if orig_or_dest.isalpha():
            return orig_or_dest
        raise StringError()


def insert_stops():
    list_of_stops = []
    stops = input("insert the stops with comma between ech other: ").strip()
    for stop in stops.split(", "):
        if stop.isalpha or stop in " ":
            list_of_stops.append(stop)
            continue
        raise InsertError()
    return list_of_stops


def want_to_search():
    while True:
        try:
            print("By what would you like to search a route? \n"
                  "        1 - by line number\n"
                  "        2 - by origin stop\n"
                  "        3 - by destination stop\n"
                  "        4 - by stop\n"
                  "        5 - exit")
            want_to_search = select_option("select your choice: ", 5)
            break
        except ValueError:
            print("must be a number")
        except BestBusCompanyException as e:
            print(e)

    match want_to_search:
        case 1:
            while True:
                try:
                    line_number = int(input("insert line number: "))
                    break
                except ValueError:
                    print("must be number")
                except BestBusCompanyException as e:
                    print(e)
            best_bus_ever.search_route_by_line(line_number)
        case 2:
            origin = insert_origion_or_destination("insert origin to search: ")
            best_bus_ever.search_route_by_origin(origin)
        case 3:
            destination = insert_origion_or_destination("insert destination to search: ")
            best_bus_ever.search_route_by_destination(destination)
        case 4:
            stop = insert_origion_or_destination("insert stop to search: ")
            best_bus_ever.search_route_by_stop(stop)
        case 5:
            return False


def report_route_delay():
    print("report delay - ")
    while True:
        try:
            line_number = int(input("insert line number: "))
            break
        except ValueError:
            print("must be number")
        except BestBusCompanyException as e:
            print(e)
    schedule_id = int(input("Choose the ride you want to report - insert the scheduled ID: "))
    best_bus_ever.report_delay(line_number, schedule_id)


def manager():
    while True:
        try:
            manager_menu()
            action = select_option("select your action choice: ", 5)
            break
        except ValueError:
            print("must be number")
        except BestBusCompanyException as e:
            print(e)
    while True:
        match action:
            case 1:
                while True:
                    try:
                        print("add route. insert the following details:")
                        line_number = int(input("insert line number: "))
                        origin = insert_origion_or_destination("origin: ")
                        destination = insert_origion_or_destination("destination: ")
                        while True:
                            try:
                                list_of_stops = insert_stops()
                                break
                            except ValueError:
                                print("must be string of words and commas")
                            except BestBusCompanyException as e:
                                print(e)
                        # after validated all details, call the function from the company class:
                        best_bus_ever.add_route(line_number, origin, destination, list_of_stops)
                        break
                        ######### not break while loop!?!!?
                    except ValueError:
                        print("must be number")
                    except BestBusCompanyException as e:
                        print(e)
            # ---------------------------------------------------------------
            case 2:
                print("delete route. insert the following: ")
                while True:
                    try:
                        line_number = int(input("insert line number: "))
                        break
                    except ValueError:
                        print("must be number")
                    except BestBusCompanyException as e:
                        print(e)

                    while True:
                        try:
                            y_or_n = select_option(f"are you sure you want delete route no. {line_number}? y - 1/ n - 2 ",2)
                            break
                        except ValueError:
                            print("must be number")
                        except BestBusCompanyException as e:
                            print(e)
                    if y_or_n == 1:
                        best_bus_ever.delete_route(line_number)
                        break
                    elif y_or_n == 2:
                        print(f"line number {line_number} hadn't been deleted")
                        break

                # ----------------------------------------------------------------
            case 3:
                print("update route")
                while True:
                    try:
                        line_number = int(input("insert line number: "))
                    except ValueError:
                        print("must be number")
                    except BestBusCompanyException as e:
                        print(e)
                    best_bus_ever.display_route_from_routes(line_number)
                    break
                while True:
                    want_to_update = input("what would you like to update?\n"
                                               "    for origin station insert - 1 - \n"
                                               "    for destination station insert - 2 - \n"
                                               "    for list of stops insert - 3 - \n"
                                               "     that's it - 4 -").strip()
                    match want_to_update:
                        case '1':
                            print("update an origin station:")
                            new_origin = insert_origion_or_destination("    insert new origin: ")
                            best_bus_ever.update_route_origin(line_number, new_origin)
                        case '2':
                            print("update a destination station:")
                            new_destination = insert_origion_or_destination("   insert new destination: ")
                            best_bus_ever.update_route_destination(line_number, new_destination)
                        case '3':
                            print("update list of stops: ")
                            new_stops_list = insert_stops()
                            best_bus_ever.update_route_stops_list(line_number, new_stops_list)
                        case '4':
                            break

                # -------------------------------------------------------------------------------
            case 4:
                print("add scheduled ride.")
                while True:
                    try:
                        line_number = int(input("insert line number: "))
                        break
                    except ValueError:
                        print("must be number")
                    except BestBusCompanyException as e:
                        print(e)
                print(f"here are the exist schedules for line {line_number}: ")
                best_bus_ever.display_route_scheduled(line_number)
                print("for adding new scheduled ride, insert the following: ")
                origin_time_str = input("insert origin time hh:mm: ")
                origin_time_str = origin_time_str.split(":")
                origin_time = time(int(origin_time_str[0]), int(origin_time_str[1]))
                origin_time = origin_time.strftime("%H:%M")
                destination_time_str = input("insert destination time hh:mm: ")
                destination_time_str = destination_time_str.split(":")
                destination_time = time(int(destination_time_str[0]), int(destination_time_str[1]))
                destination_time = destination_time.strftime("%H:%M")
                driver_name = input("driver_name: ")
                best_bus_ever.add_scheduled_ride_for_route(line_number, origin_time, destination_time, driver_name)
                # ---------------------------------------------------------------------------------
            case 5:
                break

# ----------------------------------------------------------------------------------
if __name__ == "__main__":

    # check whether this is the first time you run the app
    # if this is the first time - create a new class
    if not os.path.exists('bus_company.pickle'):
        best_bus_ever = BestBusCompany()
    else:
        # if this is not the first time - we already have a DB
        # with data from the previous runs
        with open('bus_company.pickle', 'rb') as fh:
            best_bus_ever = pickle.load(fh)

    # here comes your code that runs main menu
    # and interacts with the user and adds/ updates
    # data in your bus_company class

    print(" ******************* Welcome to Best Bus Ever ********************")
    while True:
        try:
            m_or_p = select_option("Insert 1 for Passenger, 2 for Manager: ", 2)
            break
        except ValueError:
            print("must be a number")
        except BestBusCompanyException as e:
            print(e)


#   ------------------------------------------------------------------
    if m_or_p == 1:
        exit_menu = False
        while not exit_menu:

            while True:
                passenger_menu()
                try:
                    action = select_option("Select your action: ", 3)
                    break
                except ValueError:
                    print("must be a number")
                except BestBusCompanyException as e:
                    print(e)
            if action == 3:
                exit_menu = True

            if action == 1:
                want_to_search()

            elif action == 2:
                want_to_search()
                report_route_delay()


    my_password = "RideWithUs!"
    if m_or_p == 2:
        # if password false - exit program
        if manager_authentication(my_password):
            exit_menu = False
        else:
            exit_menu = True
        while not exit_menu:
            manager()
        print("bye")


    # before exiting the program, persist the current state
    # of the system in the file, so next time it will be loaded
    with open('bus_company.pickle', 'wb') as fh:
        pickle.dump(best_bus_ever, fh)