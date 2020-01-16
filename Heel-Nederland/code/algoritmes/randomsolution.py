from traject import Traject
from stations import Stations

def random_solution(stations_objects, connection_objects, station_1_connection, station_uneven_connections, connection_only_once):
    max = 180
    solution = {}
    trajecten = []
    total_travel_time = 0

    for _ in range(20):
        if station_1_connection:
            station = stations_objects.get_random_station_1_conn(station_uneven_connections)
        elif station_uneven_connections:
            station = stations_objects.get_random_station_uneven_conn()
        else:
            station = stations_objects.get_random_station()
        
        traject = Traject(station) 

        
        visited_stations = []
        while True:
            connection = traject.get_random_connection(visited_stations, connection_only_once)
            if connection_only_once:
                visited_stations.append(connection.station_1)
                visited_stations.append(connection.station_2)

            if traject.travel_time + connection.travel_time > max:
                break 

            traject.add_connection(connection)
            connection.set_visited()

        trajecten.append(traject)

        counter_visited = 0
       
        for connection in connection_objects:
            # if connection.visited == True:
            if connection.visited > 0:  
                counter_visited += 1
        if len(connection_objects) == counter_visited:
            break
    
    for traject in trajecten:
        total_travel_time += traject.travel_time

    solution["total_travel_time"] = total_travel_time
    solution["visited_trajects"] = counter_visited
    solution["total_trajects"] = len(connection_objects)
    solution["trajecten"] = trajecten

    return solution