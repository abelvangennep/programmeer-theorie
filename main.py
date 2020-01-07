import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

import random

from connection import Connection
from loaddata import loaddata, loadconnections, loadstations
from traject import Traject

def main():

    load_data = loaddata('Data/ConnectiesHolland.csv')

    connections_data = loadconnections(load_data)

    # for connection in connections_data:
    #     print(connection)


    trajecten = []
    traject = []
    while (len(traject) < 7):
        train = Traject()
        print(train)
        while(train.end == False):
            randomconnection = random.choice(connections_data)
            train.add_connection(randomconnection)
            print(train)
            # controleren of de connectie uberhaupt gemaakt kan worden
            # random uit lijst oid halen van mogelijke opties van verbindingen



if __name__ == "__main__":
    main()
