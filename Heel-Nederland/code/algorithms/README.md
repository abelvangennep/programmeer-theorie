# Algorithms

Further explanation of the algorithms we used.

All algorithms:
- Random
- Random with heuristics
- Simulated Annealing
- Simulated Annealing with heuristics

## Random

Our random solution returns a random solution with or without heuristics,
dependent on the users choices. Our algorithm always prefers a connection that's
not visited yet, above one that's already visited.

## Simulated Annealing

Simulated annealing is a probabilistic algorithm, which can calculate a global
optimum. The algorithm compares the scores of two different solutions, even a
worse score can be excepted. To achieve the optimum, three parameters have
to be optimized, the cooling_factor, temperature and end_temperature.

Our simulated annealing algorithm can also be used with heuristics.
The starting point of simulated annealing is with a random solution or random
with heuristics.

The default parameters are:
temp = 180
cooling = 0.99999
end = 5
trains = 10


### Further information can be find in the docstrings or in the comments within
### the file.
