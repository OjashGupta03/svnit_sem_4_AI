from collections import deque

goal = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def print_states_3x3(states):
    for idx, board in enumerate(states):
        print("state:", idx)
        for r in range(3):
            for c in range(3):
                print(board[r][c], end=" ")
            print()
        print()

def bfs(start_state, goal_state):
    explored = 0

    q = deque([start_state])
    parent = {start_state: None}  # visited + parent

    found = False

    while q:
        state = q.popleft()
        explored += 1  # count every expanded state

        if state == goal_state:
            depth = 0
            cur = state
            while parent[cur] is not None:
                depth += 1
                cur = parent[cur]
            print("Goal found at depth:", depth)
            found = True
            break

        x, y = find_blank(state)

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                # generate next state
                new_state = [list(row) for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                new_tuple = tuple(tuple(row) for row in new_state)

                if new_tuple not in parent:   # not visited
                    parent[new_tuple] = state
                    q.append(new_tuple)

    print("States explored by BFS:", explored)

    if not found:
        print("Goal not found (no solution).")
        return None

    # reconstruct shortest path
    path = []
    cur = goal_state
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

if __name__ == "__main__":
    start_state = (
        (7, 2, 4),
        (5, 0, 6),
        (8, 3, 1)
    )

    ans = bfs(start_state, goal)

    if ans is not None:
        print_states_3x3(ans)
