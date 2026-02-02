from collections import deque


def swap(node, x, y, nx, ny):
    new_node = [row[:] for row in node]
    new_node[x][y], new_node[nx][ny] = new_node[nx][ny], new_node[x][y]
    return new_node

def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def encode(board):
    return tuple(tuple(r) for r in board)

def dfs_paths(start,goal):
    parent={encode(start):None}
    Encode={encode(start):start} # this is map the encoded part
    path=[encode(path)]
    def dfs(node,path):
        if node==goal:
            print(path)
            return
        x,y=find_zero(node)
        for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_node=swap(node,x,y,nx,ny)
                k=encode(new_node)
                if k not in parent:
                    parent[k] = encode(node)
                    Encode[k] = new_node
                    dfs(k,path+k)
    dfs(start)




