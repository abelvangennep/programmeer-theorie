def cut(solution): 
    trajecten = solution["trajecten"]

    for traject in trajecten: 
        while traject.travel_time > 0: 

            first_connection = traject.connections[0]
            last_connection = traject.connections[-1]

            if first_connection.visited > 1: 
                traject.delete_connection(first_connection, 0)

            elif last_connection.visited > 1: 
                traject.delete_connection(last_connection, -1)
            
            else: 
                break 
    
    return solution




# def cut(solution):
#     trajecten = solution["trajecten"]
#     # print(trajecten)

#     for traject_1 in trajecten:
#         if traject_1.travel_time > 0: 
        
#             first_connection = traject_1.connections[0]
#             last_connection = traject_1.connections[-1]
            
#             for traject_2 in trajecten:
#                 if traject_1 is not traject_2 and traject_1.travel_time > 0 and traject_2.travel_time > 0:
                    
#                     for connection in traject_2.connections:
#                         if connection == first_connection:
#                             # print("\n before (delete first connection)", traject_1)
#                             traject_1.delete_connection(first_connection, 1)
#                             if traject_1.travel_time > 0:                             
#                                 first_connection = traject_1.connections[0]
#                             # print("after", traject_1)

                            
#                         elif connection == last_connection:
#                             # print("\n before (delete last connection)", traject_1)
#                             traject_1.delete_connection(last_connection, -1)
#                             if traject_1.travel_time > 0: 
#                                 last_connection = traject_1.connections[-1]
#                             # print("after", traject_1)
                    
#                         if traject_1.travel_time <= 0:
#                             break

#                 elif traject_1 is traject_2 and traject_1.travel_time > 0 and traject_2.travel_time > 0: 
#                     counter = 0
#                     length = len(traject_2.connections)
#                     for connection in traject_2.connections: 
#                         counter += 1
#                         if connection == first_connection and counter != 1: 
#                             # print("error 1")
#                             # print("delete first connection", counter, connection)
#                             # print("first_connection =", first_connection)
#                             # print("\n before", traject_2)
#                             traject_1.delete_connection(first_connection, 0)
#                             first_connection = traject_1.connections[0]
#                             length -= 1 
#                             counter -= 1
#                             # print("after", traject_2)

#                         elif connection == last_connection and counter != length:
#                             # print("error 2")
#                             # print("\n before (delete last connection)", traject_2)
#                             traject_1.delete_connection(last_connection, -1)
#                             length -= 1
#                             last_connection = traject_1.connections[-1]
#                             # print("after", traject_2)

#                         # if traject_1.travel_time <= 0:
#                         #     break

#     return solution

