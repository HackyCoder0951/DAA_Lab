# Matrix addition
def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

# Matrix subtraction
def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

# Split a matrix into 4 equal submatrices
def split_matrix(M):
    n = len(M)
    mid = n // 2
    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]
    return A11, A12, A21, A22

# Combine 4 submatrices into one
def join_quadrants(C11, C12, C21, C22):
    top = [c11 + c12 for c11, c12 in zip(C11, C12)]
    bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
    return top + bottom

# Strassen's recursive multiplication
def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]
    

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, sub_matrix(B12, B22))
    M4 = strassen(A22, sub_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)

    return join_quadrants(C11, C12, C21, C22)

# Pad matrix to next power of 2
def pad_matrix(M):
    n = len(M)
    m = 1
    while m < n:
        m *= 2
    padded = [[0]*m for _ in range(m)]
    for i in range(n):
        for j in range(n):
            padded[i][j] = M[i][j]
    return padded, n

# Crop matrix back to original size
def crop_matrix(M, size):
    return [row[:size] for row in M[:size]]

# Read matrix from user with input validation
def read_matrix(name):
    try:
        n = int(input(f"\nEnter the size of square matrix {name} (n x n): "))
        if n <= 0:
            raise ValueError("Matrix size must be a positive integer.")
        matrix = []
        print(f"Enter the elements of matrix {name} row by row (space-separated):")
        for i in range(n):
            row = input(f"Row {i+1}: ").strip().split()
            if len(row) != n:
                raise ValueError(f"Each row must have exactly {n} elements.")
            matrix.append([int(x) for x in row])
        return matrix
    except ValueError as e:
        print("Input Error:", e)
        return None

# Main program with full exception handling
def main():
    print(" Strassen's Matrix Multiplication ")

    A = read_matrix("A")
    if A is None:
        return
    B = read_matrix("B")
    if B is None:
        return

    # Check if both matrices are square and same size
    try:
        if len(A) != len(B):
            raise ValueError("Matrices A and B must be of the same size.")

        if any(len(row) != len(A) for row in A + B):
            raise ValueError("All rows must have the same number of elements (square matrices only).")

        # Pad matrices to next power of 2
        A_pad, orig_size = pad_matrix(A)
        B_pad, _ = pad_matrix(B)

        # Perform Strassen multiplication
        C_pad = strassen(A_pad, B_pad)

        # Crop to original size
        C = crop_matrix(C_pad, orig_size)

        # Output result
        print("\n Resultant Matrix C = A x B:")
        for row in C:
            print(" ".join(map(str, row)))

    except Exception as e:
        print("Error:", e)

# Run the program
if __name__ == "__main__":
    main()
