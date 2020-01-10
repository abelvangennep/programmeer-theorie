from station import Station
import random

class Stations():

    def __init__(self):
        self.stations = {}

    def get_station(self, station_name): 
        return self.stations[station_name]
    

    def create_station(self, station_name):
        # print(type(Station(station_name)))
        if not station_name in self.stations: 
            self.stations[station_name] = Station(station_name) 
            
        

    def get_random(self):
        unvisited_connections = []
        for connections in self.stations.values():
            for connection in connections.connections:
                # print(connection.visited)
                if connection.visited == False:
                    unvisited_connections.append(connection.station_1)
                    unvisited_connections.append(connection.station_2)
                    # print(connection)
                    
                
        return random.choice(unvisited_connections)

    def __str__(self):
        stations = ""
        for station in self.stations:
            stations += station + "\n"
        return stations
