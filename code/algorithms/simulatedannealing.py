import math
import random
import copy

from calculatefunction import calculate
from visualize import see_annealing
from train import Train


def simulated_annealing(solution, stations_dict, user_choices):
    """
    This method returns a simulated annealing solution with or without heuristics
    """

    # Set variables with choices user made
    max_minutes = user_choices["max_minutes"]
    temperature = user_choices["start_temperature"]
    temperature_end = user_choices["end_temperature"]
    cooling_factor = user_choices["cooling_factor"]
    max_trains = user_choices["trains"]
    iteration = 0
    trains = solution["trains"]
    score = []

    # Calculate the difference between the amount of trains in the solution and
    # desired amount of trains
    number_of_trains_difference = len(solution["trains"]) - max_trains

    # If the difference is bigger than 0 delete trains
    if number_of_trains_difference > 0:
        for train in trains[max_trains:]:
            for connection in train.connections:
                connection.delete_visit()
        del solution["trains"][max_trains:]

    # If the difference is smaller than 0 add trains
    elif number_of_trains_difference < 0:
        for _ in range(number_of_trains_difference):
            station = stations_dict.get_completely_random_station()
            new_train = Train(station)

    # Create a new dictionary solution to compare the old solution with
    solution_temp = {}
    solution_temp["total_connections"] = solution["total_connections"]

    # Iterate untill the temperature is equal or smaller than the desired end
    while temperature > temperature_end:
        iteration += 1

        # Empty temporary solution and choose a random train
        solution_temp["trains"] =  []
        train = random.choice(trains)

        # Append al the trains to the temporary solution, except the chosen
        # train and create a new train
        for every_train in trains:
            if every_train is train:
                station = stations_dict.get_random_station(user_choices\
                        ["SA_station_uneven_connections"]\
                        , user_choices["SA_station_1_connection"])
                new_train = Train(station)
                solution_temp["trains"].append(new_train)
            else:
                solution_temp["trains"].append(every_train)

        visited_stations = []

        while True:
            # Get random connection or with heuristics if chosen
            connection = new_train.get_random_connection(visited_stations, \
                         user_choices["SA_station_only_once"])

            if user_choices["SA_station_only_once"]:
                visited_stations.append(connection.station_1)
                visited_stations.append(connection.station_2)

            # Break if maximum train duration is reached
            if new_train.travel_time + connection.travel_time > max_minutes:
                break

            new_train.add_connection(connection)

        # Calculate the score of both solutions and compare the outcomes
        K_train_1 = calculate(solution)
        K_train_2 = calculate(solution_temp)
        difference = K_train_2 - K_train_1

        # Append score to a list
        score.append(K_train_1)

        # Change the solution, when new train is accepted
        if difference > 0 or math.exp(difference / temperature) > \
            random.uniform(0, 1):

            for connection in train.connections:
                connection.delete_visit()

            trains.remove(train)
            trains.append(new_train)

        # When the new train isn't accepted
        else:
            for connection in new_train.connections:
                connection.delete_visit()

        # Reduce temperature
        temperature = temperature * cooling_factor

    # Run visualisation
    see_annealing(score)

    return solution
