from __future__ import print_function

import os
import subprocess
import matplotlib.pyplot as plt


def draw_train(best_solution, stations_objects):
    """Draw every train of the solution of the Netherlands part"""

    # List of colors for the visualization
    colors = ['goldenrod', 'indianred', 'olive', 'sandybrown', 'skyblue',
              'orchid', 'gold', 'sienna', 'khaki', 'lightpink', 'slateblue',
              'moccasin', 'yellowgreen', 'coral', 'lightsteelblue', 'indigo',
              'seagreen', 'slategray', 'salmon', 'thistle']

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
    img = plt.imread("pictures/NLkaart.png")
    plt.imshow(img, aspect="auto", extent=[3.25, 7.3, 50.65, 53.7])

    station_coordinates = []

    # Draw points on the x, y coordinates of the stations
    for station in stations_objects.stations.values():
        station_coordinates.append([station.y, station.x])
        plt.scatter(station.x, station.y, s=5)

    color_count = -1

    # Draw every train route of the solution
    for train in best_solution["trains"]:
        color_count += 1
        dict_coordinates = train.coordinates()
        x_list = dict_coordinates["x"]
        y_list = dict_coordinates["y"]
        plt.plot(x_list, y_list, color=colors[color_count])
        plt.pause(1)

    plt.show()

def draw_train_holland(best_solution, stations_objects):
    """Draw every train of the solution of the North-/South-Holland part"""

    # List of colors for the visualization
    colors = ['goldenrod', 'indianred', 'olive', 'sandybrown', 'skyblue',
              'orchid', 'gold']

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
    img = plt.imread("pictures/NLkaartHolland.png")
    plt.imshow(img, aspect="auto", extent=[3.9, 5.45, 51.55, 53.08])

    station_coordinates = []

    # Draw points on the x, y coordinates of the stations
    for station in stations_objects.stations.values():
        station_coordinates.append([station.y, station.x])
        plt.scatter(station.x, station.y, s=5)

    color_count = -1

    # Draw every train route of the solution
    for train in best_solution["trains"]:
        color_count += 1
        dict_coordinates = train.coordinates()
        x_list = dict_coordinates["x"]
        y_list = dict_coordinates["y"]
        plt.plot(x_list, y_list, color=colors[color_count])
        plt.pause(1)

    plt.show()

def see_annealing(costs):
    """Plot simulated annealing line"""
    plt.figure()

    # Set chart title
    plt.title("Evolution of scores of the simulated annealing")

    # Plot line scores
    plt.plot(costs, 'b')

    plt.show()
