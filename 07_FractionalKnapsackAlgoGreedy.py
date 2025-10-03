# ---------------------- Fractional Knapsack using Greedy ----------------------
def fractional_knapsack(weights, values, capacity):
    n = len(weights)

    # Compute value-to-weight ratio for each item
    # Store tuple (ratio, weight, value)
    value_per_weight = [
        (values[i] / weights[i], weights[i], values[i]) for i in range(n)]

    # Greedy Step: Sort items by decreasing ratio (value/weight)
    value_per_weight.sort(reverse=True)

    total_value = 0.0
    for ratio, weight, value in value_per_weight:

        # If item can fully fit, take it all
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            # If only part can fit, take fraction of it
            total_value += ratio * capacity
            break   # capacity full

    return total_value


# ---------------------- Input Section ----------------------
print("Enter number of items:")
n = int(input())

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
print("\n=== Results ===")

# Greedy based Fractional Knapsack
print("\n2. Fractional Knapsack (Greedy Approach):")
max_value_frac = fractional_knapsack(weights, values, capacity)
print("Maximum value (Fractional Knapsack):", round(max_value_frac, 2))
