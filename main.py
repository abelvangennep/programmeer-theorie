import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


from connection import Connection 
from loaddataconnections import loaddataconnections

def main():

    connections_data = loaddataconnections('Data/ConnectiesHolland.csv')

    for connection in connections_data:
        print(connection)
            





    #         row.append('0')
    #         if row[0] in dict_connections:
    #             dict_connections[row[0]].append(row)
    #         else:
    #             dict_connections[row[0]] = [row]
            
    #         if row[1] in dict_connections:
    #             dict_connections[row[1]].append(row)
    #         else:
    #             dict_connections[row[1]] = [row]
            
    # for key in dict_connections.keys():
    #    dict_connections[key]

if __name__ == "__main__":
    main()