class Connection():
    """
    In this class connection objects are created. These connection objects contain
    the first and second station, the travel time of the connection and the count
    of how many times the connection is visited.
    """

    def __init__(self, station_1, station_2, travel_time):
        self.station_1 = station_1
        self.station_2 = station_2
        self.travel_time = travel_time
        self.visited = 0

    def __eq__(self, other):
        """Compare just the two station names"""
        if self.station_1.name == other.station_1.name and self.station_2.name == other.station_2.name:
            return True
        return False

    def add_visit(self):
        """Add a visit to the connection"""
        self.visited += 1

    def delete_visit(self):
        """Delete a visit from the connection"""
        self.visited -= 1

    def __str__(self):
        """Return a string"""
        return f"{self.station_1}, {self.station_2}, {self.travel_time}, {self.visited}"
