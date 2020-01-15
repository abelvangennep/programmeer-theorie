def cut(solution):
    trajecten = solution["trajecten"]
    # print(trajecten)
    for traject_1 in trajecten:
        first_connection = traject_1.connections[0]
        last_connection = traject_1.connections[-1]
        
        for traject_2 in trajecten:
            if traject_1 is not traject_2 and traject_1.travel_time > 0 and traject_2.travel_time > 0:
                
                for connection in traject_2.connections:
                    if connection == first_connection:
                        traject_1.delete_connection(first_connection, 1)
                        first_connection = traject_1.connections[0]
                        
                    elif connection == last_connection:
                        traject_1.delete_connection(last_connection, -1)
                        last_connection = traject_1.connections[-1]
                
                    if traject_1.travel_time <= 0:
                        break

            elif traject_1 is traject_2 and traject_1.travel_time > 0 and traject_2.travel_time > 0: 
                counter = 0
                length = len(traject_2.connections)
                for connection in traject_2.connections: 
                    counter += 1
                    if connection == first_connection and counter != 0: 
                        # print("before", traject_2)
                        traject_1.delete_connection(first_connection, 0)
                        first_connection = traject_1.connections[0]
                        length -= 1 
                        counter -= 1
                        # print("after", traject_2)

                    elif connection == last_connection and counter != length:
                        # print("before", traject_2)
                        traject_1.delete_connection(last_connection, -1)
                        length -= 1
                        last_connection = traject_1.connections[-1]
                        # print("after", traject_1)

                    if traject_1.travel_time <= 0:
                        break

    return solution

