import random

class Station():
    """

    """
    def __init__(self, name):
        self.name = name
        self.connections = []
        # self.unvisited_connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    # def get_random_connection(self): 
        
    #     unvisited_connections = []

    #     for connection in self.connections:
            
    #         if connection.visited == False:
    #             unvisited_connections.append(connection)

    #     if len(unvisited_connections) > 0:
            
    #         return random.choice(unvisited_connections)

    #     return random.choice(self.connections)

    # def get_random_connection_1(self, visited_stations): 
        
    #     unvisited_connections = []
    #     unvisited_cities = []

    #     for connection in self.connections:
            
    #         if connection.visited == False:
    #             if connection.station_1 not in visited_stations and connection.station_2 not in visited_stations:
    #                 unvisited_cities.append(connection)
    #             unvisited_connections.append(connection)

    #     if len(unvisited_cities) > 0:
    #         return random.choice(unvisited_cities)

    #     if len(unvisited_connections) > 0:
    #         return random.choice(unvisited_connections)

    #     return random.choice(self.connections)        

    def __str__(self):
        return f"{self.name}"