import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from connection import Connection
from station import Station
from randomsolution import random_solution
from loaddata import load_data, load_stations, load_connections
from traject import Traject
from calculatefunction import calculate


if __name__ == '__main__':
    data_list = load_data("data/ConnectiesHolland.csv")

    stations_objects = load_stations(data_list)

    connection_objects = load_connections(data_list, stations_objects)

    solution = random_solution(stations_objects, connection_objects)

    calculate(solution)