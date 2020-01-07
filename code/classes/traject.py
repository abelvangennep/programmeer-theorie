from connection import Connection

class Traject():

    def __init__(self):
        self.connections = []
        self.travel_time = 0
        self.end = False

    def add_connection(self, connection):
        self.connections.append(connection)
        # self.travel_time += connection.travel_time

    def end_traject(self):
        self.end = True

    def __str__(self):
        return f"{self.connections}, {self.travel_time}, {self.end}"
