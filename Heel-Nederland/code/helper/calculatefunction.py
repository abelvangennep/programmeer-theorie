def calculate(solution):
    """Returns the score of the solution"""

    trains = solution["trains"]
    minutes = 0
    visited_connections = []

    for train in trains:

        # Update travel time
        minutes += train.travel_time

        # Add connection to list if visited
        for connection in train.connections:
            if connection not in visited_connections:
                visited_connections.append(connection)

    # Calculate variables and score
    P = len(visited_connections) / solution["total_connections"]
    T = len(trains)
    score = P * 10000 - (T * 100 + minutes)

    return score
