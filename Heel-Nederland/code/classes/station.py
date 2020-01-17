import random

class Station():
    """

    """
    def __init__(self, name, x, y):
        self.name = name
        self.connections = []
        self.x = x
        self.y = y

    def add_connection(self, connection):
        """Add a connection to the station"""
        self.connections.append(connection)

    def __str__(self):
        return f"{self.name}"