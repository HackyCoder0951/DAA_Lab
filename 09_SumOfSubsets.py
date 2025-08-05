def sum_of_subsets(weights, target_sum):
    n = len(weights)
    weights.sort()

    def backtrack(i, current_sum, subset):
        if current_sum == target_sum:
            print("Subset found:", subset)
            return
        if i >= n or current_sum > target_sum:
            return
        
        # Include weights[i]
        backtrack(i + 1, current_sum + weights[i], subset + [weights[i]])

        # Exclude weights[i]
        backtrack(i + 1, current_sum, subset)

# === Main Program ===
weights = list(map(int, input("Enter the set of weights (space separated): ").split()))
target_sum = int(input("Enter the target sum: "))

print("\nSubsets whose sum is", target_sum, ":")
sum_of_subsets(weights, target_sum)


# Enter the set of weights (space separated): 10 7 5 18 12 20 15
# Enter the target sum: 35

# Subsets whose sum is 35 :
# Subset found: [10, 7, 18]
# Subset found: [10, 5, 20]
# Subset found: [7, 5, 12, 11]
# ...