Pos = tuple


class Node:
    def __init__(self, state, parent, path_cost, f):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.f = f


class MinHeap:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, node):
        self.data.append(node)
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.data) - 1)
        node = self.data.pop()
        self._heapify_down(0)
        return node

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.data[i].f < self.data[parent].f:
            self._swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < len(self.data) and self.data[left].f < self.data[smallest].f:
            smallest = left
        if right < len(self.data) and self.data[right].f < self.data[smallest].f:
            smallest = right

        if smallest != i:
            self._swap(i, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]


def abs_value(p1: Pos, p2: Pos) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def print_path(node):
    if node is None:
        return
    print_path(node.parent)
    print(f"({node.state[0]},{node.state[1]})", end=" ")


def best_first_search(initial: Pos, goal: Pos):
    frontier = MinHeap()
    reached = {}

    start_node = Node(initial, None, 0, abs_value(initial, goal))
    frontier.push(start_node)
    reached[initial] = start_node

    while not frontier.is_empty():
        node = frontier.pop()

        if node.state == goal:
            print("Goal Reached! Total Steps:", node.path_cost)
            print("Evacuation Route:", end=" ")
            print_path(node)
            print()
            return

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for i in range(4):
            new_state = (node.state[0] + dr[i], node.state[1] + dc[i])

            if (
                0 <= new_state[0] < 5
                and 0 <= new_state[1] < 11
                and grid[new_state[0]][new_state[1]] == 0
            ):
                new_cost = node.path_cost + 1

                if new_state not in reached or new_cost < reached[new_state].path_cost:
                    child = Node(new_state, node, new_cost, abs_value(new_state, goal))
                    reached[new_state] = child
                    frontier.push(child)

    print("No path found to exit.")


if __name__ == "__main__":
    entry = (3, 1)
    exit = (1, 9)
    best_first_search(entry, exit)
