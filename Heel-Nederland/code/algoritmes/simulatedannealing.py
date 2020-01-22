# from .train import Train
from calculatefunction import calculate
from train import Train
import math
import random
import copy
import time
import timeit

import random

def simulated_annealing(solution, stations_dict):

    start = timeit.default_timer()
    max = 180
    temperature = 600
    cooling_factor = 0.999
    temperature_end = 10
    iteration = 0
    trains = solution["trains"]
    

    while temperature > temperature_end:
        iteration += 1

        solution_2 = {}
        solution_2["total_connections"] = solution["total_connections"]
        solution_2["trains"] =  []

        train = random.choice(trains)

        for every_train in trains:
            if every_train is train:
                station = stations_dict.get_complete_random_start_station()
                new_train = Train(station)
                solution_2["trains"].append(new_train)
            else:
                solution_2["trains"].append(every_train)


        while True:
            visited_stations = False
            station_only_once = False

            connection = new_train.get_random_connection(visited_stations, station_only_once)

            if new_train.travel_time + connection.travel_time > max:
                break

            new_train.add_connection(connection)

        K_train_1 = calculate(solution)
        K_train_2 = calculate(solution_2)

        difference = K_train_2 - K_train_1
        print("________________")
        print(K_train_1)
        print(K_train_2)
        print(iteration)
        print("17:", math.exp(difference / temperature))
        if difference > 0 or math.exp(difference / temperature) > random.uniform(0, 1):
            trains.remove(train)
            trains.append(new_train)
            print("accepted")
        else:
            print("declined")

        temperature = temperature * cooling_factor

    stop = timeit.default_timer()
    print('Time: ', stop - start)  

    
    return solution_2


    
        


