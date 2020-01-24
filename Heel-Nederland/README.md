# RailNL

RailNL is responsible for the intercity trains in the Netherlands. The purpose of this case is to take care of the train routes and get the quality of the routes as high as possible. A train route visits multiple stations and the route can't be longer than the given time frame.

In the first part of the case we focussed on the provinces North- and South-Holland. All connections need to be visited and you can use a maximum of seven trains. Every train isn't allowed to be longer than two hours.

In the second part of the case we focussed on all of the Netherlands. You can use a maximum of twenty trains and every train isn't allowed to be longer than three hours.

In the advanced part you can change three connections and see what happens if a specific station falls out.

There's a function
K = p * 10000 - ( T * 100 + Min )

Where K = quality of the routes, p = fraction of connections that are visited between 0 and 1,
T = amount of trains, Min = total time of all trains

Where the purpose of the case is to get K as high as possible.

## Prerequisites
The code is written in Python 3.7.5, in requirements.txt the used packages can be found. 
Easy installation can be done by using for Mac pip3 and for Windows just use pip

```bash
pip3 install -r requirements.txt
```

## Structure

We seperated our code in different folders. In the folder code you have four folders for
algorithms, classees, heuristics and visualization. In the folder Data are all input csv
 files with the connections and coordinates. Outputfiles contains the highscores and the
 trains that belong to that score.

## Usage
```bash
python3 main.py
```

## Authors
Yana Visscher, Abel van Gennep and Emma de Gier
