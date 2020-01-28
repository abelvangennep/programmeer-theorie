import os
import sys
import math
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "heuristics"))
sys.path.append(os.path.join(directory, "code", "visualize"))
sys.path.append(os.path.join(directory, "code", "helper"))

from calculatefunction import calculate
from simulatedannealing import simulated_annealing
from visualize import draw_train, draw_train_holland
from stations import Stations
from paste import paste
from cut import cut
from train import Train
from loaddata import load_data, load_stations, load_connections
from randomsolution import random_solution
from station import Station
from connection import Connection


def main():
    best_score = 0

    # Load all stations from the csv file
    skip = False
    stations_data = load_data("data/StationsNationaal.csv", skip)

    # Prompt user for necessary input
    user_choices = user_interface(stations_data)

    # Load the connections data from the csv file of either Heel Nederland
    # or Noord- en Zuid Holland, depending on the user's input,
    # skipping a station if necessary
    data_list = load_data(user_choices["data"], user_choices["skip"])

    for _ in range(user_choices["attempts"]):
        # Load all station objects into a dictionary 
        stations_objects = load_stations(data_list, stations_data)

        # Connection_objects is a list of all the connection,
        # which are loaded from data_list
        connection_objects = load_connections(
            data_list, stations_objects, user_choices["change_connections"])

        # Generate a random solution with chosen heuristics
        solution = random_solution(stations_objects, connection_objects,\
            user_choices)

        # Run the heuristic of "cutting" trains, if the user chose this option
        if user_choices["cut_connections"]:
            solution = cut(solution)

        # Run the heuristic of "pasting" trains, if the user chose this option
        if user_choices["paste_connections"]:
            solution = paste(solution, user_choices["max_minutes"])

        solution = delete_trains(solution)

        # Calculate the K of a solution
        score = calculate(solution)

        # Set score to new values
        if score > best_score:
            best_solution = solution
            best_score = score

    # Open outputfile
    f = open("output.csv", "w")
    f.write("random:\ntrein, lijnvoering\n")

    counter = 0

    # Write random solution to outputfile
    for train in best_solution["trains"]:
        counter += 1
        f.write(f'train_{counter}, "{train}"\n')
    f.write(f"SCORE:{best_score}\n\n")
    f.close()

    # If simulated annealing is chosen
    if user_choices["sim_annealing"] == True:
        best_solution = simulated_annealing(
            solution, stations_objects, user_choices)
        better_score = calculate(best_solution)

        # Open outputfile
        f = open("output.csv", "a+")
        f.write("simulated annealing:\ntrein, lijnvoering\n")
        counter = 0

        # Write simulated annealing solution to outputfile
        for train in best_solution["trains"]:
            counter += 1
            f.write(f'trein_{counter}, "{train}"\n')
        f.write(f"SCORE:{better_score}\n\n")
        f.close()

        # If heuristic cut is chosen
        if user_choices["SA_cut_connections"]:
            best_solution = cut(best_solution)

        # If heuristic paste is chosen
        if user_choices["SA_paste_connections"]:
            best_solution = paste(best_solution, user_choices["max_minutes"])

        best_solution = delete_trains(best_solution)

        better_score = calculate(best_solution)

        # Open outputfile
        f = open("output.csv", "a+")
        f.write("simulated annealing:\ntrein, lijnvoering\n")
        counter = 0

        # Write simulated annealing solution to outputfile
        for train in best_solution["trains"]:
            counter += 1
            f.write(f'trein_{counter}, "{train}"\n')
        f.write(f"SCORE:{better_score}\n\n")
        f.close()


    # Draw the map
    # if user_choices["data"] == "data/ConnectiesHolland.csv":
    #     draw_train_holland(best_solution, stations_objects)
    # else:
    #     draw_train(best_solution, stations_objects)


