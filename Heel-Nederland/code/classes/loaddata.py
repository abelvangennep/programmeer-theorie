import csv

from station import Station
from connection import Connection
from stations import Stations

def load_data(file, skip):
    data_list = []

    skip_count = 0 
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if skip:
                if row[0].lower() != skip.lower() and row[1].lower() != skip.lower():
                    data_list.append(row)
                else: 
                    skip_count += 1 
            else:
                data_list.append(row)
    
    if skip and skip_count == 0: 
        return False 

    return data_list

def load_stations(data_list, stations_data):
    stations = Stations()
    for item in data_list:
        stations.create_station(item[0], stations_data)
        stations.create_station(item[1], stations_data)

    return stations

def load_connections(data_list, stations_object):
    connections = []

    for item in data_list:
        station_1 = stations_object.get_station(item[0])
        station_2 = stations_object.get_station(item[1])

        connection = Connection(station_1, station_2, int(float(item[2])))
        connections.append(connection)
        station_1.add_connection(connection)
        station_2.add_connection(connection)


    return connections

# def change_connections(stations_object):

    
#     random_station = stations_object.get_complete_random_start_station()
#     random_connection = random_station.get_random_connection() 
#     print(random_connection)
    


