def cut(solution):
    trajecten = solution["trajecten"]
    for traject_1 in trajecten:
        first_connection = traject_1.connections[0]
        last_connection = traject_1.connections[-1]
        
        for traject_2 in trajecten:
            if traject_1 is not traject_2 and traject_1.travel_time > 0 and traject_2.travel_time > 0:
                for connection in traject_2.connections:
                    if connection == first_connection:
                        traject_1.delete_connection(first_connection)
                        first_connection = traject_1.connections[0]
                        
                    elif connection == last_connection:
                        traject_1.delete_connection(last_connection)
                        last_connection = traject_1.connections[-1]
                
                    if traject_1.travel_time <= 0:
                        break


    return solution
