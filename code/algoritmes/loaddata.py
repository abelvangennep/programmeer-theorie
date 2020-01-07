import csv
from connection import Connection 

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

def loadstations():
    pass
