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
from visualize import draw_train
from simulatedannealing import simulated_annealing
from calculatefunction import calculate
import math

def main():
    best_score = 0

    user_choices = user_interface()

    # Load data from the csv files with all the connections and their travel times
    data_list = load_data( user_choices["data"],  user_choices["skip"])
    stations_data = load_data("data/StationsNationaal.csv",  user_choices["skip"])

    for _ in range(user_choices["attempts"]):
        # Stations_object is a dictionary in which all the station objects are loaded
        stations_objects = load_stations(data_list, stations_data)

        # Connection_objects is a list of all the connection, which are loaded from data_list
        connection_objects = load_connections(data_list, stations_objects, user_choices["change_connections"])

        # Generate a random solution with chosen heuristics
        solution = random_solution(stations_objects, connection_objects,  user_choices["station_1_connection"],  user_choices["station_uneven_connections"],  user_choices["station_only_once"],  user_choices["max_minutes"],  user_choices["max_trains"])

        if  user_choices["cut_connections"] == True:
            # Cut a connection from a "train" if the begin or end connection is in an other train
            solution = cut(solution)

        if  user_choices["paste_connections"] == True:
            # Paste 2 trains if their total time is less then 180min and their begin and start station is the same
            solution = paste(solution)

        solution = delete_trains(solution)

        # Calculate the K of a solution
        score = calculate(solution)

        if score > best_score:
            best_solution = solution
            best_score = score


    f= open("outputfiles/output.csv","a+")
    f.write("random: train, lijnvoering\n")
    for train in best_solution["trains"]:
        f.write(f"train, {train}\n")
    f.close()

    # Append the best_score to a text file
    f= open("outputfiles/solution.txt","a+")
    f.write(f"random: attempts:{user_choices['attempts']}\n" f"SCORE:{best_score}\n\n")
    f.close()

    if  user_choices["sim_annealing"]:
        better_solution = simulated_annealing(solution, stations_objects)
        better_score = calculate(better_solution)

        f= open("outputfiles/output.csv","a+")
        f.write("simulated annealing: train, lijnvoering\n")
        for train in better_solution["trains"]:
            f.write(f"train, {train}\n")
        f.close()

        # Append the best_score to a text file
        f= open("outputfiles/solution.txt","a+")
        f.write(f"simulated annealing\n" f"SCORE:{better_score}\n\n")
        f.close()


    draw_train(better_solution, stations_objects)
    # draw_train_holland(best_solution, stations_objects)
    draw_train(best_solution, stations_objects)


