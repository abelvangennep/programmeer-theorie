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

if __name__ == "__main__":
    main()