def cut(solution): 
    trains = solution["trajecten"]

    for train in trains: 
        # While the train exists 
        while train.travel_time > 0: 

            first_connection = train.connections[0]
            last_connection = train.connections[-1]

            # Delete the first connection of the train, if it has been visited more than once
            if first_connection.visited > 1: 
                train.delete_connection(0)

            # Delete the last connection of the train, if it has been visited more than once
            elif last_connection.visited > 1: 
               train.delete_connection(-1)

            # If the first and last connection can't be deleted, break the while loop 
            else: 
                break 
    
    return solution