from station import Station
import random

class Stations():

    def __init__(self):
        self.stations = {}

    def get_station(self, station_name): 
        return self.stations[station_name]
    

    def create_station(self, station_name):
        if not station_name in self.stations: 
            self.stations[station_name] = Station(station_name) 
        

    def get_random(self):
        print(f"{random.choice(list(self.stations.values()))}")
        return random.choice(list(self.stations.values()))

    def __str__(self):
        stations = ""
        for station in self.stations:
            stations += station + "\n"
        return stations
