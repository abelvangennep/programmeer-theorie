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

    for train in trains:
        if train.travel_time > 0: 
            index = -1 
            counter = 0
            while counter <= len(train.connections): 
                index = -1 
                counter = 1
                for connection in train.connections: 
                    index += 1 
                    if index < len(train.connections) - 1:
                        if connection == train.connections[index + 1] and connection.visited > 2: 
                            train.delete_connection(index)
                            train.delete_connection(index)
                            index -= 1 
                            break 
                        else:
                            counter += 1
                    else: 
                        counter += 1

    return solution