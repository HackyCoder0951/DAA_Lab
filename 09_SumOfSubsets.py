from collections import deque
from itertools import chain, combinations

def sum_of_subsets_iterative(weights, target_sum):
    n = len(weights)
    weights.sort()
    queue = deque()
    queue.append((0, 0, []))  # (index, current_sum, current_subset)

    found = False
    while queue:
        i, current_sum, subset = queue.popleft()
        if current_sum == target_sum:
            print("Subset found:", subset)
            found = True
            continue
        if i >= n or current_sum > target_sum:
            continue

        # Include weights[i]
        queue.append((i + 1, current_sum + weights[i], subset + [weights[i]]))
        # Exclude weights[i]
        queue.append((i + 1, current_sum, subset))
    if not found:
        print("No subset found.")

# === Main Program ===
weights = list(map(int, input("Enter the set of weights (space separated): ").split()))
target_sum = int(input("Enter the target sum: "))
def all_subsets(weights):
    subsets = list(chain.from_iterable(combinations(weights, r) for r in range(len(weights)+1)))
    print("All subsets:")
    for subset in subsets:
        print(list(subset))

all_subsets(weights)
print("\nSubsets whose sum is", target_sum, ":")
sum_of_subsets_iterative(weights, target_sum)