def user_interface():

    user_choices = {}

    option_1 = ['yes', 'ye', 'y', '']
    option_2 = ['no', 'n']

    print("\n********** MAP **********\n")

    # Ask user for which part of the map the train routes should be calculated
    holland = input("Please choose:\nNoord- en Zuid-Holland (1)\nor Heel Nederland (2)\n")
    option_1_holland = ['1','noord- en zuid-holland']
    option_2_holland = ['2', 'heel nederland', '']

    holland = result_input(holland, option_1_holland, option_2_holland)
    if holland == "1":
        user_choices["data"] = "data/ConnectiesHolland.csv"
        user_choices["max_minutes"] = 120
        user_choices["max_trains"] = 7
    else:
        user_choices["data"] = "data/ConnectiesNationaal.csv"
        user_choices["max_minutes"] = 180
        user_choices["max_trains"] = 20

    # Ask user if a station should be omitted (part of advanced)
    user_choices["skip"] = False

    skip_station = input("\nShould a specific station be avoided? ")
    skip_station = result_input(skip_station, option_1, option_2)

    if skip_station == "1":
        skip_station = input("What station? ")

        # Load data from the csv files with all the connections and their travel times
        data_list = load_data(user_choices["data"], skip_station)

        while True:
            if data_list == False:
                skip_station = False
                data_list = load_data(user_choices["data"], skip_station)
                stations_data = load_data("data/StationsNationaal.csv", skip_station)
                all_stations = load_stations(data_list, stations_data)

                skip_station = input(f"This station is invalid. Please choose from the following:\n\n{all_stations}\n\n")
                data_list = load_data(user_choices["data"], skip_station)
            elif data_list != False:
                user_choices["skip"] = skip_station
                break

    # Ask user if 3 connections should be changed randomly (part of advanced)
    change_connections = input("\nDo you want 3 connections to be changed randomly? ")
    user_choices["change_connections"] = False
    if result_input(change_connections, option_1, option_2) == "1":
        user_choices["change_connections"] = True

    print("\n********** ALGORITHM **********")

    # Ask user if they want to run a completely random algorithm or employ certain heuristics
    random = input("\nPlease choose: \nCompletely random (1) \nor Random with Heuristics (2)\n")
    option_1_random = ['1', 'random', 'completely random']
    option_2_random = ['2', 'heuristics', 'random with heuristics', '']
    random = result_input(random, option_1_random, option_2_random)

    # Set all heuristics to false
    user_choices["station_only_once"] = False
    user_choices["station_1_connection"] = False
    user_choices["station_uneven_connections"] = False
    user_choices["cut_connections"] = False
    user_choices["paste_connections"] = False

    # Prompt the user for which heuristics they want to apply, if they chose this option
    if random == "2":
        print("\nPlease choose which heuristics to apply. Respond with 'yes' or 'no' for each heuristic:")

        # Set heuristic to true, if the user chooses this option
        if result_input(input("Visit a station only once per train. "), option_1, option_2) == "1":
            user_choices["station_only_once"] = True
        if result_input(input("Start a train with a station that only has one connection. "), option_1, option_2) == "1":
            user_choices["station_1_connection"] = True
        if result_input(input("Start a train with a station that has an uneven number of connections. "), option_1, option_2) == "1":
            user_choices["station_uneven_connections"] = True
        if result_input(input("Delete already visited connections, where possible. "), option_1, option_2) == "1":
            user_choices["cut_connections"] = True
        if result_input(input("Join trains together, if possible. "), option_1, option_2) == "1":
            user_choices["paste_connections"] = True

    # Ask the user if they want to run the simulated annealing algorithm
    sim_annealing = input("\nDo you want to use the Simulated Annealing algorithm? ")
    user_choices["sim_annealing"] = False
    if result_input(sim_annealing, option_1, option_2) == "1":
        user_choices["sim_annealing"] = True

    print("\n********** RUNTIME **********")

    user_choices["attempts"] = number_input(input("\nHow many times to do you want to run the random algorithm? "), int, 0, None) 

    if sim_annealing: 
        change_default = result_input(input("\nDo you want to change the default settings for simulated annealing? "), option_1, option_2) 
        if change_default == "1": 
            user_choices["temperature"] = number_input(input("Starting temperature? (default: 160) "), int, 0, None)
            user_choices["end_temperature"] = number_input(input("End temperature? (default: 5) "), int, 0, user_choices["temperature"])
            user_choices["cooling_factor"] = number_input(input("Cooling factor? (default: 0.99, min: >0, max: <1) "), float, 0, 1)
            user_choices["trains"] = number_input(input(f"Number of trains? (default: random, max: {user_choices['max_trains']}) "), int, 0, user_choices['max_trains'] + 1) 

    return user_choices


def number_input(user_input, data_type, min, max): 
    while True: 
        try: 
            user_input = data_type(user_input)
            if max == None: 
                while True: 
                    if user_input > int(min): 
                        return user_input
                    else: 
                        user_input = input(f"Please respond with a number higher than {min}. ")
                        break 
            else: 
                while True: 
                    if user_input > int(min) and user_input < int(max): 
                        return user_input
                    else: 
                        user_input = input(f"Please respond with a number between {min} and {max}. ")
                        break 
        except ValueError: 
            user_input = input("Please respond with a number. ")

def result_input(user_input, option_1, option_2): 

    while True: 
        if user_input.lower().rstrip() in option_1: 
            return "1"
        elif user_input.lower().rstrip() in option_2: 
            return "2"
        else: 
            user_input = input(f"Invalid input. Please respond with '{option_1[0]}' or '{option_2[0]}'. ")

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
