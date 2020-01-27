from train import Train
from stations import Stations

def random_solution(stations_dict, connection_objects, station_1_connection, station_uneven_connections, station_only_once, max_minutes, max_trains):
    """Returns random solution with or without heuristics"""

    solution = {}
    trains = []

    while True:
        # Get random start station or with heuristics if chosen
        station = stations_dict.get_random_start_station(station_uneven_connections, station_1_connection)

        # Make a train object
        train = Train(station)

        visited_stations = []

        while True:
            # Get random connection or with heuristics if chosen
            connection = train.get_random_connection(visited_stations, station_only_once)

            # Add to visited_stations if heuristic visit_station_only_once is chosen
            if station_only_once:
                visited_stations.append(connection.station_1)
                visited_stations.append(connection.station_2)

            # Break if maximum minutes is reached
            if train.travel_time + connection.travel_time > max_minutes:
                break

            train.add_connection(connection)

        trains.append(train)

        counter_visited = 0

        for connection in connection_objects:
            # Check if connection is visited and increment visit count
            if connection.visited > 0:
                counter_visited += 1

        # Break if all connections are visited or max train length is reached
        if len(connection_objects) == counter_visited or len(trains) > max_trains:
            break

    # Add trains and connection length to solution dictionary
    solution["trains"] = trains
    solution["total_connections"] = len(connection_objects)
    
    return solution
