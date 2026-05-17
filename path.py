import tkinter as tk
from collections import deque



ROWS = 20
COLS = 20
CELL_SIZE = 25

width = COLS * CELL_SIZE
height = ROWS * CELL_SIZE

EMPTY = 0
WALL = 1
start  = 2
end = 3
PATH = 4
mode = "wall"

root = tk.Tk()
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

grid = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid():
    canvas.delete("all")
    for i in range(ROWS):
        for j in range(COLS):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            if grid[i][j] == WALL:
                fill="black"
            else:        
                fill="white"
            if grid[i][j] == start:
                fill="green"
            if grid[i][j] == end:
                fill="red"
            if grid[i][j] == PATH:
                fill="blue"
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="gray")
mode = "wall"


def click(event):
    global mode
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE

    if mode == "wall":
        if grid[row][col] == WALL:
            grid[row][col] = EMPTY
        else:
            grid[row][col] = WALL
    if mode == "start":
        grid[row][col] = start
        mode = "wall"

    elif mode == "end":
        grid[row][col] = end
        mode = "wall"

    draw_grid()


canvas.bind("<Button-1>", click)


def set_start():
    global mode
    mode = "start"


def set_end():
    global mode
    mode = "end"




start_button = tk.Button(root, text="Set Start", command=set_start)
start_button.pack(side=tk.LEFT)

end_button = tk.Button(root, text="Set End", command=set_end)
end_button.pack(side=tk.LEFT)


draw_grid()


#--------------------------
#BFS METHOD :-
#--------------------------


start_pos = None
end_pos = None


def bfs():
    global start_pos, end_pos
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == start:
                start_pos = (i, j)
            
            elif grid[i][j] == end:
                end_pos = (i, j)
    queue = deque([start_pos])
    visited = set([start_pos])
    parent = {}
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        current = queue.popleft()

        if current == end_pos:
            reconstruct(parent)
            return
        
        for d in directions:
            r = current[0] + d[0]
            c = current[1] + d[1]

            if 0 <= r < ROWS and 0 <= c < COLS:
                if (r, c) not in visited and grid[r][c] != WALL:
                    queue.append((r, c))
                    visited.add((r, c))
                    parent[(r, c)] = current

    print("Start:", start_pos)
    print("End:", end_pos)

# -----------------------------
# PATH RECONSTRUCTION
# -----------------------------

def reconstruct(parent):
    current = end_pos
    while current != start_pos:
        current = parent[current] # cell
        if current != start_pos:
            grid[current[0]][current[1]] = PATH

    draw_grid()

def reset():  
    global grid, start_pos, end_pos
    grid = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    start_pos = None
    end_pos = None

    draw_grid()


frame = tk.Frame(root)
frame.pack()
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(side=tk.LEFT)
start_bfs_button = tk.Button(root, text="Start BFS", command=bfs)
start_bfs_button.pack(side=tk.LEFT)



draw_grid()

root.mainloop()