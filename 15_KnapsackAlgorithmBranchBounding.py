import heapq 

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsack_branch_and_bound(items, capacity):
    n = len(items)
    items.sort(key=lambda x: x.ratio, reverse=True)

    max_profit = 0
    
    # Priority queue stores tuples: (-upper_bound, current_weight, current_value, item_index)
    # We use negative upper_bound to make it a min-heap for max-profit
    pq = [(-calculate_bound(0, 0, 0, items, capacity), 0, 0, 0)] # (bound, current_weight, current_value, item_index)

    while pq:
        bound, current_weight, current_value, item_index = heapq.heappop(pq)
        bound = -bound # Convert back to positive bound

        if bound < max_profit:
            continue

        if item_index == n:
            max_profit = max(max_profit, current_value)
            continue

        # Include the current item
        if current_weight + items[item_index].weight <= capacity:
            new_weight = current_weight + items[item_index].weight
            new_value = current_value + items[item_index].value
            new_bound = calculate_bound(new_weight, new_value, item_index + 1, items, capacity)
            if new_bound > max_profit:
                heapq.heappush(pq, (-new_bound, new_weight, new_value, item_index + 1))
            max_profit = max(max_profit, new_value) # Update max_profit if this path is better

        # Exclude the current item
        new_bound = calculate_bound(current_weight, current_value, item_index + 1, items, capacity)
        if new_bound > max_profit:
            heapq.heappush(pq, (-new_bound, current_weight, current_value, item_index + 1))

    return max_profit

def calculate_bound(current_weight, current_value, item_index, items, capacity):
    n = len(items)
    if current_weight >= capacity:
        return current_value
    bound = current_value
    total_weight = current_weight
    for i in range(item_index, n):
        if total_weight + items[i].weight <= capacity:
            total_weight += items[i].weight
            bound += items[i].value
        else:
            remain = capacity - total_weight
            bound += items[i].ratio * remain
            break
    return bound

# ---------------------- Input Section ----------------------
print("=== 0/1 Knapsack using Branch and Bound ===")
n = int(input("Enter number of items: "))

weights = []
values = []
items = []

print("Enter weight and value for each item:")
for i in range(n):
    w = int(input(f"Weight of item {i+1}: "))
    v = int(input(f"Value of item {i+1}: "))
    weights.append(w)
    values.append(v)
    items.append(Item(w, v))

capacity = int(input("Enter knapsack capacity: "))

# ---------------------- Output Section ----------------------
# 0/1 Knapsack Branch and Bound
max_value_bnb = knapsack_branch_and_bound(items, capacity)
print("\n0/1 Knapsack (Branch and Bound):")
print("Maximum value:", max_value_bnb)
