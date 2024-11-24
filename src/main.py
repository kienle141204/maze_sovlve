from __init__ import Maze
from maze_solve import bfs, a_star
from utils import save_solution
from visualize import visualize_maze

def main():
    width = int(input("nhap chieu rong me cung : "))
    height = int(input("nhap chieu dai me cung : "))

    maze = Maze(width, height)
    maze = maze.create_maze_dfs()

    visualize_maze(maze,a_star)
    visualize_maze(maze,bfs)


if __name__ == '__main__':
    main()