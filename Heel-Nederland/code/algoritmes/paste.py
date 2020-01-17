def paste(solution):
    trains = solution["trajecten"]

    for train_1 in trains:
        # If the train exists
        if train_1.travel_time > 0:

            first_station_1 = train_1.start_station
            last_station_1 = train_1.current_station

            for train_2 in trains:
                # If both of the trains exist and are not the same train
                if train_1 is not train_2 and train_1.travel_time > 0 and train_2.travel_time > 0:
                    
                    # If the total travel time of both trains does not exeed the train timeframe limit 
                    if train_1.travel_time + train_2.travel_time <= 180:

                        first_station_2 = train_2.start_station
                        last_station_2 = train_2.current_station

                        # If the start station of the first train and the end station of the second train are the same
                        if first_station_1 == last_station_2:

                            # Attach the first train to the end of the second train 
                            for connection in train_1.connections:
                                train_2.add_connection(connection)

                            # Empty the first train object
                            train_1.empty_traject()

                        # If the end station of the first train and the start station of the second train are the same
                        elif first_station_2 == last_station_1:

                            # Attach the second train to the end of the first train 
                            for connection in train_2.connections:
                                train_1.add_connection(connection)
                            
                            # Empty the second train object
                            train_2.empty_traject()

                        # If the end station of the first train and the end station of the second train are the same                        
                        elif last_station_1 == last_station_2:

                            # Attach the first train to the end of the second train in reversed order
                            for connection in reversed(train_1.connections):
                                train_2.add_connection(connection)
                            
                            # Empty the first train object
                            train_1.empty_traject()

                        # If the start station of the first train and the start station of the second train are the same
                        elif first_station_1 == first_station_2: 
                            pass

    return solution
