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

    # ...  
    data = ""
    max_minutes = 0
    max_trains = 0  
    holland = input("Please choose:\nNoord- en Zuid-Holland (1)\nor Heel Nederland (2)\n")
    while True: 
        option_1 = ['1','noord- en zuid-holland']
        option_2 = ['2', 'heel nederland', '']

        if holland.lower() in option_1: 
            data = "data/ConnectiesHolland.csv"
            max_minutes = 120
            max_trains = 7 
            break 
        elif holland.lower() in option_2:
            data = "data/ConnectiesNationaal.csv"
            max_minutes = 180
            max_trains = 20 
            break
        else: 
            holland = input("Invalid input. Please type '1' or '2'. ")
    

    
    # Advanced 
    skip_station = input("\nDoes a train station need to be avoided? ")
    skip_station = boolean_input(skip_station)
    if skip_station: 
        skip_station = input("Which station? ")

    # Load data from the csv files with all the connections and their travel times
    data_list = load_data(data, skip_station)

    while True: 
        if data_list == False: 
            skip_station = False
            data_list = load_data(data, skip_station)
            stations_data = load_data("data/StationsNationaal.csv", skip_station)
            all_stations = load_stations(data_list, stations_data)

            skip_station = input(f"This station is invalid. Please choose from the following:\n\n{all_stations}\n\n")
            data_list = load_data(data, skip_station)
        elif data_list != False: 
                break 

    change_connections = input("\nShould any connections be changed? ")
    change_connections = boolean_input(change_connections)

    # ... 
    random = input("\nPlease choose: \nCompletely random (1) \nor Random with Heuristics (2)\n")
    heuristics = False
    while True: 
        option_1 = ['1', 'random', 'completely random']
        option_2 = ['2', 'heuristics', 'random with heuristics', '']

        if random.lower() in option_1: 
            # Set all heuristics to false 
            station_only_once = False 
            station_1_connection = False 
            station_uneven_connections = False 
            cut_connections = False
            paste_connections = False
            break 
        elif random.lower() in option_2: 
            heuristics = True
            break 
        else: 
            random = input("Invalid input. Please type '1' or '2'. ")

    # Prompt the user for which heuristics they want to apply, if they chose this option 
    if heuristics: 
        print("\nPlease choose which heuristics to apply. Respond with yes or no for each heuristic:")

        station_only_once = input("Visit a station only once per train. ")
        station_only_once = boolean_input(station_only_once)

        station_1_connection = input("Start a train with a station that only has one connection. ")
        station_1_connection = boolean_input(station_1_connection)

        station_uneven_connections = input("Start a train with a station that has an uneven number of connections. ")
        station_uneven_connections = boolean_input(station_uneven_connections)

        cut_connections = input("Delete already visited connections, where possible. ")
        cut_connections = boolean_input(cut_connections)

        paste_connections = input("Join trains together, if possible. ")
        paste_connections = boolean_input(paste_connections)

    # ...
    sim_annealing = input("\nDo you want to use the Simulated Annealing algorithm?\n")
    sim_annealing = boolean_input(sim_annealing)

    # # Load data from the csv files with all the connections and their travel times
    # data_list = load_data(data, skip_station)
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
        # if connection_objects == False: 
        #     skip_data = input(f"This station is invalid! Please choose from {stations_objects}")

        # Solution random, generates a random solution with chosen heuristics 
        solution = random_solution(stations_objects, connection_objects, station_1_connection, station_uneven_connections, station_only_once, max_minutes, max_trains)
        
        if cut_connections:
            # Cut a connection from a "train" if the begin or end connection is in an other train
            solution = cut(solution)

        if paste_connections:
            # Paste 2 trains if their total time is less then 180min and their begin and start station is the same
            solution = paste(solution)

        solution = delete_trains(solution)


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

    if sim_annealing: 
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

        draw_train(better_solution, stations_objects)
        # draw_train_holland(best_solution, stations_objects)
    else:
        draw_train(best_solution, stations_objects)

# ... 
def boolean_input(user_input):
    yes = ['yes', 'y', 'ye', '']
    no = ['no', 'n']

    while True: 
        if user_input.lower() in yes:
            user_input = True
            break 
        elif user_input.lower() in no:
            user_input = False
            break 
        else:
            user_input = input("Invalid input. Please respond with yes or no. ")

    return user_input

# remove trains
def delete_trains(solution):
    trains = solution["trains"]
    existing_trains = []

    for train in trains:
        if train.travel_time > 0:
            existing_trains.append(train)

    solution["trains"] = existing_trains

    return solution


if __name__ == '__main__':
    main()
