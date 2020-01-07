import csv
from connection import Connection 

def loaddataconnections(data):
    connections_data = []
    with open(data, newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            connections_object = Connection(row[0], row[1], row[2])
            connections_data.append(connections_object)

    return connections_data