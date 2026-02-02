from collections import deque

def bfs_tree(graph, start):
    q = deque([start])
    visited = {start}
    parent = {start: None}
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)
    return order, parent

def dfs_tree(graph, start):
    visited = set()
    parent = {start: None}
    order = []

    def dfs(u):
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                parent[v] = u
                dfs(v)

    dfs(start)
    return order, parent

def print_tree(parent, id_to_name, title="Tree (child <- parent)"):
    print(f"\n{title}:")
  
    for child in parent.keys():
        par = parent[child]
        child_name = id_to_name[child]
        par_name = "None" if par is None else id_to_name[par]
        print(f"{child_name} <- {par_name}")



if __name__ == "__main__":
    id_to_name = {
    0:"Raj", 1:"Priya", 2:"Aarav", 3:"Sunil", 4:"Akash",
    5:"Neha_C", 6:"Neha_R", 7:"Sneha", 8:"Rahul", 9:"Maya",
    10:"Arjun_B", 11:"Pooja", 12:"Arjun_R"
    }
    graph = {
    0:  [3, 5],                # Raj -> Sunil, Neha_C
    1:  [0, 2, 4],             # Priya -> Raj, Aarav, Akash
    2:  [5, 12],               # Aarav -> Neha_C, Arjun_R

    3:  [0, 4, 7, 9],          # Sunil -> Raj, Akash, Sneha, Maya
    4:  [3, 1],                # Akash -> Sunil, Priya

    5:  [4, 0, 7],             # Neha_C -> Akash, Raj, Sneha
    6:  [1, 2, 5, 8],          # Neha_R -> Priya, Aarav, Neha_C, Rahul

    7:  [8, 5],                # Sneha -> Rahul, Neha_C
    8:  [7, 5, 6, 11, 12],     # Rahul -> Sneha, Neha_C, Neha_R, Pooja, Arjun_R

    9:  [10],                  # Maya -> Arjun_B
    10: [9, 11],               # Arjun_B -> Maya, Pooja
    11: [8, 10, 12],           # Pooja -> Rahul, Arjun_B, Arjun_R

    12: [6, 8]                 # Arjun_R -> Neha_R, Rahul
    }
    start_id = 0
    bfs_order, bfs_parent = bfs_tree(graph, start_id)
    dfs_order, dfs_parent = dfs_tree(graph, start_id)
    print("BFS Order:")
    print([id_to_name[i] for i in bfs_order])
    

    print_tree(bfs_parent, id_to_name, "BFS Parent Tree")
    # print("\nDFS Order:")
    # print([id_to_name[i] for i in dfs_order])
    # print_tree(dfs_parent, id_to_name, "DFS Parent Tree")
