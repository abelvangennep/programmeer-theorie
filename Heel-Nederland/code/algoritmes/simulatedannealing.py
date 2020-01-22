# from .train import Train
from calculatefunction import calculate
import math
import random
import copy
import time

import random

def simulated_annealing(solution, stations_dict):
    max = 180
    temperature = 160
    cooling_factor = 0.99
    temperature_end = 10
    iteration = 0

    while temperature > temperature_end:
        iteration += 1

        solution_2 = copy.deepcopy(solution)
        trains_2 = solution_2["trains"]
        K_train_1 = calculate(solution)
        train = random.choice(trains_2)

        train.empty_train()

        station = stations_dict.get_complete_random_start_station()

        train.set_start_station(station)

        while True:
            visited_stations = False
            station_only_once = False

            connection = train.get_random_connection(visited_stations, station_only_once)

            if train.travel_time + connection.travel_time > max:
                break

            train.add_connection(connection)

        K_train_2 = calculate(solution_2)

        difference = K_train_2 - K_train_1
        print("________________")
        print(K_train_1)
        print(K_train_2)
        print(iteration)
        print("17:", math.exp(difference / temperature))
        if difference > 0 or math.exp(difference / temperature) > random.uniform(0, 1):
            solution = solution_2
            print("accepted")
        else:
            print("declined")

        temperature = temperature * cooling_factor
        # time.sleep(1)

    return solution_2
