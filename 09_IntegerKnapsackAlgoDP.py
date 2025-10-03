# ---------------------- 0/1 Knapsack using Dynamic Programming ----------------------
def knapsack_01(weights, values, capacity):
    n = len(weights)

    # DP Table: K[i][w] will store the maximum value
    # that can be attained with items 0..i and capacity w
    K = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build DP table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # If current item can fit in knapsack
            if weights[i - 1] <= w:
                # Option 1: Include this item -> values[i-1] + value of remaining capacity
                include = values[i - 1] + K[i - 1][w - weights[i - 1]]

                # Option 2: Exclude this item -> value remains same as previous row
                exclude = K[i - 1][w]

                # Take max of including or excluding item
                K[i][w] = max(include, exclude)
            else:
                # Item cannot fit, so take previous row's value
                K[i][w] = K[i - 1][w]

    # Final answer is stored at bottom-right corner of DP table
    return K[n][capacity]


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

# Dynamic Programming based 0/1 Knapsack
print("\n1. 0/1 Knapsack (DP Approach):")
max_value_01 = knapsack_01(weights, values, capacity)
print("Maximum value (0/1 Knapsack):", max_value_01)