import random
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
import time
from utils import save_solution
from __init__ import Maze

from maze_solve import bfs, a_star

def visualize_maze(maze,algorithms):
    points = []
    def onclick(event):
        if len(points) < 2:
            x, y = int(event.ydata), int(event.xdata)
        
            if maze[x][y] == 1:
                points.append((x,y))
                plt.scatter(y,x, c='red', s=25)
                plt.draw()

                if len(points) == 2:
                    start, goal = points[0] , points[1]
                    print(f"start: {start}, goal: {goal}")

                    st = time.time()
                    path = algorithms(maze, start, goal)
                    et = time.time()
                    _time = et-st

                    if path:
                        colored_maze = maze.copy()
                        for dx, dy in path:
                            colored_maze[dx,dy] = 2
                        
                        cmap = ListedColormap(["black", "white", "green"])
                        plt.imshow(colored_maze, cmap=cmap)
                        plt.title(f"{algorithms.__name__}, time : {_time}")
                        plt.show()
                        save_solution(maze, start, goal, path, algorithms, _time)
                    else:
                        print("error")
            else:
                print("chon start va goal")
    
    plt.imshow(maze, cmap="gray")
    plt.title("click to select 2 points")
    plt.connect('button_press_event', onclick)
    plt.show()
