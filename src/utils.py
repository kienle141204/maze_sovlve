import json
import os
import numpy as np

def save_solution(maze, start, goal, path, algorithm, _time):
    steps = len(path)
    out_path = f'results/{algorithm.__name__}.json'

    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # Chuyển maze thành danh sách để JSON có thể xử lý
    maze_list = maze.tolist() if isinstance(maze, np.ndarray) else maze

    # Tạo dữ liệu đầu ra
    solution_data = {
        "maze shape": maze.shape ,
        "start": start,
        "goal": goal,
        "algorithm": algorithm.__name__,
        "steps": steps,
        "solution": [f"{x}, {y}" for x, y in path],
        "execution_time": _time
    }

    # Ghi dữ liệu vào tệp JSON
    with open(out_path, 'w') as json_file:
        json.dump(solution_data, json_file, indent=4)

    print(f'Solution saved to {out_path}')



