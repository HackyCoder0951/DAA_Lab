INF = float('inf')

def prims_algorithm(graph, n):
    selected = [False] * n
    key = [INF] * n
    parent = [-1] * n

    key[0] = 0  # Start from the first vertex

    for _ in range(n):
        min_key = INF
        u = -1
        for v in range(n):
            if not selected[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        selected[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("\nMinimum Spanning Tree (MST) Edges and Weights:")
    total_cost = 0
    for i in range(1, n):
        print(f"{parent[i]} - {i} \tWeight: {graph[i][parent[i]]}")
        total_cost += graph[i][parent[i]]

    print(f"Total cost of MST: {total_cost}")

def take_input():
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency matrix (use 0 for no connection):")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print("Error: Row length must match number of vertices.")
            return
        graph.append(row)

    prims_algorithm(graph, n)

# Run
take_input()
