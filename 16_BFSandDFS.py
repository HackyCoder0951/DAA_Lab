from collections import deque

# BFS Implementation
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            queue.extend(graph[node])  # Add all neighbors
    return bfs_order


# DFS Implementation (Recursive)
def dfs_recursive(graph, node, visited=None, dfs_order=None):
    if visited is None:
        visited = set()
    if dfs_order is None:
        dfs_order = []

    visited.add(node)
    dfs_order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, dfs_order)

    return dfs_order


# DFS Implementation (Iterative using stack)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    dfs_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            dfs_order.append(node)
            stack.extend(reversed(graph[node]))  # reverse for proper order
    return dfs_order


# ---------------------------
# User Input Section
# ---------------------------
if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    graph = {}

    for i in range(n):
        vertex = input(f"Enter vertex {i+1} name: ")
        neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").split()
        graph[vertex] = neighbors

    start = input("Enter start vertex: ")

    print("\nGraph:", graph)
    print("BFS Traversal:", bfs(graph, start))
    print("DFS Traversal (Recursive):", dfs_recursive(graph, start))
    print("DFS Traversal (Iterative):", dfs_iterative(graph, start))
