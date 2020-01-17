class Connection():
    """

    """
    def __init__(self, station_1, station_2, travel_time):
        self.station_1 = station_1
        self.station_2 = station_2
        self.travel_time = travel_time
        # self.visited = False
        self.visited = 0 

    def add_visit(self):
        # self.visited = True
        self.visited += 1 

    def delete_visit(self): 
        self.visited -= 1 

    def __str__(self):
        """Returns a string"""
        return f"{self.station_1}, {self.station_2}, {self.travel_time}, {self.visited}"

