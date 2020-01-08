import csv

from station import Station
from connection import Connection
from stations import Stations

def loaddata(file):
    stations = Stations()

    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            station_1_name = row[0]
            station_2_name = row[1]
            travel_time = int(row[2])
            
            station_1 = stations.get_station(station_1_name)
            station_2 = stations.get_station(station_2_name)

            connection = Connection(station_1, station_2, travel_time) 
            station_1.add_connection(connection)
            station_2.add_connection(connection)

            # print(f"Added {station1} to {station2} : {duration}")
    return stations    

