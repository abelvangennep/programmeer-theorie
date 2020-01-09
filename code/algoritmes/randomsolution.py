from traject import Traject
from stations import Stations

def random_solution(stations_objects, connection_objects):
    max = 120
    solution = {}
    trajecten = []
    total_travel_time = 0
    for i in range(7):
        station = stations_objects.get_random()
        traject = Traject(station) 
        # print(f"traject: {traject}")
        # print(f"traject_station: {traject.current_station}")
        while True:
            # print(f"currentstation:{traject.current_station}")
            connection = traject.current_station.get_random_connection()
            

            if traject.travel_time + connection.travel_time > max:
                break 

            traject.add_connection(connection)
            connection.set_visited()

        print(f"{traject}\n")
        trajecten.append(traject)

        
        counter_visited = 0
       
        for connection in connection_objects:
            if connection.visited == True:
                counter_visited += 1
        if len(connection_objects) == counter_visited:
            print("gelukt")
            break
    
    for traject in trajecten:
        total_travel_time += traject.travel_time
        
    solution["total_travel_time"] = total_travel_time
    solution["visited_trajects"] = counter_visited
    solution["trajecten"] = trajecten

    
    return solution


