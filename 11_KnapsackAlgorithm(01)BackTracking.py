# 0/1 Knapsack using Backtracking
def knapsack_backtracking(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_items = []

    def backtrack(index, current_weight, current_value, current_items):
        nonlocal max_value, best_items

        # Base case: if all items are considered
        if index == n:
            if current_value > max_value:
                max_value = current_value
                best_items = list(current_items)
            return

        # Case 1: Include the current item if it fits
        if current_weight + weights[index] <= capacity:
            current_items.append(index)
            backtrack(index + 1,
                      current_weight + weights[index],
                      current_value + values[index],
                      current_items)
            current_items.pop()  # Backtrack

        # Case 2: Exclude the current item
        backtrack(index + 1, current_weight, current_value, current_items)

    backtrack(0, 0, 0, [])
    return max_value, best_items


# # Fractional Knapsack is not suitable for backtracking;
# # Greedy is always optimal for fractional case.
# def knapsack_fractional_greedy(weights, values, capacity):
#     items = sorted([(values[i] / weights[i], weights[i], values[i], i)
#                    for i in range(len(weights))], reverse=True)

#     total_value = 0
#     current_weight = 0
#     selected_items = []

#     for ratio, weight, value, original_index in items:
#         if current_weight + weight <= capacity:
#             current_weight += weight
#             total_value += value
#             selected_items.append((original_index, 1.0))  # full item
#         else:
#             remaining_capacity = capacity - current_weight
#             fraction = remaining_capacity / weight
#             total_value += value * fraction
#             selected_items.append((original_index, fraction))  # fractional item
#             break

#     return total_value, selected_items


# ---------------------- Input Section ----------------------
print("=== Knapsack using Backtracking (0/1) ===")
n = int(input("Enter number of items: "))

weights = []
values = []

print("Enter weight and value for each item:")
for i in range(n):
    w = int(input(f"Weight of item {i+1}: "))
    v = int(input(f"Value of item {i+1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter knapsack capacity: "))

# ---------------------- Output Section ----------------------
# 0/1 Knapsack Backtracking
max_value_bt, best_items_bt = knapsack_backtracking(weights, values, capacity)
print("\n0/1 Knapsack (Backtracking):")
print("Maximum value:", max_value_bt)
print("Items taken (indices):", best_items_bt)

# Fractional Knapsack (Greedy approach note)
# max_value_frac, selected_frac = knapsack_fractional_greedy(weights, values, capacity)
# print("\nFractional Knapsack (Greedy, since backtracking not efficient):")
# print("Maximum value:", round(max_value_frac, 2))
# print("Items taken (index, fraction):", selected_frac)


# === Knapsack using Backtracking (0/1) ===
# Enter number of items: 4
# Enter weight and value for each item:
# Weight of item 1: 2
# Value of item 1: 10
# Weight of item 2: 4
# Value of item 2: 10
# Weight of item 3: 6
# Value of item 3: 12
# Weight of item 4: 9
# Value of item 4: 18
# Enter knapsack capacity: 15