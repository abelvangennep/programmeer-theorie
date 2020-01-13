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

    def get_random_station(self):
        unvisited_connections = []
        # stations_with_1_connection = []
        # stations_uneven_connections = []
        # for station in self.stations.values():
        #     if len(station.connections) == 1 and station.connections[0].visited == False:
        #         stations_with_1_connection.append(station)
                # stations_with_1_connection.append(station.connections[0].station_2)

        for connection in station.connections:
            if connection.visited == False:
                if connection.station_1 not in unvisited_connections:
                    unvisited_connections.append(connection.station_1)
                if connection.station_2 not in unvisited_connections:
                    unvisited_connections.append(connection.station_2)
        return random.choice(unvisited_connections)

    def get_random_station_1_conn(self, uneven):
        stations_with_1_connection = []
        for station in self.stations.values():
            if len(station.connections) == 1 and station.connections[0].visited == False:
                stations_with_1_connection.append(station)
        if len(stations_with_1_connection) > 0:
            return random.choice(stations_with_1_connection)
        elif uneven:
            get_random_station_uneven_conn()
        get_random_station()

    def get_random_station_uneven_conn(self):
        stations_uneven_connections = []
        for station in self.stations.values():
            if len(station.connections) % 2 == 1:
                for connection in station.connections:
                    if connection.visited == False and station not in stations_uneven_connections:
                        stations_uneven_connections.append(station)
        if  len(stations_uneven_connections) > 0:
            return random.choice(stations_uneven_connections)
        get_random_station()

    def get_random_station_original(self):
        unvisited_connections = []

        for connections in self.stations.values():
            for connection in connections.connections:
                if connection.visited == False:
                    unvisited_connections.append(connection.station_1)
                    unvisited_connections.append(connection.station_2)

        return random.choice(unvisited_connections)

    def __str__(self):
        stations = ""
        for station in self.stations:
            stations += station + "\n"
        return stations
