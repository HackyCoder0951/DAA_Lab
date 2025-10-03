import sys

def tsp_dp(graph):
    n = len(graph)
    
    # dp[mask][i] will be the minimum cost to visit all cities in 'mask'
    # ending at city 'i'.
    # Initialize with infinity
    dp = [[sys.maxsize for _ in range(n)] for _ in range(1 << n)]
    
    # Base case: starting at city 0, cost to visit only city 0 is 0
    dp[1 << 0][0] = 0
    
    # Iterate over all possible masks (subsets of cities)
    for mask in range(1, 1 << n):
        for u in range(n):
            # If city u is in the current mask
            if (mask >> u) & 1:
                # If dp[mask][u] is still infinity, it means we haven't found a path to u yet
                if dp[mask][u] == sys.maxsize:
                    continue
                
                # Try to extend the path to an unvisited city v
                for v in range(n):
                    # If v is not in the current mask and there's a path from u to v
                    if not ((mask >> v) & 1) and graph[u][v] > 0:
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + graph[u][v])
                        
    # After filling the DP table, find the minimum cost to return to the starting city (city 0)
    # from any city, having visited all cities.
    min_tour_cost = sys.maxsize
    final_mask = (1 << n) - 1 # Mask where all cities are visited
    
    for u in range(n):
        if graph[u][0] > 0: # Check if there's a path from u back to city 0
            min_tour_cost = min(min_tour_cost, dp[final_mask][u] + graph[u][0])
            
    return min_tour_cost

def take_input_and_run_tsp_dp():
    n = int(input("Enter the number of cities (vertices): "))
    print("Enter the cost adjacency matrix (use 0 if no direct path):")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print("Error: Row length must be equal to number of cities.")
            return
        graph.append(row)

    min_cost = tsp_dp(graph)
    print(f"\nMinimum cost to complete TSP tour (DP): {min_cost}")


# Run
take_input_and_run_tsp_dp()