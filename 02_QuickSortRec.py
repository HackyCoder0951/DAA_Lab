def quick_sort_recursive(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)

def quick_sort_iterative(arr):
    size = len(arr)
    stack = [(0, size - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# ------------------- Input & Execution -------------------

n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

method = int(input("Choose sorting method:\n1. Recursive\n2. Iterative\nEnter choice (1/2): "))

if method == 1:
    quick_sort_recursive(arr, 0, n - 1)
    print("Sorted array using Recursive Quick Sort:")
    print(arr)

elif method == 2:
    quick_sort_iterative(arr)
    print("Sorted array using Iterative Quick Sort:")
    print(arr)

else:
    print("Invalid choice.")
