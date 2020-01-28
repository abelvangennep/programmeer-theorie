from train import Train
from stations import Stations


def random_solution(stations_dict, connection_objects, user_choices):
    """This method returns a random solution with or without heuristics"""

    counter_visited = 0 
    solution = {}
    trains = []

    # While not all connections are visited yet 
    # and the maximum amount of trains is not reached
    while len(connection_objects) != counter_visited\
        and len(trains) < user_choices["max_trains"]:

        counter_visited = 0 
        visited_stations = [] 
        
        # Get a random start station, applying chosen heuristics       
        station = stations_dict.get_random_start_station(
            user_choices["station_uneven_connections"],
            user_choices["station_1_connection"])

        # Make a new train object
        train = Train(station)

        while True:
            # Get a random connection, applying chosen heuristics
            connection = train.get_random_connection(visited_stations,
                user_choices["station_only_once"])

            # Add the stations in this connection to a list of visited stations
            # if heuristic of visiting a station only once per train is chosen
            if user_choices["station_only_once"]:
                visited_stations.append(connection.station_1)
                visited_stations.append(connection.station_2)

            # Break if adding the connection would exceed the max train duration
            if train.travel_time + connection.travel_time >\
                user_choices["max_minutes"]:
                break
            
            train.add_connection(connection)

        trains.append(train)

        for connection in connection_objects:
            # Check if connection is visited and increment visit count
            if connection.visited > 0:
                counter_visited += 1

    # Add trains and length of visited connections to the solution dictionary
    solution["trains"] = trains
    solution["total_connections"] = len(connection_objects)

    return solution
