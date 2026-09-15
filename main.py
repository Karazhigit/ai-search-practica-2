from collections import deque
import heapq


# =========================
# GRAPH
# =========================

graph = {
    "Gate": [("Library", 2), ("Cafe", 1), ("Hall", 4)],
    "Library": [("Classroom", 4), ("Study Zone", 2)],
    "Cafe": [("Study Zone", 5), ("Robotics Lab", 10)],
    "Hall": [("Classroom", 1), ("Robotics Lab", 6)],
    "Classroom": [("AI Lab", 8)],
    "Study Zone": [("Robotics Lab", 1), ("AI Lab", 10)],
    "Robotics Lab": [("AI Lab", 4)],
    "AI Lab": []
}

START = "Gate"
GOAL = "AI Lab"


# =========================
# PATH COST
# =========================

def path_cost(graph, path):
    total = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]

        for neighbour, cost in graph[current]:
            if neighbour == next_node:
                total += cost
                break

    return total


# =========================
# DFS
# =========================

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


# =========================
# BFS
# =========================

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    expanded = []

    while queue:
        node, path = queue.popleft()
        expanded.append(node)

        if node == goal:
            return path, expanded

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None, expanded


# =========================
# UCS
# =========================

def ucs(graph, start, goal):
    frontier = [(0, start, [start])]
    best_cost = {start: 0}
    expanded = []

    while frontier:
        g, node, path = heapq.heappop(frontier)

        if g != best_cost.get(node):
            continue

        expanded.append(node)

        if node == goal:
            return path, g, expanded

        for neighbour, step_cost in graph[node]:
            new_g = g + step_cost

            if new_g < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_g

                heapq.heappush(
                    frontier,
                    (new_g, neighbour, path + [neighbour])
                )

    return None, float("inf"), expanded


# =========================
# A*
# =========================

heuristic = {
    "Gate": 9,
    "Library": 7,
    "Cafe": 10,
    "Hall": 9,
    "Classroom": 8,
    "Study Zone": 5,
    "Robotics Lab": 4,
    "AI Lab": 0
}


def astar(graph, start, goal, h):
    frontier = [(h[start], 0, start, [start])]
    best_g = {start: 0}
    expanded = []

    while frontier:
        f, g, node, path = heapq.heappop(frontier)

        if g != best_g.get(node):
            continue

        expanded.append(node)

        if node == goal:
            return path, g, expanded

        for neighbour, step_cost in graph[node]:
            new_g = g + step_cost

            if new_g < best_g.get(neighbour, float("inf")):
                best_g[neighbour] = new_g

                new_f = new_g + h[neighbour]

                heapq.heappush(
                    frontier,
                    (new_f, new_g, neighbour, path + [neighbour])
                )

    return None, float("inf"), expanded


# =========================
# RESULTS
# =========================

dfs_path, dfs_expanded = dfs(graph, START, GOAL)
bfs_path, bfs_expanded = bfs(graph, START, GOAL)
ucs_path, ucs_cost, ucs_expanded = ucs(graph, START, GOAL)
astar_path, astar_cost, astar_expanded = astar(
    graph, START, GOAL, heuristic
)


print("===== DFS =====")
print("Path:", " -> ".join(dfs_path))
print("Cost:", path_cost(graph, dfs_path))
print("Expanded:", " -> ".join(dfs_expanded))


print("\n===== BFS =====")
print("Path:", " -> ".join(bfs_path))
print("Cost:", path_cost(graph, bfs_path))
print("Expanded:", " -> ".join(bfs_expanded))


print("\n===== UCS =====")
print("Path:", " -> ".join(ucs_path))
print("Cost:", ucs_cost)
print("Expanded:", " -> ".join(ucs_expanded))


print("\n===== A* =====")
print("Path:", " -> ".join(astar_path))
print("Cost:", astar_cost)
print("Expanded:", " -> ".join(astar_expanded))
