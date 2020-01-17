def cut(solution): 
    trajecten = solution["trajecten"]

    for traject in trajecten: 
        while traject.travel_time > 0: 

            first_connection = traject.connections[0]
            last_connection = traject.connections[-1]

            if first_connection.visited > 1: 
                traject.delete_connection(0)
                # if first_connection.visited < 1: 
                #     print("first connection", first_connection)

            elif last_connection.visited > 1: 
                traject.delete_connection(-1)
                # if first_connection.visited < 1: 
                    # print("last connection", last_connection)

            else: 
                break 
    
    return solution