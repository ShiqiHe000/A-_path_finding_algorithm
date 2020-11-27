import pygame
import math
from queue import PriorityQueue

WIDTH = 800 # square window
WIN = pygame.display.set_mode((WIDTH, WIDTH))   # set up display
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)   # already visited node
GREEN = (0, 255, 0) # node in the open set
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255) # has not been visited
BLACK = (0, 0, 0)   # a barrier
PURPLE = (128, 0, 128)  # the path
ORANGE = (255, 165 ,0)  # start node
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)  # the end node

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width    # the coordinate of the cube
        self.y = col + width
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
        return self.color == TURQUOISE

    # reset to white
    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width) )

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False

# heuristic function (H(n))
# p1: point1
# p2: point2
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

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
            pygame.draw.line(win, GREY, (j * gap, 0). (j * gap, width))

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

    pygame.display.update()

# get the spot the mouse chooses. Return the row and column of the cliked spot.
# pos: mouse position
# rows: total rows
# width: domain size
def get_click_position(pos, rows, width):
    gap = width // rows

    y, x = pos
    row = y // gap
    col = x // gap

    return row, col

def main(win, width):
    ROWS = 50   # COLS = ROWS
    gird = make_grid(ROWS, WIDTH)

    # start and end positions
    start = None
    end = None

    run = True  # run the main loop or not
    started = False # we started the algorithm or not

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif started:
                continue    # if the algorithm is started,
                            # we don't want the user to input anymore (except quit).


    pygame.quit()   # exit the pygame window
