from station import Station
import random

class Stations():
    """
    In this class station objects are added to a stations dictionary.
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
        """Return a random start station, possible with heuristics"""
        stations_with_1_connection = []
        stations_uneven_connections = []
        unvisited_connections = []
        all_stations = []

        for station in self.stations.values():
            # If station with one connection
            if one_connection:
                # If one connection and unvisited append
                if len(station.connections) == 1 and station.connections[0].visited == 0:
                    stations_with_1_connection.append(station)

            for connection in station.connections:
                # If station with uneven amount of connections
                if uneven_connection:
                    if len(station.connections) % 2 == 1 and connection.visited < 1 and station not in stations_uneven_connections:
                    # HEB VAN DE IF STATEMENT HIERONDER DE VOLGORDE VERANDERD NAAR HIERBOVEN
                    # if connection.visited < 1 and station not in stations_uneven_connections and len(station.connections) % 2 == 1:
                        stations_uneven_connections.append(station)

                if connection.visited < 1 and station not in unvisited_connections:
                    unvisited_connections.append(station)

            if station not in all_stations:
                all_stations.append(station)

        if len(stations_with_1_connection) > 0:
            return random.choice(stations_with_1_connection)

        elif len(stations_uneven_connections) > 0:
            return random.choice(stations_uneven_connections)

        elif len(unvisited_connections) > 0:
            return random.choice(unvisited_connections)

        return random.choice(all_stations)

    def get_complete_random_start_station(self):
        """Returns a complete random start station"""
        all_stations = []

        # Add all stations once to list
        for station in self.stations.values():
            if station not in all_stations:
                all_stations.append(station)
        return random.choice(all_stations)

    def __str__(self):
        stations = ""
        for station in self.stations:
            stations += station + "   "
        return stations
