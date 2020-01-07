from connection import Connection

class Traject(): 

    def __init__(self): 
        self.connections = [] 
        self.travel_time = 0

    def add_connection(self, connection): 
        self.connections.append(connection)
        self.travel_time += connection.travel_time

    def end_traject(self): 
        pass

    def __str__(self): 
        pass