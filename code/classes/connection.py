class Connection():
    """

    """
    def __init__(self, destination_1, destination_2, travel_time):
        self.destination_1 = destination_1
        self.destination_2 = destination_2
        self.travel_time = travel_time
        self.visited = False

    def visited(self):
        pass

    def __str__(self):
        """Returns a string"""

        return f"{self.destination_1}, {self.destination_2}, {self.travel_time}"

