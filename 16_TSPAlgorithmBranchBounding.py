import heapq

def tsp_branch_and_bound(graph):
    num_cities = len(graph)
    
    # Priority queue to store (cost, path, visited_mask)
    # Cost is the lower bound of the path
    pq = []
    
    # Initial state: start from city 0
    # (cost, current_path, visited_mask)
    # current_path is a list of cities visited so far
    # visited_mask is a bitmask to keep track of visited cities
    
    # Calculate initial lower bound (sum of minimum outgoing edges from each city)
    initial_lower_bound = 0
    for i in range(num_cities):
        min_edge = float('inf')
        for j in range(num_cities):
            if i != j:
                min_edge = min(min_edge, graph[i][j])
        initial_lower_bound += min_edge

    # Add the starting node to the priority queue
    # (lower_bound, current_city, path_list, visited_mask)
    heapq.heappush(pq, (initial_lower_bound, 0, [0], 1 << 0))
    
    min_cost = float('inf')
    best_path = []

    while pq:
        lower_bound, current_city, path, visited_mask = heapq.heappop(pq)

        # If all cities are visited
        if len(path) == num_cities:
            # Add the cost to return to the starting city
            current_total_cost = sum(graph[path[i]][path[i+1]] for i in range(num_cities - 1)) + graph[path[-1]][path[0]]
            
            if current_total_cost < min_cost:
                min_cost = current_total_cost
                best_path = path + [path[0]] # Add starting city to complete the cycle
            continue

        # If current lower bound is already greater than or equal to the best found cost, prune
        if lower_bound >= min_cost:
            continue

        # Explore neighbors
        for next_city in range(num_cities):
            if not (visited_mask &(1 << next_city)): # If next_city has not been visited
                new_visited_mask = visited_mask | (1 << next_city)
                new_path = path + [next_city]
                
                # Calculate new lower bound
                # This is a simplified lower bound calculation.
                # A more sophisticated one would involve minimum spanning trees or assignment problems.
                # For simplicity, we'll just add the cost of the new edge to the current lower bound.
                # This is not strictly correct for a tight lower bound but serves as an example.
                
                # A better lower bound for the remaining path could be calculated here.
                # For this example, we'll use a simple heuristic:
                # current path cost + minimum outgoing edge from next_city to an unvisited city
                
                current_path_cost = sum(graph[new_path[i]][new_path[i+1]] for i in range(len(new_path) - 1))
                
                remaining_lower_bound = 0
                unvisited_cities = []
                for i in range(num_cities):
                    if not (new_visited_mask & (1 << i)):
                        unvisited_cities.append(i)
                
                if unvisited_cities:
                    # Find minimum outgoing edge from each unvisited city
                    for city_u in unvisited_cities:
                        min_out_edge = float('inf')
                        for city_v in range(num_cities):
                            if city_u != city_v and not (new_visited_mask & (1 << city_v)):
                                min_out_edge = min(min_out_edge, graph[city_u][city_v])
                        if min_out_edge != float('inf'):
                            remaining_lower_bound += min_out_edge
                
                # The lower bound should also include the cost to return to the start from the last unvisited city
                # This is a very simplified lower bound. For a true B&B, you'd need a more robust calculation.
                # For now, let's just use the current path cost as a base for the lower bound.
                new_lower_bound = current_path_cost + remaining_lower_bound

                heapq.heappush(pq, (new_lower_bound, next_city, new_path, new_visited_mask))