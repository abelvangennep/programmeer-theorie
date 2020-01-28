class Connection():
    """

    """
    def __init__(self, station_1, station_2, travel_time):
        self.station_1 = station_1
        self.station_2 = station_2
        self.travel_time = travel_time
        self.visited = False

    def set_visited(self):
        self.visited = True

    def __str__(self):
        """Returns a string"""
        return f"{self.station_1}, {self.station_2}, {self.travel_time}, {self.visited}"

