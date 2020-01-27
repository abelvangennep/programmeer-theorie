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
We seperated our code in different folders. In the folder code you have four folders for algorithms, classes, heuristics and visualization. In the algorithm folder you can find the different algorithms we used. We have a complete random solution and simulated annealing solution. Both can be used with or without heuristics, which you can find in the heuristics folder.
In the folder data contains all input csv files with the connections and coordinates. Outputfiles contains the highscores and the
trains that belong to that score.

## Usage
We made a user interface so the user can choose North-/South-Holland or Holland, which algorithms and if heuristics should be used. And the user can choose if a station should be omitted or different connections should be made (advanced part).
Just run:

```bash
python3 main.py
```

## Authors
Yana Visscher, Abel van Gennep and Emma de Gier


## Highscore 

trein, Vlissingen - 63 - Roosendaal - 22 - Dordrecht - 18 - Breda - 13 - Tilburg - 21 - Eindhoven - 9 - Helmond - 30 - Venlo (176)
trein, Enschede - 7 - Hengelo - 10 - Almelo - 42 - Zwolle - 35 - Amersfoort - 24 - Apeldoorn - 20 - Zutphen - 12 - Deventer - 24 - Almelo (174)
trein, Den Helder - 36 - Alkmaar - 9 - Castricum - 12 - Zaandam - 25 - Beverwijk - 16 - Haarlem - 6 - Heemstede-Aerdenhout - 13 - Leiden Centraal - 12 - Den Haag HS - 8 - Delft - 7 - Schiedam Centrum - 5 - Rotterdam Centraal (149)
trein, Lelystad Centrum - 14 - Almere Centrum - 27 - Amsterdam Amstel - 10 - Amsterdam Zuid - 6 - Schiphol Airport - 15 - Leiden Centraal - 9 - Den Haag Laan v NOI - 12 - Delft - 13 - Den Haag Centraal - 12 - Leiden Centraal - 14 - Alphen a/d Rijn - 28 - Utrecht Centraal - 14 - Amersfoort (174)
trein, Zwolle - 40 - Assen - 17 - Groningen - 35 - Leeuwarden - 16 - Heerenveen - 14 - Steenwijk - 24 - Zwolle - 24 - Deventer - 10 - Apeldoorn (180)
trein, Hilversum - 26 - Almere Centrum - 20 - Amsterdam Centraal - 6 - Amsterdam Sloterdijk - 6 - Zaandam - 26 - Hoorn - 24 - Alkmaar - 9 - Castricum - 13 - Beverwijk - 16 - Haarlem - 11 - Amsterdam Sloterdijk - 16 - Amsterdam Zuid (173)
trein, Den Haag Centraal - 18 - Gouda - 10 - Rotterdam Alexander - 9 - Rotterdam Blaak - 14 - Dordrecht - 17 - Rotterdam Centraal - 8 - Rotterdam Alexander - 9 - Rotterdam Blaak - 11 - Schiedam Centrum - 7 - Delft - 8 - Den Haag HS - 21 - Gouda - 19 - Alphen a/d Rijn (151)
trein, Roosendaal - 11 - Etten-Leur - 7 - Breda - 13 - Tilburg - 15 - s-Hertogenbosch - 27 - Utrecht Centraal - 18 - Gouda - 28 - Den Haag Laan v NOI - 9 - Leiden Centraal - 15 - Schiphol Airport - 33 - Utrecht Centraal (176)
trein, Amsterdam Amstel - 8 - Amsterdam Centraal - 27 - Utrecht Centraal - 15 - Hilversum - 28 - Amsterdam Amstel - 19 - Utrecht Centraal - 24 - Ede-Wageningen - 10 - Arnhem Centraal (131)
trein, Zutphen - 8 - Dieren - 12 - Arnhem Centraal - 12 - Nijmegen - 16 - Oss - 11 - s-Hertogenbosch - 18 - Eindhoven - 17 - Weert - 14 - Roermond - 15 - Sittard - 15 - Heerlen - 15 - Sittard - 15 - Maastricht (168)

attempts:3371716
SCORE:7348.0