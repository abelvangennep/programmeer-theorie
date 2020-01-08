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

    def get_random_connection(self): 
        unvisited_connections = []

        for connection in self.connections:
            if connection.visited == False:
                unvisited_connections.append(connection)

        if len(unvisited_connections) > 0:
            return random.choice(unvisited_connections)

        return random.choice(self.connections)

    def __str__(self):
        return self.name