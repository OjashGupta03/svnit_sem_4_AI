from collections import deque

def swap(node, x, y, nx, ny):
    new_node = [row[:] for row in node]
    new_node[x][y], new_node[nx][ny] = new_node[nx][ny], new_node[x][y]
    return new_node

def encode(board):
    return tuple(tuple(r) for r in board)

def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def bfs_shortest_path(start, goal):
    q = deque([start])
    parent = {encode(start): None}          # visited + parent
    board_map = {encode(start): start}      # key -> board

    while q:
        node = q.popleft()
        if node == goal:
            break

        x, y = find_zero(node)
        for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_node = swap(node, x, y, nx, ny)
                k = encode(new_node)
                if k not in parent:
                    parent[k] = encode(node)
                    board_map[k] = new_node
                    q.append(new_node)

    goal_key = encode(goal)
    if goal_key not in parent:
        return None

    # reconstruct path
    path = []
    cur = goal_key
    while cur is not None:
        path.append(board_map[cur])
        cur = parent[cur]
    path.reverse()
    return path

    # all possible states
    # path=[]
    # for i in parent:
    #     path.append(i)
    # return path

def print_states_3x3(states):
    state=0
    for board in states:
        print("state:",state)
        for r in range(3):
            for c in range(3):
                print(board[r][c], end=" ")
            print()
        print() 
        state+=1

if __name__ == "__main__":
    goal  = [[0,1,2],[3,4,5],[6,7,8]]
    start = [[7,2,4],[5,0,6],[8,3,1]]
    states=0

    ans = bfs_shortest_path(start, goal)
    if ans is None:
        print("No solution found")
    else:
        print_states_3x3(ans)
