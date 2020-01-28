def get_random_connection_1(self, visited_stations): 
        
    all_connections = []
    unvisited_connections = []
    for station in visited_stations:
        print(f"visited_stations{station}")

    for connection in self.connections:
        print(connection)
        if connection.station_1 not in visited_stations and connection.station_2 not in visited_stations:
            print("1")
            all_connections.append(connection)
            print(all_connections)
            if connection.visited == False:
                unvisited_connections.append(connection)  

    if len(unvisited_connections) > 0:
        return random.choice(unvisited_connections)   

    if len(all_connections) > 0:
        return random.choice(all_connections)  

    def __str__(self):
        return f"{self.name}"