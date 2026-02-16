"""
3 girls and 3 boys river crossing.
State = (lg, lb, boat)
boat: 0 = LEFT, 1 = RIGHT
Totals: girls=3, boys=3
Rule: on each bank, if girls > 0 then girls >= boys
"""

def check_state(lg, lb):
    if lg < 0 or lb < 0 or lg > 3 or lb > 3:
        return False
    rg = 3 - lg
    rb = 3 - lb
    # left bank safety
    if lg > 0 and lg < lb:
        return False

    # right bank safety
    if rg > 0 and rg < rb:
        return False

    return True


def change(t):
    lg, lb, boat = t

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    res = []
    for g, b in moves:
        if boat == 0:  # boat on LEFT 
            x=(lg - g, lb - b, 1)
        else:          # boat on RIGHT 
            x=(lg + g, lb + b, 0)
        if check_state(x[0],x[1]):
            res.append(x)
    return res


def depthfs(initial, goal, limit):
    parent = {initial: None}

    def dfs(node, d):
        if node == goal:
            return True
        if d == limit:
            return False

        for nxt in change(node):
            
            if (nxt in parent):
                continue

            parent[nxt] = node

            
            if dfs(nxt, d + 1):
                return True

        return False

    found = dfs(initial, 0)
    return parent, found


def reconstruct_path(parent, goal):
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path


def iterative_deepening_search(initial, goal, max_limit=50):
    total_explored = 0
    
    for limit in range(max_limit + 1):
        parent, found = depthfs(initial, goal, limit)
        total_explored += len(parent)

        if found:
            return parent, limit, total_explored

    return None, None, total_explored
1

if __name__ == "__main__":
    initial = (3, 3, 0)
    goal = (0, 0, 1)

    parent, found = depthfs(initial, goal, limit=14)
    print("DLS (limit=3):")
    if not found:
        print("No solution found within depth limit 3.")
        print("States explored:", len(parent))
    else:
        path = reconstruct_path(parent, goal)
        print("Solution path:")
        for step in path:
            print(step)
        print("States explored:", len(parent))
        print("Path length:", len(path) - 1)

    print("\nIDS:")
    parent, best_limit, total_explored = iterative_deepening_search(initial, goal, max_limit=50)
    if parent is None:
        print("No solution found up to max_limit.")
        print("Total states explored:", total_explored)
    else:
        path = reconstruct_path(parent, goal)
        print("Found at depth limit:", best_limit)
        print("Solution path:")
        for step in path:
            print(step)
        print("States explored in final iteration:", len(parent))
        print("Total states explored across all IDS iterations:", total_explored)
        print("Path length:", len(path) - 1)
