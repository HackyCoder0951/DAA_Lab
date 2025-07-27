# Iterative Linear Search
def linear_search_iterative(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Recursive Linear Search
def linear_search_recursive(arr, key, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == key:
        return index
    return linear_search_recursive(arr, key, index + 1)

# Iterative Binary Search
def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Recursive Binary Search
def binary_search_recursive(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, high)
    else:
        return binary_search_recursive(arr, key, low, mid - 1)

# Main Menu-Driven Program
def main():
    arr = []
    print("Enter the number of elements:")
    n = int(input())

    print(f"Enter {n} elements:")
    for _ in range(n):
        arr.append(int(input()))

    while True:
        print("\nMENU:")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1 or choice == 2:
            print("Choose Method:")
            print("1. Iterative")
            print("2. Recursive")
            method = int(input("Enter method: "))

            key = int(input("Enter the element to search: "))

            if choice == 1:
                if method == 1:
                    index = linear_search_iterative(arr, key)
                else:
                    index = linear_search_recursive(arr, key)

            elif choice == 2:
                arr.sort()
                print(f"Sorted Array: {arr}")
                if method == 1:
                    index = binary_search_iterative(arr, key)
                else:
                    index = binary_search_recursive(arr, key, 0, len(arr) - 1)

            if index != -1:
                print(f"Element found at index {index}")
            else:
                print("Element not found.")

        elif choice == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main()
