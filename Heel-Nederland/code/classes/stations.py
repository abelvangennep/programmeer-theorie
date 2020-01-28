from station import Station
import random


class Stations():
    """
    In this class station objects are added to a stations dictionary.
    """

    def __init__(self):
        self.stations = {}

    def get_station(self, station_name):
        """Return the station with given station name"""
        return self.stations[station_name]

    def append_station(self, name, station_object):
        """Add a station to the stations dictionary"""
        self.stations[name] = station_object

    def get_random_station(self, uneven_connection, one_connection):
        """Return a random station, possibly with heuristics"""
        stations_with_1_connection = []
        stations_uneven_connections = []
        unvisited_connections = []

        for station in self.stations.values():
            # If the heuristic of starting a train with only one connection
            # was chosen
            if one_connection:
                # Append the station if it only has one connection and no visit
                if len(station.connections) == 1 and\
                    station.connections[0].visited == 0:
                    stations_with_1_connection.append(station)

            for connection in station.connections:
                # If the heuristic of starting a train with an uneven amount of
                # connections was chosen
                if uneven_connection:
                    # Append the station if it has an uneven number of connections
                    # and no visits
                    if len(station.connections) % 2 == 1 and connection.visited \
                        < 1 and station not in stations_uneven_connections:
                        stations_uneven_connections.append(station)

                # Append every unvisited station
                if connection.visited < 1 and station not in unvisited_connections:
                    unvisited_connections.append(station)

        # Return if there's a station with one connection
        if len(stations_with_1_connection) > 0:
            return random.choice(stations_with_1_connection)

        # Return if there's a station with an uneven amount of connections
        elif len(stations_uneven_connections) > 0:
            return random.choice(stations_uneven_connections)

        # Return if there are unvisited stations
        elif len(unvisited_connections) > 0:
            return random.choice(unvisited_connections)

        # Return a completely random station, if all the other lists are empty
        return self.get_completely_random_station()

    def get_completely_random_station(self):
        """Return a completely random station"""
        all_stations = []

        # Add all stations to list
        for station in self.stations.values():
            if station not in all_stations:
                all_stations.append(station)

        return random.choice(all_stations)

    def __str__(self):
        stations = ""
        for station in self.stations:
            stations += station + "  "

        return stations
