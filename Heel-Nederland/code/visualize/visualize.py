from __future__ import print_function

import os
import subprocess
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Draw points based on x, y values
def draw_traject(best_solution, stations_objects):

    axes = plt.gca()
    axes.set_ylim(50.7, 53.7)
    axes.set_xlim(3.25, 7.3)

        # Read image
    img = plt.imread("NLkaart.png")

    plt.imshow(img, aspect = "auto", extent = [3.25, 7.3, 50.65, 53.7])

    station_coordinates = []
    for station in stations_objects.stations.values():
        station_coordinates.append([station.y, station.x])

    # kan dit in een keer met hierboven
    for coordinate in station_coordinates:
        y = coordinate[0]
        x = coordinate[1]
        plt.scatter(x, y, s = 5)

    for traject in best_solution["trajecten"]:
        dict_coordinates = traject.coordinates()
        x_list = dict_coordinates["x"]
        y_list = dict_coordinates["y"]
        plt.pause(0.5)
        # for i in range(len(x_list)):
        plt.plot(x_list, y_list)
        plt.pause(0.5)

    # station_coordinates = []
    # for station in stations_objects.stations.values():
    #     station_coordinates.append([station.y, station.x])
    #
    # # kan dit in een keer met hierboven
    # for coordinate in station_coordinates:
    #     y = coordinate[0]
    #     x = coordinate[1]
    #     plt.scatter(x, y, s = 5)

    # Set x, y label
    plt.xlabel("X")
    plt.ylabel("Y")

    # Set chart title
    plt.title("Traject")

    #     # Read image
    # img = plt.imread("NLkaart.png")
    #
    # plt.imshow(img, aspect = "auto", extent = [3.25, 7.3, 50.65, 53.7])

    plt.show()

def draw_traject_holland(best_solution, stations_objects):
        axes = plt.gca()
        axes.set_ylim(51.55, 53.08)
        axes.set_xlim(3.9, 5.45)

            # Read image
        img = plt.imread("NLkaartHolland.png")

        plt.imshow(img, aspect = "auto", extent = [3.9, 5.45, 51.55, 53.08])

        station_coordinates = []
        for station in stations_objects.stations.values():
            station_coordinates.append([station.y, station.x])

        # kan dit in een keer met hierboven
        for coordinate in station_coordinates:
            y = coordinate[0]
            x = coordinate[1]
            plt.scatter(x, y, s = 5)

        for traject in best_solution["trajecten"]:
            dict_coordinates = traject.coordinates()
            x_list = dict_coordinates["x"]
            y_list = dict_coordinates["y"]
            plt.pause(0.5)
            plt.plot(x_list, y_list)
            plt.pause(0.5)

        # Set x, y label
        plt.xlabel("X")
        plt.ylabel("Y")

        # Set chart title
        plt.title("Traject Holland")

        plt.show()
