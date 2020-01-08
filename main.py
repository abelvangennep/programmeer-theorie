import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from connection import Connection
from station import Station
from loaddata import load_data, load_stations, load_connections
from traject import Traject

data_list = load_data("data/ConnectiesHolland.csv")

stations_objects = load_stations(data_list)

connection_objects = load_connections(data_list, stations_objects)

max = 120

trajecten = []
for i in range(7):
    station = stations_objects.get_random()
    traject = Traject(station) 
    # print(f"traject: {traject}")
    # print(f"traject_station: {traject.current_station}")
    while True:
        # print(f"currentstation:{traject.current_station}")
        connection = traject.current_station.get_random_connection()
        

        if traject.travel_time + connection.travel_time > max:
            break 

        traject.add_connection(connection)
        connection.set_visited()
        

    print(f"{traject}\n")
    trajecten.append(traject)
