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

def simulated_annealing(solution, stations_dict):
    """
    Simulated annealing is a probabilistic algorithm, which can calculte a globale optimum.
    The algorithm compares the scores of to different solutions, even a worse score can be excepted.
    To achieve the optimum, three parameters have to be optimized, the cooling_factor, temperature and end_temperature.
    """
    start = timeit.default_timer()
    
    score = []
    
    max_train_duration = 180
    temperature = 160
    cooling_factor = 0.99999
    temperature_end = 20
    iteration = 0
    amount_of_trains = 11
    trains = solution["trains"]

    # Calculate the difference between the amount of trains in the solution and desired amount of trains
    number_of_trains_difference = len(solution["trains"]) - amount_of_trains

    # If the difference is bigger then 0 delete trains,
    if number_of_trains_difference > 0:
        del solution["trains"][amount_of_trains:]

    # If the difference is smaller then 0 add trains
    elif number_of_trains_difference < 0:
        for _ in range(number_of_trains_difference):
            station = stations_dict.get_complete_random_start_station()
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
            visited_stations = False
            station_only_once = False

            # Select a random connection and append the connection if the total time limit is lower then max_train_duration 
            connection = new_train.get_random_connection(visited_stations, station_only_once)
            if new_train.travel_time + connection.travel_time > max_train_duration:
                break

            new_train.add_connection(connection)

        # Calculate the score of both solutions and compare the outcomes
        K_train_1 = calculate(solution)
        K_train_2 = calculate(solution_temp)
        difference = K_train_2 - K_train_1
         
        # Append score to a list
        score.append(K_train_1)

        
        print("________________")
        print(K_train_1)
        print(K_train_2)
        print(iteration)
        print("17:", math.exp(difference / temperature))

        # Change the solution, when new train is excepted
        if difference > 0 or math.exp(difference / temperature) > random.uniform(0, 1):
            trains.remove(train)
            trains.append(new_train)
        
        # Reduce temperature
        temperature = temperature * cooling_factor
    
    # Run visualisation
    see_annealing(score)

    # Print runtime of simulated annealing
    stop = timeit.default_timer()
    print('Time: ', stop - start)


    return solution
