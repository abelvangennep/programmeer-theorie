import random


class Traject():

    def __init__(self, start_station):
        self.start_station = start_station
        self.current_station = start_station
        self.connections = []
        self.travel_time = 0

    def get_random_connection(self, visited_stations, visit_city_once):
        """Return a random connection"""
        unvisited_connections = []
        unvisited_cities = []
        unvisited_connections_traject = []
        all_connections = []

        # Loop over all of the current station's connections
        for connection in self.current_station.connections:

            # Add the connection to the list of unvisited connections, if its visit count is lower than 1
            if connection.visited < 1:
                unvisited_connections.append(connection)

            # Add the connection to the list of unvisited connections in this train, if it is not in self.connections
            if connection not in self.connections:
                unvisited_connections_traject.append(connection)

            # Add every connection to the list of all connections
            all_connections.append(connection)

            # If a station should only be visited once per train
            if visit_city_once:
                # ???
                if connection.station_1 not in visited_stations or connection.station_2 not in visited_stations:
                    unvisited_cities.append(connection)

        # Return a random unvisited connection, if there is any
        if unvisited_connections:
            return random.choice(unvisited_connections)

        # Return a random connection leading to a new city, if there is any 
        if unvisited_cities:
            return random.choice(unvisited_cities)

        # Return a random in this train unvisited connection, if there is any 
        if unvisited_connections_traject:
            return random.choice(unvisited_connections_traject)

        # Return a random connection, if all of the other lists are empty 
        return random.choice(all_connections)

    def add_connection(self, connection):
        """Add a connection to the train"""
        self.connections.append(connection)
        self.travel_time += connection.travel_time

        if self.current_station == connection.station_1:
            self.current_station = connection.station_2
        else:
            self.current_station = connection.station_1

        connection.add_visit()

    def delete_connection(self, index):
        """Delete a connection from the train"""
        #
        connection = self.connections[index]

        # Update the train's travel time
        self.travel_time -= connection.travel_time

        # If the connection is not the last connection of the train
        if self.travel_time > 0:
            # If the connection is the start of the train
            if index == 0:
                if self.start_station == connection.station_1:
                    self.start_station = connection.station_2
                else:
                    self.start_station = connection.station_1

            # Else if the connection is the end of the train
            elif index == -1:
                if self.current_station == connection.station_1:
                    self.current_station = connection.station_2
                else:
                    self.current_station = connection.station_1

            self.connections.pop(index)

            connection.delete_visit()

        # Empty the train, if the connection is the last connection
        else:
            self.empty_traject()

    def empty_traject(self):
        """Empty the train object by deleting all variables"""
        for connection in self.connections:
            connection.delete_visit()

        self.travel_time = 0
        self.connections = []
        self.start_station = ""
        self.current_station = ""

    def coordinates(self):
        """ """ 
        coordinates = {}
        coordinates_x = []
        coordinates_y = []
        station = self.start_station

        coordinates_x.append(station.x)
        coordinates_y.append(station.y)

        for connection in self.connections:
            if connection.station_1 == station:
                station = connection.station_2
                coordinates_x.append(station.x)
                coordinates_y.append(station.y)
            else:
                station = connection.station_1
                coordinates_x.append(station.x)
                coordinates_y.append(station.y)

        coordinates["x"] = coordinates_x
        coordinates["y"] = coordinates_y

        return coordinates

    def __str__(self):
        station = self.start_station
        route = self.start_station
        if not self.connections and self.travel_time == 0 and self.start_station == "":
            string = "*deleted*"
        else:
            for connection in self.connections:
                if connection.station_1 == station:
                    station = connection.station_2
                else:
                    station = connection.station_1
                route = f"{route} - {connection.travel_time} - {station}"
            string = f"{route} ({self.travel_time})"
        return string

