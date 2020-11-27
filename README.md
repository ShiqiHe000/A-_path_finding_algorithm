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

# Want to Play with the Program?
To see how the algorithm works, execute the `main.py` program:

```
  python3 main.py
```
Note that you to have `pygame` installed ([How to install pygame](https://www.pygame.org/wiki/GettingStarted)). 

**Don't want to download the program? Try it in Gitpod!** 

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ShiqiHe000/A_start_pathfinding_algorithm/main.py)

## How to Play?
1. Use you mouse to choose (left clik) a **start point**. This point will be colored in orange. 
    Note that if you want to erase your choice, just right clik the point. 
2. Use you mouse to choose a **end point**. This point will be colored in blue. 
3. Press the left key of your mouse and draw the **barrers** between the start and end points. The bariiers will be colored in black. 
4. When you finished, press space key to see the algorithm processes and find the shortest path between two targeted node.
    In the end, the shortest path will be colored in purple. 
5. To restart the program, press `c`. 


Performance example:
<p align="center">
  <img src="./imgs/example.png" width="300" height = "300" class="center">
</p>
