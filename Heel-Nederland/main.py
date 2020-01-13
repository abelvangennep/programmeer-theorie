import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from connection import Connection
from station import Station
from randomsolution import random_solution, solution_1_city
from loaddata import load_data, load_stations, load_connections
from traject import Traject
from calculatefunction import calculate
from cut import cut 
from stations import Stations


if __name__ == '__main__':
    best_score = 0
    attempts = 1

    # raw_input returns the empty string for "enter"
    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}

    # Prompt user for heuristiek: Random station chooses a station with one connection
    station_1_connection = input("Do you prefer to start with a station, which has only one connection.").lower()
    if station_1_connection in yes:
        station_1_connection = True
    elif station_1_connection in no:
        station_1_connection = False
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")

    # Prompt user for heuristiek: Random station chooses a station with an uneven number of connections
    station_uneven_connections = input("Do you prefer to start with a station, with an uneven number of connections.").lower()
    if station_uneven_connections in yes:
        station_uneven_connections = True
    elif station_uneven_connections in no:
        station_uneven_connections = False
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")

    for _ in range(attempts):
        data_list = load_data("data/ConnectiesNationaal.csv")

        stations_objects = load_stations(data_list)

        connection_objects = load_connections(data_list, stations_objects)

        solution = random_solution(stations_objects, connection_objects)
        solution = cut(solution)
        score = calculate(solution)

        if score > best_score:
            best_score = score

    f= open("solution.txt","a+")
    f.write(f"attempts:{attempts}\n" f"SCORE:{best_score}\n\n")
    f.close()
    
    

