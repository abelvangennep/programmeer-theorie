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
            
    def get_random_station(self):        
        unvisited_connections = []
        stations_with_1_connection = [] 
        for station in self.stations.values():
            # print(station.connections)
            if len(station.connections) == 1 and station.connections[0].visited == False:
                stations_with_1_connection.append(station)
                # stations_with_1_connection.append(station.connections[0].station_2)

            for connection in station.connections:
                # print(connection.visited)
                if connection.visited == False:
                    unvisited_connections.append(connection.station_1)
                    unvisited_connections.append(connection.station_2)
                    # print(connection)
        if len(stations_with_1_connection) > 0: 
            return random.choice(stations_with_1_connection)          
        return random.choice(unvisited_connections)

    def get_random_station_2(self):        
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

