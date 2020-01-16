import matplotlib.pyplot as plt

# Draw points based on x, y values
def draw_traject(best_solution, stations_objects):
    axes = plt.gca()
    axes.set_ylim(50.7, 53.7)
    axes.set_xlim(3.25, 7.3)
    # dict_coordinates = {}
    for traject in best_solution["trajecten"]:
        dict_coordinates = traject.coordinates()
        x_list = dict_coordinates["x"]
        y_list = dict_coordinates["y"]

    # print(x_list, y_list)
        plt.plot(x_list, y_list)

    station_coordinates = []
    for station in stations_objects.stations.values():
        station_coordinates.append([station.y, station.x])
    print(station_coordinates)


    # kan dit in een keer met hierboven
    for coordinate in station_coordinates:
        y = coordinate[0]
        x = coordinate[1]
        plt.scatter(x, y, s = 5)



    # x = 4.761111259
    # y = 52.95527649

    # plt.scatter(x, y, s = 5)

# stations = [[52.95527649, 4.761111259], [52.37888718, 4.900277615], [51.98500061, 5.705555439]]
# # x_list = []
# # y_list = []
# for station in stations:
#     y = station[0]
#     y_list.append(y)
#
#     x = station[1]
#     x_list.append(x)
#     plt.scatter(x, y, s = 5)
    # plt.plot(x_list, y_list, 'r')

    # Set x, y label
    plt.xlabel("X")
    plt.ylabel("Y")

    # Set chart title
    plt.title("Traject")

        # Read image
    img = plt.imread("NLkaart.png")

    plt.imshow(img, aspect = "auto", extent = [3.25, 7.3, 50.65, 53.7])

        # Plot
        # ax.imshow(img)
    plt.show()
