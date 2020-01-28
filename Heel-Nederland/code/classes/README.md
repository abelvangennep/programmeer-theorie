# Classes

Further explanation of the classes we used.

All classes:
- Connection
- Station
- Stations
- Train

## Connection
Contains attributes station names within the connection, travel time and a
counter of times the connection is visited.

The functions we wrote within the connection class can be used to compare two
station names with eachother to see if the connection is the same, add a
visit to a connection or delete a connection.

## Station
Contains attribute station name, all the connections in a list, and the x, y
coordinates of the station

The connections list of the station contains connection objects.

The functions we wrote within the station class can be used to add a connection
to a station or delete a connection from a station.

## Stations
Contains an dictionary of all stations as keys and their connections as
values.

The functions we wrote within the station class can be used to get a station
name, add a station object to the stations dictionary, get a random start station with
heuristics or get a complete random start station, dependent on if or which
heuristics are chosen.

## Train
Contains attributes start- and endstation, all connections that are visited and
total travel time.

The functions we wrote within the train class can be used to set a start station,
get a random connection, add a connection to the train object, delete a
station, empty the train or get all the coordinates of all visited train
stations of the train.


### Further information can be find in the docstrings or in the comments within
### the file.
