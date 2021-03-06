import random


class Train():
    """
    In this class train objects are stored. These train objects contain all
    connections of one train, the start/end station and the travel time.
    """

    def __init__(self, start_station):
        self.start_station = start_station
        self.current_station = start_station
        self.connections = []
        self.travel_time = 0

    def set_start_station(self, station):
        """Set the start station and current station"""
        self.start_station = station
        self.current_station = station

    def get_random_connection(self, visited_stations, visit_station_once):
        """Return a random connection"""
        unvisited_connections = []
        unvisited_stations = []
        unvisited_connections_train = []
        all_connections = []

        # Seperate all connections in the lists
        for connection in self.current_station.connections:
            # If connection is unvisited
            if connection.visited < 1:
                unvisited_connections.append(connection)

                # If the heuristic of visiting every station only once per 
                # train was chosen
                if visit_station_once:
                    if connection.station_1 not in visited_stations or \
                        connection.station_2 not in visited_stations:
                        unvisited_stations.append(connection)

            # If connection is not in the current train
            if connection not in self.connections:
                unvisited_connections_train.append(connection)

            all_connections.append(connection)

        # Return a random connection with unvisited stations
        if unvisited_stations:
            return random.choice(unvisited_stations)

        # Return a random unvisited connection
        elif unvisited_connections:
            return random.choice(unvisited_connections)

        # Return a random connection which is not visited in current train
        elif unvisited_connections_train:
            return random.choice(unvisited_connections_train)

        # Return a completely random connection if all the other lists are empty
        return random.choice(all_connections)

    def add_connection(self, connection):
        """Add a connection to the train"""
        self.connections.append(connection)

        # Update the train's travel time
        self.travel_time += connection.travel_time

        # Set new current station
        if self.current_station == connection.station_1:
            self.current_station = connection.station_2
        else:
            self.current_station = connection.station_1

        connection.add_visit()

    def delete_connection(self, index):
        """Delete a connection from the train"""
        connection = self.connections[index]

        # Update the train's travel time
        self.travel_time -= connection.travel_time

        # If the connection is not the last connection of the train
        if self.travel_time > 0:
            # Set new current station if the connection is the first
            if index == 0:
                if self.start_station == connection.station_1:
                    self.start_station = connection.station_2
                else:
                    self.start_station = connection.station_1

            # Set new current station if the connection is the last
            elif index == -1:
                if self.current_station == connection.station_1:
                    self.current_station = connection.station_2
                else:
                    self.current_station = connection.station_1

            connection.delete_visit()
            self.connections.pop(index)

        # Empty the train if the connection is the last connection
        else:
            self.empty_train()

    def empty_train(self):
        """Empty the train object by deleting all variables"""
        for connection in self.connections:
            connection.delete_visit()

        self.travel_time = 0
        self.connections = []
        self.start_station = ""
        self.current_station = ""

    def coordinates(self):
        """Save all coordinates of the train stations that are visited"""
        coordinates = {}
        coordinates_x = []
        coordinates_y = []
        station = self.start_station

        coordinates_x.append(station.x)
        coordinates_y.append(station.y)

        for connection in self.connections:
            # Check if station is the first or second station, change station
            # and add coordinates coordinates
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
        train_stations_list = []
        train_stations_list.append(station.name)

        for connection in self.connections:
            if connection.station_1 == station:
                train_stations_list.append(connection.station_2.name)
                station = connection.station_2
            else:
                train_stations_list.append(connection.station_1.name)
                station = connection.station_1

        return f"{train_stations_list}"
