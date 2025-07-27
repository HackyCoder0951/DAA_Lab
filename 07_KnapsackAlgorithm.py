def knapsack_01(weights, values, capacity):
    n = len(weights)
    K = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table K[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + K[i - 1][w - weights[i - 1]]
                exclude = K[i - 1][w]
                K[i][w] = max(include, exclude)
            else:
                K[i][w] = K[i - 1][w]

    return K[n][capacity]


def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    value_per_weight = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    value_per_weight.sort(reverse=True)  # Sort by value/weight ratio

    total_value = 0.0
    for ratio, weight, value in value_per_weight:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break

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

print("\n1. 0/1 Knapsack (DP Approach):")
max_value_01 = knapsack_01(weights, values, capacity)
print("Maximum value (0/1 Knapsack):", max_value_01)

print("\n2. Fractional Knapsack (Greedy Approach):")
max_value_frac = fractional_knapsack(weights, values, capacity)
print("Maximum value (Fractional Knapsack):", round(max_value_frac, 2))
