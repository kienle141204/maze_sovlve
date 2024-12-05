from __init__ import Maze
from maze_solve import bfs, a_star
from utils import save_solution
from visualize import visualize_maze

def main():
    n = int(input("Nhập kích thước mê cung bạn muốn : "))
    
    maze = Maze(n, n)
    maze = maze.create_maze_dfs()

    nn = int(input("nhap so diem di qua : "))
    visualize_maze(maze, nn)

if __name__ == '__main__':
    main()