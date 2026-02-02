from collections import deque

def all_paths_bfs_with_expansion_cost(graph, start, goal):
    
    q = deque()
    q.append((start, [start], 0)) 

    res = []
    totalExpansionCost = 0

    while q:
        node, path, _ = q.popleft()

       
        for nxt, w in graph[node]:
            totalExpansionCost += w

        if node == goal:
            res.append((path, totalExpansionCost))
            continue

        for nxt, w in graph[node]:
            if nxt in path: 
                continue

            q.append((nxt, path + [nxt], totalExpansionCost))

    return res


def all_distances_dfs(graph, start, goal):
    
    res = []

    def dfs(node, total, path, visited):
        if node == goal:
            res.append((path[:], total))
            return

        for nxt, w in graph[node]:
            if nxt in visited:
                continue
            visited.add(nxt)
            path.append(nxt)
            dfs(nxt, total + w, path, visited)
            path.pop()
            visited.remove(nxt)

    dfs(start, 0, [start], {start})
    return res


if __name__ == "__main__":
    graph = {
        "Chicago": [("Detroit", 283), ("Cleveland", 345), ("Indianapolis", 182)],
        "Indianapolis": [("Chicago", 182), ("Columbus", 176)],
        "Columbus": [("Indianapolis", 176), ("Cleveland", 144), ("Pittsburgh", 185)],
        "Cleveland": [("Chicago", 345), ("Detroit", 169), ("Buffalo", 189), ("Pittsburgh", 134), ("Columbus", 144)],
        "Detroit": [("Chicago", 283), ("Cleveland", 169), ("Buffalo", 256)],
        "Buffalo": [("Detroit", 256), ("Cleveland", 189), ("Pittsburgh", 215), ("Syracuse", 150)],
        "Pittsburgh": [("Cleveland", 134), ("Columbus", 185), ("Buffalo", 215), ("Philadelphia", 305), ("Baltimore", 247)],
        "Syracuse": [("Buffalo", 150), ("Philadelphia", 253), ("New York", 254), ("Boston", 312)],
        "Baltimore": [("Pittsburgh", 247), ("Philadelphia", 101)],
        "Philadelphia": [("Baltimore", 101), ("New York", 97), ("Pittsburgh", 305), ("Syracuse", 253)],
        "New York": [("Philadelphia", 97), ("Boston", 215), ("Providence", 181), ("Syracuse", 254)],
        "Providence": [("New York", 181), ("Boston", 50)],
        "Boston": [("Syracuse", 312), ("New York", 215), ("Providence", 50), ("Portland", 107)],
        "Portland": [("Boston", 107)],
    }

    start_city = "Syracuse"
    end_city = "Chicago"

    print("--- BFS: All Paths + BFS Expansion Cost  ---")
    bfs_paths = all_paths_bfs_with_expansion_cost(graph, start_city, end_city)
    bfs_paths.sort(key=lambda x: len(x[0]))  
    for p, exp_cost in bfs_paths:
        print(f"Cost (BFS expansion cost): {exp_cost} | Path: {' -> '.join(p)}")

    print("\n--- DFS: All Paths + Normal Path Cost ---")
    dfs_paths = all_distances_dfs(graph, start_city, end_city)
    dfs_paths.sort(key=lambda x: len(x[0]))
    for p, dist in dfs_paths:
        print(f"Cost: {dist} | Path: {' -> '.join(p)}")
