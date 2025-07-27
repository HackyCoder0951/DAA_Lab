def merge(left, right):
    result = []
    i = j = 0

    # Compare elements and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    return merge(left, right)

def merge_sort_iterative(arr):
    width = 1
    n = len(arr)

    while width < n:
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)

            # Merge arr[left:mid] and arr[mid:right]
            left_part = arr[left:mid]
            right_part = arr[mid:right]
            merged = merge(left_part, right_part)

            # Replace in original array
            arr[left:right] = merged

        width *= 2
    return arr

# ----------- Main Program ------------
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

print("\nChoose sorting method:")
print("1. Recursive Merge Sort")
print("2. Iterative Merge Sort")
method = int(input("Enter method (1 or 2): "))

if method == 1:
    result = merge_sort_recursive(arr)
    print("Sorted array using Recursive Merge Sort:", result)
elif method == 2:
    result = merge_sort_iterative(arr)
    print("Sorted array using Iterative Merge Sort:", result)
else:
    print("Invalid method selected.")
