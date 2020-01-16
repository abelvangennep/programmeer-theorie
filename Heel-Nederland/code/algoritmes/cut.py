def cut(solution): 
    trajecten = solution["trajecten"]

    for traject in trajecten: 
        while traject.travel_time > 0: 

            first_connection = traject.connections[0]
            last_connection = traject.connections[-1]

            if first_connection.visited > 1: 
                traject.delete_connection(0)

            elif last_connection.visited > 1: 
                traject.delete_connection(-1)
            
            else: 
                break 
    
    return solution