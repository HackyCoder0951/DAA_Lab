# Core Strassen's Matrix Multiplication

def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def split_matrix(M):
    n = len(M)
    mid = n // 2
    return [row[:mid] for row in M[:mid]], [row[mid:] for row in M[:mid]], \
           [row[:mid] for row in M[mid:]], [row[mid:] for row in M[mid:]]

def join_quadrants(C11, C12, C21, C22):
    return [c11 + c12 for c11, c12 in zip(C11, C12)] + \
           [c21 + c22 for c21, c22 in zip(C21, C22)]

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

# Example usage
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = strassen(A, B)
print(C)
