start =[3,3,0,0]
goal =[0,0,3,3]
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0
def valid(state):
    if state[1]>0 and state[0]>state[1]:
        return False
    if(state[3]>0 and state[2]>state[3]):
        return False
    if (state[0] < 0 or state[0] > 3 or
        state[1] < 0 or state[1] > 3 or
        state[2] < 0 or state[2] > 3 or
        state[3] < 0 or state[3] > 3):
        return False

    return True
def steps(state,boat):
    children = []
    moves=[(1,0),(0,1),(2,0),(0,2),(1,1)]
    for move in moves:
        if(boat=="left"):
            new_state = [state[0] - move[0], state[1] - move[1], state[2] + move[0], state[3] + move[1]]
        else:
            new_state = [state[0] + move[0], state[1] +move[1], state[2] -move[0], state[3] - move[1]]
        if valid(new_state):
            children.append(new_state)
    return children
def dls(limit):
    stack = Stack()
    stack.push((start, "left", 0))  
    visited = set()
    while not stack.is_empty():
        state, boat, depth = stack.pop()
        if depth > limit:
            continue
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        if state == goal:
            print("Goal reached!")
            return True
        for child in steps(state, boat):
            if tuple(child) not in visited:
                new_boat = "right" if boat == "left" else "left"
                stack.push((child, new_boat, depth + 1))
    return "cutoff"
print(dls(3))