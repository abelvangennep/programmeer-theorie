import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from connection import Connection
from station import Station
from loaddata import loaddata
from traject import Traject

stations = loaddata("data/ConnectiesHolland.csv")

max = 120

trajecten = []
for i in range(7):
    station = stations.get_random()

    traject = Traject(station)
    while True:
        connection = traject.current_station.get_random_connection()
        if traject.travel_time + connection.travel_time > max:
            break
        traject.add_connection(connection)

    print(f"{traject}\n")
    trajecten.append(traject)
