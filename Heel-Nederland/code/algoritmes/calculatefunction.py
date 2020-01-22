def calculate(solution):
    
    trains = solution["trains"]
    minutes = 0 
    visited_connections = []
    
    for train in trains: 
        minutes += train.travel_time

        for connection in train.connections: 
            if connection not in visited_connections: 
                visited_connections.append(connection)
                # print(connection)


    # print("len(visited_connections)", len(visited_connections))
    P = len(visited_connections) / solution["total_connections"]

    T = len(trains)

    # print("P:", P)
    # print("T", T)
    # print("minutes", minutes)
    score = P * 10000 - (T * 100 + minutes)

    return score 