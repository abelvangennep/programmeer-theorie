from traject import Traject
from stations import Stations

def random_solution(stations_dict, connection_objects, station_1_connection, station_uneven_connections, station_only_once):
    max = 180
    solution = {}
    trajecten = []

    while True:
        station = stations_dict.get_random_start_station(station_uneven_connections, station_1_connection)
        traject = Traject(station) 

        visited_stations = []

        while True:
            connection = traject.get_random_connection(visited_stations, station_only_once)
            if station_only_once:
                visited_stations.append(connection.station_1)
                visited_stations.append(connection.station_2)

            if traject.travel_time + connection.travel_time > max:
                break 

            traject.add_connection(connection)

        trajecten.append(traject)

        counter_visited = 0
       
        for connection in connection_objects:
            # if connection is visited
            if connection.visited > 0:  
                counter_visited += 1
                
        if len(connection_objects) == counter_visited or len(trajecten) > 20:
            break

    existing_trajecten = []
    for traject in trajecten: 
        if traject.travel_time > 0: 
            existing_trajecten.append(traject)
    
    solution["total_connections"] = len(connection_objects)
    solution["trajecten"] = existing_trajecten

    return solution