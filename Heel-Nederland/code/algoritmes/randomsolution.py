from traject import Traject
from stations import Stations

def random_solution(stations_objects, connection_objects):
    max = 180
    solution = {}
    trajecten = []
    total_travel_time = 0
    for _ in range(20):
        station = stations_objects.get_random_station()
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

        # print(f"{traject}\n")
        trajecten.append(traject)

        counter_visited = 0
       
        for connection in connection_objects:
            if connection.visited == True:
                counter_visited += 1
        if len(connection_objects) == counter_visited:
            # print("gelukt")
            break
    
    for traject in trajecten:
        total_travel_time += traject.travel_time

    solution["total_travel_time"] = total_travel_time
    solution["visited_trajects"] = counter_visited
    solution["total_trajects"] = len(connection_objects)
    solution["trajecten"] = trajecten

    return solution

def solution_1_city(stations_objects, connection_objects):
    # niet 2 keer in dezelfde stad met dezelfde trein
    max = 180
    solution = {}
    trajecten = []
    total_travel_time = 0
    for _ in range(20):
        station = stations_objects.get_random_station()
        traject = Traject(station) 
        # print(f"traject: {traject}")
        # print(f"traject_station: {traject.current_station}")
        visited_stations = []
        while True:
            # print(f"currentstation:{traject.current_station}")
            connection = traject.current_station.get_random_connection_1(visited_stations)
            visited_stations.append(connection.station_1)
            visited_stations.append(connection.station_2)

            if traject.travel_time + connection.travel_time > max:
                break 

            traject.add_connection(connection)
            connection.set_visited()

        # print(f"{traject}\n")
        trajecten.append(traject)

        counter_visited = 0
       
        for connection in connection_objects:
            if connection.visited == True:
                counter_visited += 1
        if len(connection_objects) == counter_visited:
            # print("gelukt")
            break
    
    for traject in trajecten:
        total_travel_time += traject.travel_time

    solution["total_travel_time"] = total_travel_time
    solution["visited_trajects"] = counter_visited
    solution["total_trajects"] = len(connection_objects)
    solution["trajecten"] = trajecten

    return solution


