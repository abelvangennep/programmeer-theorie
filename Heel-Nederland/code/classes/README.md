# Classes

Further explanation of the classes we used.

All classes:
1. Connection
1. Station
1. Stations
1. Train

## Connection
Contains attributes station names within the connection, travel time and a
counter of times the connection is visited.

Can compare two station names with eachother to see if the connection is the
same. Add and delete a visit to a connection.

## Station
Contains attribute station name, all the connections in a list, and the x, y
coordinates of the station

The connections list of the station contains connection objects.

DEFS
Add and delete an connection to a station.

## Stations
Contains an dictionary of all stations as keys and their connections as
values.

DEFS
- Get_random_start_station: where dependent on the chosen heuristics a start
station is returned.
- get_complete_random_start_station: complete random start station for the random solution.

## Train
Contains attributes start- and endstation, all connections that are visited
and total travel time.

DEFS
- set_start_station: set start station and current station
- get_random_connection: return a random connection
- add_connection: add a connection to a train
- delete_connection: delete connection of a train
