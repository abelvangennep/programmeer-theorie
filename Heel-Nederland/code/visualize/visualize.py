from __future__ import print_function

import os
import subprocess
import matplotlib.pyplot as plt

def draw_train(best_solution, stations_objects):

    # Set x ,y limits
    axes = plt.gca()
    axes.set_xlim(3.25, 7.3)
    axes.set_ylim(50.7, 53.7)

    # Set x, y label
    plt.xlabel("X")
    plt.ylabel("Y")

    # Set chart title
    plt.title("train")

    # Read and show image
    img = plt.imread("NLkaart.png")
    plt.imshow(img, aspect = "auto", extent = [3.25, 7.3, 50.65, 53.7])

    station_coordinates = []
    for station in stations_objects.stations.values():
        station_coordinates.append([station.y, station.x])
        plt.scatter(station.x, station.y, s = 5)

    for train in best_solution["trains"]:
        dict_coordinates = train.coordinates()
        x_list = dict_coordinates["x"]
        y_list = dict_coordinates["y"]
        plt.plot(x_list, y_list)
        plt.pause(1)

    plt.show()

def draw_train_holland(best_solution, stations_objects):

    # Set x ,y limits
    axes = plt.gca()
    axes.set_ylim(51.55, 53.08)
    axes.set_xlim(3.9, 5.45)

    # Set x, y label
    plt.xlabel("X")
    plt.ylabel("Y")

    # Set chart title
    plt.title("train Holland")

    # Read and show image
    img = plt.imread("NLkaartHolland.png")
    plt.imshow(img, aspect = "auto", extent = [3.9, 5.45, 51.55, 53.08])

    station_coordinates = []
    for station in stations_objects.stations.values():
        station_coordinates.append([station.y, station.x])
        plt.scatter(station.x, station.y, s = 5)

    for train in best_solution["trains"]:
        dict_coordinates = train.coordinates()
        x_list = dict_coordinates["x"]
        y_list = dict_coordinates["y"]
        plt.plot(x_list, y_list)
        plt.pause(1)

    plt.show()


def see_annealing(costs):
    plt.figure()
    plt.title("Evolution of scores of the simulated annealing")
    # plt.plot(122)
    plt.plot(costs, 'b')
    plt.show()
