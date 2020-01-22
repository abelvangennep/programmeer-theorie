import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "heuristics"))
sys.path.append(os.path.join(directory, "code", "visualize"))

from connection import Connection
from station import Station
from randomsolution import random_solution
from loaddata import load_data, load_stations, load_connections
from train import Train
from cut import cut
from paste import paste
from stations import Stations
from visualize import draw_train, draw_train_holland
from simulatedannealing import simulated_annealing
from calculatefunction import calculate
import math


def main():
    best_score = 0
    attempts = 1

    skip_station = input("Do you want to omit/avoid/skip a specific station? ")
    # skip_station = boolean_input(skip_station)

    # Prompt user for heuristiek: In one train a train should never get twice to the same station.
    station_only_once = input("Should a station only be visited once, per train.").lower()
    station_only_once = boolean_input(station_only_once)

    # Prompt user for heuristiek: Random station chooses a station with one connection
    station_1_connection = input("Do you prefer to start with a station, which has only one connection.").lower()
    station_1_connection = boolean_input(station_1_connection)

    # Prompt user for heuristiek: Random station chooses a station with an uneven number of connections
    station_uneven_connections = input("Do you prefer to start with a station, with an uneven number of connections.").lower()
    station_uneven_connections = boolean_input(station_uneven_connections)

    # Prompt user for heuristiek: Cut a train if the begin or end connection is already in an other train
    cut_connections = input("Do you prefer to cut connections, if the beginning or end is already in an other train.").lower()
    cut_connections = boolean_input(cut_connections)

    # Prompt user for heuristiek: Paste 2 trains if their total time is less then 180min and their begin and start station is the same
    paste_connections = input("Do you prefer to paste trains together,if their total time is less then 180min and their begin and start station is equal.").lower()
    paste_connections = boolean_input(paste_connections)
        

    # Load data from csv files with all the connections and their travel time
    data_list = load_data("data/ConnectiesNationaal.csv", skip_station)
    stations_data = load_data("data/StationsNationaal.csv", skip_station)

    for _ in range(attempts):
        # Stations_object is a dictionary in which all the station objects are loaded
        stations_objects = load_stations(data_list, stations_data)

        # Connection_objects is a list of all the connection, which are loaded from data_list
        connection_objects = load_connections(data_list, stations_objects)
        # Solution random, generates a random solution with possibly some heuristieken
        solution = random_solution(stations_objects, connection_objects, station_1_connection, station_uneven_connections, station_only_once)
        if cut_connections:
            # Cut a connection from a "train" if the begin or end connection is in an other train

            solution = cut(solution)

        if paste_connections:
            # Paste 2 trains if their total time is less then 180min and their begin and start station is the same
            solution = paste(solution)

        solution = delete_train(solution)

        
        # Calculate the K of a solution
        score = calculate(solution)

        if score > best_score:
            best_solution = solution
            best_score = score

    # print("0.4", math.exp(0.4))
    # print("0.2", math.exp(0.2))
    # print("-0.4", math.exp(-0.4))
    # print("0.001", math.exp(0.001))
    # print("2", math.exp(2))

    f= open("output.csv","a+")
    f.write("random: trein, lijnvoering\n")
    for train in best_solution["trains"]:
        f.write(f"trein, {train}\n")
    f.close()

    # Append the best_score to a text file
    f= open("solution.txt","a+")
    f.write(f"random: attempts:{attempts}\n" f"SCORE:{best_score}\n\n")
    f.close()

    better_solution = simulated_annealing(solution, stations_objects)
    better_score = calculate(better_solution)

    f= open("output.csv","a+")
    f.write("simulated annealing: trein, lijnvoering\n")
    for train in better_solution["trains"]:
        f.write(f"trein, {train}\n")
    f.close()

    # Append the best_score to a text file
    f= open("solution.txt","a+")
    f.write(f"simulated annealing: attempts:{attempts}\n" f"SCORE:{better_score}\n\n")
    f.close()

    # draw_train(better_solution, stations_objects)
    # # draw_train_holland(best_solution, stations_objects)

def boolean_input(user_input):
    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}

    if user_input in yes:
        user_input = True
    elif user_input in no:
        user_input = False
    else:
        sys.stdout.write("Please respond with 'yes' or 'no', you have now automatically chosen for the answer 'no' ")
        user_input = False

    return user_input

def delete_train(solution):
    trains = solution["trains"]
    existing_trains = []

    for train in trains:
        if train.travel_time > 0:
            existing_trains.append(train)

    solution["trains"] = existing_trains

    return solution


if __name__ == '__main__':
    main()
