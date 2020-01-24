def create_train():
    """"""
    station = stations_dict.get_random_start_station(station_uneven_connections, station_1_connection)
    train = Train(station)

    visited_stations = []

    while True:
        connection = train.get_random_connection(visited_stations, station_only_once)
        if station_only_once:
            visited_stations.append(connection.station_1)
            visited_stations.append(connection.station_2)

        if train.travel_time + connection.travel_time > max:
            break

        train.add_connection(connection)
