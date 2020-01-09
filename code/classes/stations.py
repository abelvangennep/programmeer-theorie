from station import Station
import random

class Stations():
    """

    """

    def __init__(self):
        self.stations = {}

    def get_station(self, station_name):
        return self.stations[station_name]

    def create_station(self, station_name):
        if not station_name in self.stations:
            self.stations[station_name] = None
        # print(self.stations)

    def get_random(self):
        print(random.choice(list(self.stations.values())))
        return random.choice(list(self.stations.values()))

    def add_connection(self, station_name, connection):
        if self.stations[station_name] == None:
            self.stations[station_name] = []

        self.stations[station_name].append([connection])
        print(self.stations)


    def get_random_connection(self, station_name):
        unvisited_connections = []

        for connection in self.stations[station_name].values():
            if connection.visited == False:
                unvisited_connections.append(connection)

        if len(unvisited_connection) > 0:
            return random.choice(unvisited_connections)

        return random.choice(self.connections)

    def __str__(self):
        string = ""
        for key,values in self.stations.items():
            for value in values:
                string += value[0].station_1
        return string
