def paste(solution): 
    trajecten = solution["trajecten"]

    for traject_1 in trajecten: 
        if traject_1.travel_time > 0: 
            first_station_1 = traject_1.start_station
            last_station_1 = traject_1.current_station

            for traject_2 in trajecten: 
                if traject_1 is not traject_2 and traject_1.travel_time > 0 and traject_2.travel_time > 0: 
                    if traject_1.travel_time + traject_2.travel_time <= 180:

                        first_station_2 = traject_2.start_station
                        last_station_2 = traject_2.current_station 

                        if first_station_1 == last_station_2:
                            # print(f"\n traject 1 before: {traject_1}\n")
                            # print(f"traject 2 before: {traject_2}\n")
                            
                            for connection in traject_1.connections: 
                                traject_2.add_connection(connection)
                        
                            traject_1.empty_traject()
                                
                            # print(f"traject 1 after: {traject_1}\n")
                            # print(f"traject 2 after: {traject_2}\n")
                        
                        elif first_station_2 == last_station_1: 

                        #     print(f"\n traject 1 before: {traject_1}\n")
                        #     print(f"traject 2 before: {traject_2}\n")                        

                            for connection in traject_2.connections: 
                                traject_1.add_connection(connection)
                            traject_2.empty_traject() 

                        #     print(f"traject 1 after: {traject_1}\n")
                        #     print(f"traject 2 after: {traject_2}\n")

                        elif last_station_1 == last_station_2: 
                        #     print(f"\n traject 1 before: {traject_1}\n")
                        #     print(f"traject 2 before: {traject_2}\n")      

                            for connection in reversed(traject_1.connections): 
                                traject_2.add_connection(connection)
                            traject_1.empty_traject()
                                
                        #     print(f"traject 1 after: {traject_1}\n")
                        #     print(f"traject 2 after: {traject_2}\n")

    return solution


