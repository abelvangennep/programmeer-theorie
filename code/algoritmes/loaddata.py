import csv

from station import Station
from connection import Connection
from stations import Stations

def load_data(file):
    data_list = []

    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data_list.append(row)

    return data_list

def load_stations(data_list):
    stations = Stations()
    for item in data_list:
        stations.create_station(item[0])
        stations.create_station(item[1])

    return stations

def load_connections(data_list, stations_dict):
    connections = []

    for item in data_list:
        # station_1 = stations_dict.get_station(item[0])
        # print(station_1)
        # station_2 = stations_dict.get_station(item[1])

        connection = Connection(item[0], item[1], int(item[2]))
        connections.append(connection)
        stations_dict.add_connection(item[0], connection)
        # print(connection)
        stations_dict.add_connection(item[1], connection)


    return connections
