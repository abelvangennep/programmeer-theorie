import csv
from connection import Connection 
# from station import Station

def loaddata(data):
    data_list = []
    with open(data, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
             data_list.append(row)

    return data_list

def loadconnections(data_list):
    connections_data = []
    for row in data_list:
        connections_object = Connection(row[0], row[1], row[2])
        connections_data.append(connections_object)

    return connections_data

# def loadstations(data_list):
#     stations_data = []
#     for row in data_list:
#         for station in stations_data:  
#             if row[0] == stations_data[station][1]: 
#                 pass
#             stations_object = Station(row[0])
#             stations_data.append(stations_object)
        
#     return stations_data

