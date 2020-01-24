import csv
import random

from station import Station
from connection import Connection
from stations import Stations

def load_data(file, skip):
    """"""
    data_list = []
    skip_count = 0
    
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if skip:
                if row[0].lower() != skip.lower().rstrip() and row[1].lower() != skip.lower().rstrip():
                    data_list.append(row)
                else:
                    skip_count += 1
            else:
                data_list.append(row)

    if skip and skip_count == 0:
        return False

    return data_list

def load_stations(data_list, stations_data):
    """"""
    stations = Stations()
    for item in data_list:
        stations.create_station(item[0], stations_data)
        stations.create_station(item[1], stations_data)

    return stations

def load_connections(data_list, stations_object, change_connections):
    """Add connections to station objects(??)"""
    connections = []

    for item in data_list:
        station_1 = stations_object.get_station(item[0])
        station_2 = stations_object.get_station(item[1])

        connection = Connection(station_1, station_2, int(float(item[2])))
        connections.append(connection)

        station_1.add_connection(connection)
        station_2.add_connection(connection)


    if change_connections:
        i = 0
        for i in range(3):
            i += 1
            random_connection = random.choice(connections)

            uneven_connection = False
            one_connection = False
            random_station = stations_object.get_random_start_station(uneven_connection, one_connection)

            # If the random station is not part of the connection
            if random_station is not random_connection.station_1 and random_station is not random_connection.station_2:

                # Random station from the 2 stations in connection
                change_station = random.choice([random_connection.station_1, random_connection.station_2])

                # Delete this connection from the station
                if change_station == random_connection.station_1:
                    random_connection.station_1 = random_station
                # IS DEZE ELSE NODIG??????????
                else:
                    random_connection.station_2 = random_station
                # Add connection to the random station
                random_station.add_connection(random_connection)

                # Replace it with complete random station
                change_station.delete_connection(random_connection)
    return connections
