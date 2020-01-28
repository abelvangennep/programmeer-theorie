import csv
import random

from station import Station
from connection import Connection
from stations import Stations

def load_data(file, skip):
    """Load all data from a csv file and return the data in a list"""
    data_list = []

    # Read the csv file
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # If a station should be skipped (advanced), 
            # append only the other stations
            if skip:
                if row[0].lower() != skip.lower().rstrip() and row[1].lower() \
                    != skip.lower().rstrip():
                    data_list.append(row)
            else:
                data_list.append(row)

    return data_list

def load_stations(data_list, stations_data):
    """Create and return station objects"""
    # Create a stations object
    stations = Stations()

    # Create a station object for every station 
    # and append to the stations object
    for item in stations_data:
        station_object = Station(item[0], float(item[2]), float(item[1]))
        stations.append_station(item[0], station_object)

    return stations

def load_connections(data_list, stations_object, change_connections):
    """Load and return all connections"""
    connections = []

    for item in data_list:
        station_1 = stations_object.get_station(item[0])
        station_2 = stations_object.get_station(item[1])

        # Create a connection object and append the connection to the list
        connection = Connection(station_1, station_2, int(float(item[2])))
        connections.append(connection)

        # Add the connection to both station objects
        station_1.add_connection(connection)
        station_2.add_connection(connection)

    # If the user chose to change 3 connections randomly (advanced)
    if change_connections:
        
        change = 0
        nof_changes = 3
        for change in range(nof_changes):
            
            # Get a random connection and random station
            random_connection = random.choice(connections)
            random_station = stations_object.get_completely_random_station() 

            # If the random station is not part of the connection
            if random_station != random_connection.station_1 and \
                random_station != random_connection.station_2:

                # If changing the first station of the random connection into
                # the random station will result in a not existing connection
                for connection in random_station.connections: 
                    change = True
                    if connection.station_1 == random_station: 
                        # If this connection exists set change to false
                        if connection.station_2 == random_connection.station_2: 
                            change = False
                    else: 
                        
                        # If this connection exists set change to false 
                        if connection.station_1 == random_connection.station_2: 
                            change = False

                # Change the random connection and delete it from the changed
                # station and add it to the random station
                if change == True: 
                    random_connection.station_1 = random_station 
                    random_station.add_connection(random_connection)
                    random_connection.station_1.delete_connection(random_connection)

                    change += 1 

    return connections
