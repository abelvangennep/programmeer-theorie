import csv

list_cities = []
dict_connections = {}
with open('Data/ConnectiesHolland.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        row.append('0')
        if row[0] in dict_connections:
            dict_connections[row[0]].append(row)
        else:
            dict_connections[row[0]] = [row]
        
        if row[1] in dict_connections:
            dict_connections[row[1]].append(row)
        else:
            dict_connections[row[1]] = [row]
        
for key in dict_connections.keys():
    dict_connections[key]