def user_interface(stations_data):
    """User interface"""
    user_choices = {}

    # Set options for yes or no questions
    option_1 = ['yes', 'ye', 'y', '']
    option_2 = ['no', 'n']

    print("\n********** MAP **********\n")

    # Ask user for which part of the map the train routes should be calculated
    holland = input(
        "Please choose:\nNoord- en Zuid-Holland (1)\nor Heel Nederland (2)\n")

    # Set options for this question
    option_1_holland = ['1', 'noord- en zuid-holland']
    option_2_holland = ['2', 'heel nederland', '']

    holland = string_input(holland, option_1_holland, option_2_holland)
    # Set the variables for data file, maximum amount of trains 
    # and minutes per train, depending on the user's choice
    if holland == "1":
        user_choices["data"] = "data/ConnectiesHolland.csv"
        user_choices["max_minutes"] = 120
        user_choices["max_trains"] = 7
    else:
        user_choices["data"] = "data/ConnectiesNationaal.csv"
        user_choices["max_minutes"] = 180
        user_choices["max_trains"] = 20

    # Ask the user if a station should be omitted (part of advanced)
    skip_station = string_input(
        input("\nShould a specific station be avoided? "), option_1, option_2)

    # If the user chooses to skip a station, prompt for which one
    if skip_station == "1":
        skip_station = input("What station? ")

        # Load all possible stations into a list
        all_stations = []
        for row in stations_data:
            all_stations.append(row[0].lower())

        while True:
            if skip_station.lower().rstrip() in all_stations:
                break
            # If the user's input is invalid, ask again and show the list of 
            # all possible stations
            skip_station = input(
                f"This station is invalid. Please choose from the following:\
                    \n\n{all_stations}\n\n")
    else:
        skip_station = False

    user_choices["skip"] = skip_station

    # Ask user if 3 connections should be changed randomly (part of advanced)
    change_connections = input(
        "\nDo you want 3 connections to be changed randomly? ")
    user_choices["change_connections"] = False
    if string_input(change_connections, option_1, option_2) == "1":
        user_choices["change_connections"] = True

    print("\n********** ALGORITHM **********")

    # Ask user if they want to run a completely random algorithm 
    # or employ certain heuristics
    random = input(
        "\nPlease choose: \nCompletely random (1)\
            \nor Random with Heuristics (2)\n")
    option_1_random = ['1', 'random', 'completely random']
    option_2_random = ['2', 'heuristics', 'random with heuristics', '']
    random = string_input(random, option_1_random, option_2_random)

    # Set all heuristics to false
    user_choices["station_only_once"] = False
    user_choices["station_1_connection"] = False
    user_choices["station_uneven_connections"] = False
    user_choices["cut_connections"] = False
    user_choices["paste_connections"] = False

    # Prompt the user for which heuristics they want to apply, 
    # if they chose this option
    if random == "2":
        print("\nPlease choose which heuristics to apply. Respond with 'yes'"\
        " or 'no' for each heuristic:")

        # Set heuristic to true, if the user chooses this option
        if string_input(input("Visit a station only once per train. "),\
            option_1, option_2) == "1":
            user_choices["station_only_once"] = True
        if string_input(input("Start a train with a station that only has one"\
            " connection. "), option_1, option_2) == "1":
            user_choices["station_1_connection"] = True
        if string_input(input("Start a train with a station that has an"\
            " uneven number of connections. "), option_1, option_2) == "1":
            user_choices["station_uneven_connections"] = True
        if string_input(input("Delete already visited connections, where"\
            " possible. "), option_1, option_2) == "1":
            user_choices["cut_connections"] = True
        if string_input(input("Join trains together, if possible. "),\
            option_1, option_2) == "1":
            user_choices["paste_connections"] = True

    # Ask the user if they want to run the simulated annealing algorithm
    sim_annealing = input(
        "\nDo you want to use the Simulated Annealing algorithm? ")
    user_choices["sim_annealing"] = False
    if string_input(sim_annealing, option_1, option_2) == "1":
        user_choices["sim_annealing"] = True

    # Ask user if they want to employ certain heuristics in combination
    # with Simulated Annealing
    if user_choices["sim_annealing"]: 
        sim_annealing_heuristics = input(
            "\nPlease choose: \nSimmulated Annealing without heuristics (1)"\
                " \nor Random Simmulated Annealing with Heuristics (2)\n")
        option_1_random = ['1', 'random', 'completely random']
        option_2_random = ['2', 'heuristics', 'random with heuristics', '']
        random = string_input(random, option_1_random, option_2_random)

        # Set all heuristics to false
        user_choices["SA_station_only_once"] = False
        user_choices["SA_station_1_connection"] = False
        user_choices["SA_station_uneven_connections"] = False
        user_choices["SA_cut_connections"] = False
        user_choices["SA_paste_connections"] = False

        if sim_annealing_heuristics == "2":
            print("\nPlease choose which heuristics to apply. Respond with 'yes'"\
                " or 'no' for each heuristic:")

            # Set heuristic to true, if the user chooses this option
            if string_input(input("Visit a station only once per train. "),\
                option_1, option_2) == "1":
                user_choices["SA_station_only_once"] = True
            if string_input(input("Start a train with a station that only has"\
                " one connection. "), option_1, option_2) == "1":
                user_choices["SA_station_1_connection"] = True
            if string_input(input("Start a train with a station that has an"\
                " uneven number of connections. "), option_1, option_2) == "1":
                user_choices["SA_station_uneven_connections"] = True
            if string_input(input("Delete already visited connections, where"\
                " possible. "), option_1, option_2) == "1":
                user_choices["SA_cut_connections"] = True
            if string_input(input("Join trains together, if possible. "),\
                option_1, option_2) == "1":
                user_choices["SA_paste_connections"] = True

    print("\n********** RUNTIME **********")
    user_choices["attempts"] = number_input(input(
        "\nHow many times to do you want to run the random algorithm? "),\
            int, 0, None)

    user_choices["start_temperature"] = 180
    user_choices["end_temperature"] = 5
    user_choices["cooling_factor"] = 0.9999
    user_choices["trains"] = 10

    if user_choices["sim_annealing"]:
        change_default = string_input(input(
            "\nDo you want to change the default settings for simulated"\
                " annealing? "), option_1, option_2)
        if change_default == "1":
            user_choices["start_temperature"] = number_input(
                input("Starting temperature? (default: 180) "), int, 0, None)
            user_choices["end_temperature"] = number_input(input(
                "End temperature? (default: 5) "), int, 0,\
                    user_choices["start_temperature"])
            user_choices["cooling_factor"] = number_input(
                input("Cooling factor? (default: 0.9999) "),\
                    float, 0, 1)
            user_choices["trains"] = number_input(input(
                f"Number of trains? (default: 10"), int, 0,\
                        user_choices['max_trains'] + 1)

    return user_choices


