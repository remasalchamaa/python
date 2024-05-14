import copy

maze = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]


def is_valid(dest, visited):
    x = dest[0]
    y = dest[1]
    if x < 0 or x >= len(maze):
        return False
    if y < 0 or y >= len(maze[0]):
        return False
    if maze[x][y] == 0:
        return False
    if visited[x][y] == True:
        return False
    return True


rec_total_sol = 0


def maze_dfs_recur(start, goal, visited, num_moves):
    global rec_total_sol
    if start == goal:
        print(f"at the goal with {num_moves} moves")
        for row in visited:
            row_txt = ''
            for col in row:
                row_txt += f"{col:<3}"
            print(row_txt)
        rec_total_sol += 1
        return

    if is_valid([start[0], start[1]+1], visited):
        temp_visited = copy.deepcopy(visited)
        temp_visited[start[0]][start[1]+1] = True
        maze_dfs_recur([start[0], start[1]+1], goal,
                       temp_visited, num_moves + 1)

    if is_valid([start[0]+1, start[1]], visited):
        temp_visited = copy.deepcopy(visited)
        temp_visited[start[0]+1][start[1]] = True
        maze_dfs_recur([start[0]+1, start[1]], goal,
                       temp_visited, num_moves + 1)

    if is_valid([start[0], start[1]-1], visited):
        temp_visited = copy.deepcopy(visited)
        temp_visited[start[0]][start[1]-1] = True
        maze_dfs_recur([start[0], start[1]-1], goal,
                       temp_visited, num_moves + 1)

    if is_valid([start[0]-1, start[1]], visited):
        temp_visited = copy.deepcopy(visited)
        temp_visited[start[0]-1][start[1]] = True
        maze_dfs_recur([start[0]-1, start[1]], goal,
                       temp_visited, num_moves + 1)


# visited[0][0] = True
# maze_dfs_recur([0, 0], [4, 4], visited, 0)
# print("total recursion solutions: ", rec_total_sol)

q = []
q_total_sol = 0


def maze_dfs_stack():
    global q_total_sol
    while len(q):
        cur = q.pop()
        start = cur[0]
        goal = cur[1]
        visited = cur[2]
        num_moves = cur[3]

        if start == goal:
            q_total_sol += 1
            print(f"at the goal with {num_moves} moves")
            for row in visited:
                row_txt = ''
                for col in row:
                    row_txt += f"{col:<3}"
                print(row_txt)

        if is_valid([start[0]+1, start[1]], visited):
            temp_visited = copy.deepcopy(visited)
            temp_visited[start[0]+1][start[1]] = True
            q.append([[start[0]+1, start[1]], goal,
                     temp_visited, num_moves + 1])

        if is_valid([start[0], start[1]+1], visited):
            temp_visited = copy.deepcopy(visited)
            temp_visited[start[0]][start[1]+1] = True
            q.append([[start[0], start[1]+1], goal,
                     temp_visited, num_moves + 1])

        if is_valid([start[0], start[1]-1], visited):
            temp_visited = copy.deepcopy(visited)
            temp_visited[start[0]][start[1]-1] = True
            q.append([[start[0], start[1]-1], goal,
                     temp_visited, num_moves + 1])

        if is_valid([start[0]-1, start[1]], visited):
            temp_visited = copy.deepcopy(visited)
            temp_visited[start[0]-1][start[1]] = True
            q.append([[start[0]-1, start[1]], goal,
                     temp_visited, num_moves + 1])
    print("total solutions: ", q_total_sol)


visited[0][0] = True
q.append([[0, 0], [4, 4], visited, 0])
maze_dfs_stack()
