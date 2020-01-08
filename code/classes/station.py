import random

class Station():
    """

    """
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    def get_random_connection(self): 
        return random.choice(self.connections)

    def __str__(self):
        return self.name