def number_input(user_input, data_type, min, max):
    """Check if number input is valid and return the user's input."""
    while True:
        try:
            user_input = data_type(user_input)
            if max == None:
                while True:
                    if user_input > int(min):
                        return user_input
                    else:
                        user_input = input(
                            f"Please respond with a number higher than {min}. ")
                        break
            else:
                while True:
                    if user_input > int(min) and user_input < int(max):
                        return user_input
                    else:
                        user_input = input(
                            f"Please respond with a number between {min} and"\
                                " {max}. ")
                        break
        except ValueError:
            user_input = input("Please respond with a number. ")


def string_input(user_input, option_1, option_2):
    """Check if string input is valid and return which option the user chooses."""
    while True:
        if user_input.lower().rstrip() in option_1:
            return "1"
        elif user_input.lower().rstrip() in option_2:
            return "2"
        else:
            user_input = input(
                f"Invalid input. Please respond with '{option_1[0]}' or"\
                    f" '{option_2[0]}'. ")


def delete_trains(solution):
    """Remove empty trains from solution."""
    trains = solution["trains"]
    existing_trains = []

    for train in trains:
        if train.travel_time > 0:
            existing_trains.append(train)

    solution["trains"] = existing_trains

    return solution


if __name__ == '__main__':
    main()
