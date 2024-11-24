from queue import Queue
from queue import PriorityQueue

def re_path(maze, came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    
    path.reverse()

    return path

def draw_path(maze, path):
    for x, y in path:
        maze[x][y] = 2

# BFS
def bfs(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    came_from = {} # luu cha cua cac diem trong loi giai

    visited = [[0]*cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = Queue()
    q.put((start,0))

    while not q.empty():
        current, step = q.get()

        if current == goal:
            return step, re_path(maze, came_from, current)
        
        for dx, dy in directions:
            new_state = (current[0] + dx, current[1] + dy)

            if 0 < new_state[0] < rows and 0 < new_state[1] < cols and visited[new_state[0]][new_state[1]] == 0:
                if maze[new_state[0]][new_state[1]] != 0:
                    came_from[new_state] = current
                    visited[new_state[0]][new_state[1]] = 1
                    q.put((new_state,step + 1))
    return None


# A STAR
def heurictics(a_point, b_point):
    return abs(a_point[0]-b_point[0]) + abs(a_point[1]-b_point[1])

def a_star(maze, start, goal):
    came_from = {}
    rows = len(maze)
    cols = len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    pq = PriorityQueue()
    pq.put((0,start))

    g = {start : 0}
    f = {start : heurictics(start, goal)}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            return re_path(maze, came_from, current)

        for dx, dy in directions:
            new_state = (current[0] + dx, current[1] + dy)
            if 0 < new_state[0] < rows and 0 < new_state[1] < cols and maze[new_state[0]][new_state[1]] != 0:
                new_g = g[current] + 1

                if new_g < g.get(new_state, float('inf')):
                    came_from[new_state] = current
                    new_f = new_g + heurictics(new_state, goal)
                    f[new_state] = new_f
                    g[new_state] = new_g
                    pq.put((new_f, new_state))
    return None




