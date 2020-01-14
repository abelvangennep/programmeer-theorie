class Traject():

    def __init__(self, start_station):
        self.start_station = start_station
        self.current_station = start_station
        self.connections = []
        self.travel_time = 0

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
                # self.start_station = self.connections[1]
                self.connections.remove(self.connections[0])
            else:
                if self.current_station == connection.station_1:
                    self.current_station = connection.station_2
                else:
                    self.current_station = connection.station_1
                # self.start_station = self.connections[-2]
                self.connections.remove(self.connections[-1])


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
