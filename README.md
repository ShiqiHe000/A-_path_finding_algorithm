# A* Pathfinding Algorithm with Visualization
[A*](https://en.wikipedia.org/wiki/A*_search_algorithm) is a graph traversal and path search algorithm, 
which is often used in many fields of computer science due to its completeness, 
optimality, and optimal efficiency. 

A* is a **best-first search**, 
meaning that it is formulated in terms of weighted graphs: 
starting from a specific starting node of a graph, 
it aims to find a path to the given goal node having the smallest cost 
(least distance travelled, etc.). 

A* select the shortest path that minimizes the function:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(n)&space;=&space;g(n)&space;&plus;&space;h(n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(n)&space;=&space;g(n)&space;&plus;&space;h(n)" title="f(n) = g(n) + h(n)" /></a>

where `n` is the current node in the graph, `g(n)` is the cost of the path from the start node to `n`, 
`h(n)` is a heuristic function that estimate the minimum cost from the current node to the goal. 
If you want to know more, please check [here](https://en.wikipedia.org/wiki/A*_search_algorithm). 

