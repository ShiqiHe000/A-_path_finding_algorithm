import pygame
import math
from queue import PriorityQueue

WIDTH = 800 # square window
WIN = pygame.display.set_mode((WIDTH, WIDTH))   # set up display
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)   # already visited node
GREEN = (0, 255, 0) # node in the open set
BLUE = (50, 140, 250)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255) # has not been visited
BLACK = (0, 0, 0)   # a barrier
PURPLE = (128, 0, 128)  # the path
ORANGE = (255, 165, 0)  # start node
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)  # the end node

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = col * width    # the coordinate of the cube
        self.y = row * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # return the row, col of the current spot
    def get_position(self):
        return self.row, self.col

    # we have visited this spot
    def is_closed(self):
        return self.color == RED

    # is this spot in the open set
    def is_open(self):
        return self.color == GREEN

    # is a barrier node?
    def is_barrier(self):
        return self.color == BLACK

    # start node?
    def is_start(self):
        return self.color == ORANGE

    # end node?
    def is_end(self):
        return self.color == BLUE

    # reset to white
    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = BLUE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # up
        if self.row - 1 >= 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        # down
        if self.row + 1 < self.total_rows and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        # left
        if self.col - 1 >= 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])
        # right
        if self.col + 1 < self.total_rows and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

    def __lt__(self, other):
        return False

# heuristic function (H(n))
# p1: point1
# p2: point2
def h(p1, p2):
    row1, col1 = p1
    row2, col2 = p2
    return abs(row1 - row2) + abs(col1 - col2)

# draw: lambda function to draw the surface
# grid: the 2d list of the grid
# start: the start spot
# end: the end spot
def algorithm(draw, grid, start, end):
    draw()

    count = 0   # the time we came to this spot. Use this to break tie if two spots have same F value
    open_set = PriorityQueue()
    open_set.put((0, count, start)) # (F(n), time we came to thsi spot, spot)
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_position(), end.get_position())

    # a set to tell us what's in the priority queue
    open_set_hash = {start}

    while not open_set.empty():
        # allows the user to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        current = open_set.get()[2] # current node
        open_set_hash.remove(current)

        if current == end:  # we found the shortest path
            # todo: make path
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:    # shorter path, update
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_position(), end.get_position())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()  # put this neighbour in open_set

        draw()

        if current != start:
            current.make_closed()

    return False       # we do not find the path



# a list to hold all the spot in teh grid
# square domain rows = cols
# width: the width of the entire grid.
def make_grid(rows, width):
    grid = []   # make it a 2D list that represent the domain
    gap = width // rows # the width of each cube

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


# draw the grid lines (grey)
def draw_grid_lines(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


# fun to draw every thing
def draw(win, grid, rows, width):
    # fill the surface with a solid color
    win.fill(WHITE)

    # draw the spot
    for row in grid:
        for spot in row:
            spot.draw(win)
    # draw the grid lines
    draw_grid_lines(win, rows, width)
#    pygame.display.flip()
    pygame.display.update()


# get the spot the mouse chooses. Return the row and column of the cliked spot.
# pos: mouse position
# rows: total rows
# width: domain size
def get_click_position(pos, rows, width):
    gap = width // rows

    x, y = pos
    row = y // gap
    col = x // gap

    return row, col

def main(win, width):
    ROWS = 50   # COLS = ROWS
    grid = make_grid(ROWS, width)

    # start and end positions
    start = None
    end = None

    run = True  # run the main loop or not
    started = False # we started the algorithm or not

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue    # if the algorithm is started,
                            # we don't want the user to input anymore (except quit).
            if pygame.mouse.get_pressed()[0]: # left button
                pos = pygame.mouse.get_pos()
                row, col = get_click_position(pos, ROWS, width)
                spot = grid[row][col]   # get the spot
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start: # make it a barrier
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # right button
                pos = pygame.mouse.get_pos()
                row, col = get_click_position(pos, ROWS, width)
                spot = grid[row][col]   # get the spot
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (not started):    # start running the algorithm
                    started = True
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    # call algorithm
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

    pygame.quit()   # exit the pygame window



main(WIN, WIDTH)
