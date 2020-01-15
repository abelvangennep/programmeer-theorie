import random

class Traject():

    def __init__(self, start_station):
        self.start_station = start_station
        self.current_station = start_station
        self.connections = []
        self.travel_time = 0

    def get_random_connection(self, visited_stations, visit_city_once): 
        
        unvisited_connections = []
        unvisited_cities = []
        unvisited_connections_traject = []
        all_connections = []

        for connection in self.current_station.connections:

            if connection.visited == False:
                unvisited_connections.append(connection)

            if connection not in self.connections:
                unvisited_connections_traject.append(connection)
        
            all_connections.append(connection)

            if visit_city_once:
                if connection.station_1 not in visited_stations and connection.station_2 not in visited_stations:
                    unvisited_cities.append(connection)

        if len(unvisited_connections) > 0:
            return random.choice(unvisited_connections)

        if len(unvisited_cities) > 0:
            return random.choice(unvisited_cities)
               
        if len(unvisited_connections_traject) > 0:
            return random.choice(unvisited_connections_traject)

        return random.choice(all_connections)        


    def add_connection(self, connection):
        self.connections.append(connection)
        self.travel_time += connection.travel_time

        if self.current_station == connection.station_1:
            self.current_station = connection.station_2
        else:
            self.current_station = connection.station_1

    def delete_connection(self, connection):

        self.travel_time -= connection.travel_time

        if self.travel_time > 0:
            if self.connections.index(connection) == 0:
                if self.start_station == connection.station_1:
                    self.start_station = connection.station_2
                else:
                    self.start_station = connection.station_1
                
                self.connections.pop(0)
            else:
                if self.current_station == connection.station_1:
                    self.current_station = connection.station_2
                else:
                    self.current_station = connection.station_1
                
                self.connections.pop(-1)
            return False
        
        else: 
            return True

    def coordinates(self):
        coordinates = {}
        coordinates_x = []
        coordinates_y = []
        station = self.start_station
        
        for connection in self.connections:
            if connection.station_1 == station:
                coordinates_x.append(station.x)
                coordinates_y.append(station.y)
                station = connection.station_2
            else:
                coordinates_x.append(station.x)
                coordinates_y.append(station.y)
                station = connection.station_1
        
        coordinates["x"] = coordinates_x
        coordinates["y"] = coordinates_y

        return coordinates


    def __str__(self):
        station = self.start_station
        route = self.start_station
        for connection in self.connections:
            if connection.station_1 == station:
                station = connection.station_2
            else:
                station = connection.station_1
            route = f"{route} - {connection.travel_time} - {station}"
        return f"{route} ({self.travel_time})"

        # connecties = ""
        # for connection in self.connections:
        #     connecties += f" -{connection} "
        # return connecties
