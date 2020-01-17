def calculate(solution):
    
    trajecten = solution["trajecten"]
    minutes = 0 
    visited_connections = []
    
    for traject in trajecten: 
        minutes += traject.travel_time

        for connection in traject.connections: 
            if connection not in visited_connections: 
                visited_connections.append(connection)
    
    P = len(visited_connections) / solution["total_connections"]

    T = len(trajecten)

    score = P * 10000 - (T * 100 + minutes)
    
 
    # print(f"minutes: {minutes}")
    # print(f"treinen: {T}")
    # print(f"P: {P}")
    # print(f"bezochte trajecten {len(visited_connections)}")
    # print(f"score:{score}")

    return score 


    
    # minutes = 0
    # for traject in solution["trajecten"]:
    #     if traject.travel_time == 0: 
    #         # print("traject.travel_time")
    #         solution["trajecten"].remove(traject)
    #     minutes += traject.travel_time
    
    # solution["trajecten"]
    # P = solution["visited_trajects"] / solution["total_trajects"]
    # T = len(solution["trajecten"])
    # # print(f"minutes:{minutes}")
    # # print(f"number of trajecten:{T}")
    # print(f"P:{P}")
    # score = P * 10000 - (T * 100 + minutes)
    # print(f"minutes: {minutes}")
    # print(f"treinen: {T}")
    # print(f"score:{score}")

    # return score