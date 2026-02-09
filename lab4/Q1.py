class Deque:
    def __init__(self):
        self.data = []
        self.front = 0

    def append(self, item):
        self.data.append(item)

    def popleft(self):
        item = self.data[self.front]
        self.front += 1
        return item

    def is_empty(self):
        return self.front >= len(self.data)


class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, priority, item):
        self.data.append((priority, item))
        self.data.sort(key=lambda x: x[0])

    def pop(self):
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0


cities = [
    "Chicago", "Indianapolis", "Detroit", "Cleveland", "Columbus",
    "Buffalo", "Pittsburgh", "Syracuse", "Baltimore",
    "Philadelphia", "New York", "Boston", "Providence", "Portland"
]

N = len(cities)
graph = [[0] * N for _ in range(N)]

def add_edge(a, b, cost):
    i, j = cities.index(a), cities.index(b)
    graph[i][j] = cost
    graph[j][i] = cost

edges = [
    ("Chicago","Indianapolis",182), ("Chicago","Detroit",283), ("Chicago","Cleveland",345),
    ("Indianapolis","Columbus",176),
    ("Detroit","Cleveland",169), ("Detroit","Buffalo",256),
    ("Cleveland","Buffalo",189), ("Cleveland","Pittsburgh",134), ("Cleveland","Columbus",144),
    ("Columbus","Pittsburgh",185),
    ("Buffalo","Pittsburgh",215), ("Buffalo","Syracuse",150),
    ("Pittsburgh","Baltimore",247), ("Pittsburgh","Philadelphia",305),
    ("Syracuse","Philadelphia",254), ("Syracuse","Boston",312),
    ("Baltimore","Philadelphia",101),
    ("Philadelphia","New York",97),
    ("New York","Providence",181), ("New York","Boston",215),
    ("Boston","Providence",50), ("Boston","Portland",107)
]

for e in edges:
    add_edge(*e)

heuristic = [0,180,280,340,400,500,450,600,520,510,560,700,650,780]


def bfs(start, goal):
    start, goal = cities.index(start), cities.index(goal)
    dq = Deque()
    dq.append((start, [start]))
    explored = 0

    while not dq.is_empty():
        node, path = dq.popleft()
        explored += 1

        if node == goal:
            return explored

        for n in range(N):
            if graph[node][n] != 0 and n not in path:
                dq.append((n, path + [n]))

    return explored


def dfs(start, goal):
    start, goal = cities.index(start), cities.index(goal)
    explored = 0

    def dfs_util(node, path):
        nonlocal explored
        explored += 1
        if node == goal:
            return
        for n in range(N):
            if graph[node][n] != 0 and n not in path:
                dfs_util(n, path + [n])

    dfs_util(start, [])
    return explored


def befs(start, goal):
    start, goal = cities.index(start), cities.index(goal)
    pq = PriorityQueue()
    pq.push(heuristic[start], (start, [start]))
    visited = set()
    explored = 0

    while not pq.is_empty():
        _, (node, path) = pq.pop()
        explored += 1

        if node == goal:
            print(path)
            return explored

        visited.add(node)

        for n in range(N):
            if graph[node][n] != 0 and n not in visited:
                pq.push(heuristic[n], (n, path + [n]))

    return explored


start_city = "Syracuse"
goal_city = "Chicago"

print("BFS explored paths:", bfs(start_city, goal_city))
print("DFS explored paths:", dfs(start_city, goal_city))
print("BEFS explored paths:", befs(start_city, goal_city))
