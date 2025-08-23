import sys

def tsp(graph, visited, current_pos, n, count, cost, start_pos, min_cost):
    if count == n and graph[current_pos][start_pos] > 0:
        min_cost[0] = min(min_cost[0], cost + graph[current_pos][start_pos])
        return

    for i in range(n):
        if not visited[i] and graph[current_pos][i] > 0:
            visited[i] = True
            tsp(graph, visited, i, n, count + 1, cost + graph[current_pos][i], start_pos, min_cost)
            visited[i] = False  # backtrack

def take_input_and_run_tsp():
    n = int(input("Enter the number of cities (vertices): "))
    print("Enter the cost adjacency matrix (use 0 if no direct path):")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print("Error: Row length must be equal to number of cities.")
            return
        graph.append(row)

    visited = [False] * n
    visited[0] = True
    min_cost = [sys.maxsize]
    tsp(graph, visited, 0, n, 1, 0, 0, min_cost)
    
    print(f"\nMinimum cost to complete TSP tour: {min_cost[0]}")

# Run
take_input_and_run_tsp()
