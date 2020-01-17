def calculate(solution):
    
    trains = solution["trajecten"]
    minutes = 0 
    visited_connections = []
    
    for train in trains: 
        minutes += train.travel_time

        for connection in train.connections: 
            if connection not in visited_connections: 
                visited_connections.append(connection)

    P = len(visited_connections) / solution["total_connections"]

    T = len(trains)

    score = P * 10000 - (T * 100 + minutes)

    return score 

