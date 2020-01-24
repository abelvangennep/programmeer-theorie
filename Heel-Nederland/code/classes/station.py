import random

class Station():
    """
    In this class station objects are created. These station objects contain
    the name of the station, the connections the station has and the x, y coordinates
    of the station.
    """
    def __init__(self, name, x, y):
        self.name = name
        self.connections = []
        self.x = x
        self.y = y

    def add_connection(self, connection):
        """Add a connection to the station"""
        self.connections.append(connection)

    def delete_connection(self, connection):
        """Deletes a connection of the station"""
        self.connections.remove(connection)

    def __str__(self):
        return f"{self.name}"
