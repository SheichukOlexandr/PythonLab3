def is_symmetric_sequence(sequence):
    return sequence == sequence[::-1]

def find_symmetric_rows(matrix):
    symmetric_rows = []
    for i, row in enumerate(matrix):
        if is_symmetric_sequence(row):
            symmetric_rows.append(i)
    return symmetric_rows

def print_vector(vector):
    for i in range(0, len(vector), 7):
        print(*vector[i:i+7])


A = [
    [1, 2, 3, 3, 2, 1],
    [1, 2, 3, 5, 3, 2, 1],
    [1, 2, 3, 4, 3, 2, 1],
    [1, 2, 3, 3, 2, 1],
    [1, 2, 3, 5, 3, 2, 1],
    [1, 2, 1, 2, 1, 2]
]


symmetric_rows = find_symmetric_rows(A)
print("Симетричні рядки матриці A:", symmetric_rows)

# Побудова вектора B з номерів симетричних рядків
B = symmetric_rows
print("Вектор B:", B)

print("Вектор B по 7 елементів у рядку:")
print_vector(B)
