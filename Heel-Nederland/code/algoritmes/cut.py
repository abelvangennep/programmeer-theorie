def cut(solution):
    trajecten = solution["trajecten"]
    for traject_1 in trajecten:
        first_connection = traject_1.connections[0]
        last_connection = traject_1.connections[-1]

        for traject_2 in trajecten:
            if traject_1 is not traject_2:
                for connection in traject_2.connections:
                    if connection == first_connection:
                        # print(f"eerst:{traject_1.travel_time}")
                        # print(first_connection)
                        traject_1.delete_connection(first_connection)
                        first_connection = traject_1.connections[0]
                        # print(first_connection)
                        # print(traject_1.travel_time)

                    elif connection == last_connection: 
                        traject_1.delete_connection(last_connection)
                        last_connection = traject_1.connections[-1]

    return solution
