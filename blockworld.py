from collections import deque
import copy

# Function to check if goal state is reached
def is_goal(state, goal):
    return state == goal

# Function to generate possible moves
def get_neighbors(state):
    neighbors = []
    blocks = list(state.keys())

    for block in blocks:
        if state[block] != "clear":
            continue

        # Move block to table
        new_state = copy.deepcopy(state)
        new_state[block] = "table"
        neighbors.append(new_state)

        # Move block onto another clear block
        for target in blocks:
            if target != block and state[target] == "clear":
                new_state = copy.deepcopy(state)
                new_state[block] = target
                neighbors.append(new_state)

    return neighbors

# BFS Algorithm
def bfs(initial, goal):
    visited = []
    queue = deque([(initial, [])])

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.append(state)

        if is_goal(state, goal):
            return path + [state]

        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))

    return None


# Initial and Goal States
initial_state = {
    "A": "table",
    "B": "table",
    "C": "A"
}

goal_state = {
    "A": "B",
    "B": "C",
    "C": "table"
}

solution = bfs(initial_state, goal_state)

if solution:
    print("Solution Found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
