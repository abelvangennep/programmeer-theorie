from train import Train
from stations import Stations

def random_solution(stations_dict, connection_objects, station_1_connection, station_uneven_connections, station_only_once, max_minutes, max_trains):
    # max = 180
    solution = {}
    trains = []

    while True:
        station = stations_dict.get_random_start_station(station_uneven_connections, station_1_connection)
        train = Train(station) 

        visited_stations = []

        while True:
            connection = train.get_random_connection(visited_stations, station_only_once)
            if station_only_once:
                visited_stations.append(connection.station_1)
                visited_stations.append(connection.station_2)

            if train.travel_time + connection.travel_time > max_minutes:
                break 

            train.add_connection(connection)

        trains.append(train)

        counter_visited = 0
       
        for connection in connection_objects:
            # if connection is visited
            if connection.visited > 0:  
                counter_visited += 1
                
        if len(connection_objects) == counter_visited or len(trains) > max_trains:
            break

    solution["trains"] = trains
    solution["total_connections"] = len(connection_objects)
    
    return solution