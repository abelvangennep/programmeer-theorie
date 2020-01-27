def cut(solution):
    """Cuts unnessecary connections that are already visited in another train"""
    trains = solution["trains"]

    # Delete first/last connections
    for train in trains:
        # While the train exists
        while train.travel_time > 0:
            first_connection = train.connections[0]
            last_connection = train.connections[-1]

            # Delete the first connection of the train, if it has been visited
            # more than once
            if first_connection.visited > 1:
                train.delete_connection(0)

            # Delete the last connection of the train, if it has been visited
            # more than once
            elif last_connection.visited > 1:
                train.delete_connection(-1)

            # Break if the last connection can't be deleted
            else:
                break

    # Delete other possible connections
    for train in trains:
        # If the train exists
        if train.travel_time > 0:
            counter = 0

            # Keep iterating over the connections of this train, while connections
            # are being deleted
            while counter <= len(train.connections):
                index = -1
                counter = 1

                for connection in train.connections:
                    index += 1

                    # If the connection at index is not the last connection
                    if index < len(train.connections) - 1:

                        # If the connection is the same as the next connection
                        # and has been visited more than twice
                        if connection == train.connections[index + 1] and \
                        connection.visited > 2:

                            # Delete both connections
                            train.delete_connection(index)
                            train.delete_connection(index)
                            index -= 1
                            break

                    counter += 1

    return solution
