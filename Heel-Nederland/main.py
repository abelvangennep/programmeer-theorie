import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "visualize"))

from connection import Connection
from station import Station
from randomsolution import random_solution
from loaddata import load_data, load_stations, load_connections
from traject import Traject
from calculatefunction import calculate
from cut import cut
from paste import paste
from stations import Stations
from userinput import boolean_input
from visualize import draw_traject


if __name__ == '__main__':
    best_score = 0
    attempts = 10

    # Prompt user for heuristiek: In one traject a train should never get twice to the same station.
    while True:
        connection_only_once = input("Should a station only be visited once, per traject.").lower()
        connection_only_once = boolean_input(connection_only_once)
        if not connection_only_once == 3:
            break

    # Prompt user for heuristiek: Random station chooses a station with one connection
    while True:
        station_1_connection = input("Do you prefer to start with a station, which has only one connection.").lower()
        station_1_connection = boolean_input(station_1_connection)
        if not connection_only_once == 3:
            break

    # Prompt user for heuristiek: Random station chooses a station with an uneven number of connections
    while True:
        station_uneven_connections = input("Do you prefer to start with a station, with an uneven number of connections.").lower()
        station_uneven_connections = boolean_input(station_uneven_connections)
        if not connection_only_once == 3:
            break

    # Prompt user for heuristiek: Cut a traject if the begin or end connection is already in an other traject
    while True:
        cut_connections = input("Do you prefer to cut connections, if the beginning or end is already in an other traject.").lower()
        cut_connections = boolean_input(cut_connections)
        if not connection_only_once == 3:
            break

    # Prompt user for heuristiek: Paste 2 trajects if their total time is less then 180min and their begin and start station is the same
    while True:
        paste_connections = input("Do you prefer to paste trajects together,if their total time is less then 180min and their begin and start station is equal.").lower()
        paste_connections = boolean_input(paste_connections)
        if not connection_only_once == 3:
            break


    # Load data from csv files with all the connections and their travel time
    data_list = load_data("data/ConnectiesNationaal.csv")
    stations_data = load_data("data/StationsNationaal.csv")

    for _ in range(attempts):
        # Stations_object is a dictionary in which all the station objects are loaded
        stations_objects = load_stations(data_list, stations_data)

        # Connection_objects is a list of all the connection, which are loaded from data_list
        connection_objects = load_connections(data_list, stations_objects)
        # Solution random, generates a random solution with possibly some heuristieken
        solution = random_solution(stations_objects, connection_objects, station_1_connection, station_uneven_connections, connection_only_once)
        if cut_connections:
            # Cut a connection from a "traject" if the begin or end connection is in an other traject
            solution = cut(solution)

        if paste_connections:
            # Paste 2 trajects if their total time is less then 180min and their begin and start station is the same
            solution = paste(solution)

        # Calculate the K of a solution
        score = calculate(solution)

        if score > best_score:
            best_solution = solution
            best_score = score

    f= open("output.csv","a+")
    f.write("trein, lijnvoering\n")
    for traject in best_solution["trajecten"]:
        f.write(f"trein, {traject}\n")
    f.close()

    # Append the best_score to a text file
    f= open("solution.txt","a+")
    f.write(f"attempts:{attempts}\n" f"SCORE:{best_score}\n\n")
    f.close()

    draw_traject(best_solution, stations_objects)
