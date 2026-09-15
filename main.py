graph = {
    "Gate": [("Library", 2), ("Cafe", 1), ("Hall", 4)],
    "Library": [("Classroom", 4), ("Study Zone", 2)],
    "Cafe": [("Study Zone", 5), ("Robotics Lab", 2)],
    "Hall": [("Classroom", 1), ("Robotics Lab", 6)],
    "Classroom": [("AI Lab", 8)],
    "Study Zone": [("Robotics Lab", 1), ("AI Lab", 5)],
    "Robotics Lab": [("AI Lab", 4)],
    "AI Lab": []
}

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    expanded = []

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        expanded.append(node)

        if node == goal:
            return path, expanded

        for neighbour, cost in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))

    return None, expanded
