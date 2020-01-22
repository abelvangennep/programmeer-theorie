from station import Station
import random

class Stations():
    """ 
    """
    def __init__(self):
        self.stations = {}

    def get_station(self, station_name):
        """Return the station with the given station name""" 
        return self.stations[station_name]

    def create_station(self, station_name, stations_data):
        """Create a new station"""
        if not station_name in self.stations:
            for item in stations_data:
                if station_name == item[0]:
                    y = float(item[1])
                    x = float(item[2])
            self.stations[station_name] = Station(station_name, x, y)

    def get_random_start_station(self, uneven_connection, one_connection):
        """Return a random start station"""
        stations_with_1_connection = []
        stations_uneven_connections = []
        unvisited_connections = []
        
        for station in self.stations.values():
            if one_connection:
                if len(station.connections) == 1 and station.connections[0].visited == False:
                    stations_with_1_connection.append(station)
            
            for connection in station.connections:
                if uneven_connection:
                    if connection.visited < 1 and station not in stations_uneven_connections and len(station.connections) % 2 == 1:
                        stations_uneven_connections.append(station)

                if connection.visited < 1 and station not in unvisited_connections: 
                        unvisited_connections.append(station)

        if len(stations_with_1_connection) > 0:
            return random.choice(stations_with_1_connection)
        
        elif len(stations_uneven_connections) > 0:
            return random.choice(stations_uneven_connections)
        return random.choice(unvisited_connections)

    def get_complete_random_start_station(self):
        all_stations = []

        for station in self.stations.values():
            if station not in all_stations:
                all_stations.append(station)
        
        return random.choice(all_stations)

    def __str__(self):
        stations = ""
        for station in self.stations:
            stations += station + "\n"
        return stations
