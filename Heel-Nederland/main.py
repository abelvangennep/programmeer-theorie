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


if __name__ == '__main__':
    best_score = 0
    attempts = 100

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

