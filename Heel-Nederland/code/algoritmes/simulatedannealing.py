# from .train import Train
from calculatefunction import calculate
from visualize import see_annealing
from train import Train
import math
import random
import copy
import time
import timeit
import random

def simulated_annealing(solution, stations_dict, user_choices):
    """
    Simulated annealing is a probabilistic algorithm, which can calculte a globale optimum.
    The algorithm compares the scores of to different solutions, even a worse score can be excepted.
    To achieve the optimum, three parameters have to be optimized, the cooling_factor, temperature and end_temperature.
    """
    start = timeit.default_timer()

    score = []

    max_train_duration = user_choices["max_minutes"]
    temperature = user_choices["start_temperature"] 
    temperature_end = user_choices["end_temperature"] 
    cooling_factor = user_choices["cooling_factor"] 
    iteration = 0
    amount_of_trains = user_choices["trains"]
    trains = solution["trains"]

    # Calculate the difference between the amount of trains in the solution and desired amount of trains
    number_of_trains_difference = len(solution["trains"]) - amount_of_trains

    # If the difference is bigger then 0 delete trains,
    if number_of_trains_difference > 0:
        for train in trains[amount_of_trains:]:
            for connection in train.connections:
                connection.delete_visit()
        del solution["trains"][amount_of_trains:]

    # If the difference is smaller then 0 add trains
    elif number_of_trains_difference < 0:
        for _ in range(number_of_trains_difference):
            station = stations_dict.get_random_start_station(user_choices["SA_station_uneven_connections"], user_choices["SA_station_1_connection"])
            new_train = Train(station)

    # Create a new dictionary solution to compare the old solution with
    solution_temp = {}
    solution_temp["total_connections"] = solution["total_connections"]

    # Itterate untill the temperature is equal or smaller then the desired end
    while temperature > temperature_end:
        iteration += 1

        # empty temporary solution, and choose a random train
        solution_temp["trains"] =  []
        train = random.choice(trains)

        # Append al the trains to the temporary solution, except the chosen train and create a new train
        for every_train in trains:
            if every_train is train:
                station = stations_dict.get_complete_random_start_station()
                new_train = Train(station)
                solution_temp["trains"].append(new_train)
            else:
                solution_temp["trains"].append(every_train)

        while True:
            visited_stations = []

            # Select a random connection and append the connection if the total time limit is lower then max_train_duration
            connection = new_train.get_random_connection(visited_stations, user_choices["SA_station_only_once"])
            
            if user_choices["SA_station_only_once"]:
                visited_stations.append(connection.station_1)
                visited_stations.append(connection.station_2)

            if new_train.travel_time + connection.travel_time > max_train_duration:
                break

            new_train.add_connection(connection)

        # Calculate the score of both solutions and compare the outcomes
        K_train_1 = calculate(solution)
        K_train_2 = calculate(solution_temp)
        difference = K_train_2 - K_train_1

        # Append score to a list
        score.append(K_train_1)

        # Change the solution, when new train is excepted
        if difference > 0 or math.exp(difference / temperature) > random.uniform(0, 1):
            
            for connection in train.connections:
                connection.delete_visit()
                
            trains.remove(train)
            trains.append(new_train)

        # If the new train isnt accepted 
        else:
            for connection in new_train.connections:
                connection.delete_visit()

        # Reduce temperature
        temperature = temperature * cooling_factor

    # Print runtime of simulated annealing
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    # Run visualisation
    see_annealing(score)


    return solution
