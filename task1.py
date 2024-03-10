def is_symmetric_sequence(sequence):
    n = len(sequence)
    for i in range(n // 2):
        if sequence[i] != sequence[n - i - 1]:
            return False
    return True

def build_B_matrix(A):
    B = []
    n = len(A)
    for i in range(n):
        if is_symmetric_sequence(A[i]):
            B.append(i)
    return B

def print_vector(vector, per_row=7):
    for i, element in enumerate(vector, 1):
        print(element, end=' ')
        if i % per_row == 0:
            print()

# Приклад вхідної матриці
A = [
    [1, 2, 3, 3, 2, 1],
    [1, 2, 3, 5, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [1, 1, 1, 1, 1]
]

B = build_B_matrix(A)
print_vector(B)
