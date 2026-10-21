import numpy as np

def input_matrix(rows : int) -> np.ndarray:
    choice = input("выберите способ заполнения матрицы (1. с клавиатуры; 2. случайные числа): ")
    
    if choice == "1":
        elements = [int(input(f"элемент {i//rows},{i%rows}: ")) for i in range(rows * rows)]
        return np.array(elements).reshape(rows, rows)
    
    low = int(input("введите нижнюю границу интервала: "))
    high = int(input("введите верхнюю границу интервала: "))
    return np.random.randint(low, high + 1, size=(rows, rows))

def main():
    print("лаб 3")
    rows = int(input("введите размер квадратной матрицы: "))
    if rows <= 0:
        return print("размер должен быть > 0")

    matrix = input_matrix(rows)
    print("\nначальная матрица:\n", matrix)


    zero_indices = np.where(matrix[0] == 0)[0]
    
    if zero_indices.size > 0:
        zero_col = zero_indices[0]
        print(f"\nноль найден в столбце {zero_col + 1}")
        if zero_col > 0:
            matrix[:, [0, zero_col]] = matrix[:, [zero_col, 0]]
            print(f"сменили местами столбец {zero_col + 1} и столбец 1:\n", matrix)
    else:
        print("\nв первой строке нет нулей")


    max_element = np.max(matrix[np.triu_indices(rows)])
    print(f"\nмаксимальный элем-т верхнего прав треуг: {max_element}")

if __name__ == "__main__":
    main()



'''import random

def input_matrix(rows : int):
    choice = input("выберите способ заполнения матрицы (1. с клавиатуры; 2. случайные числа): ")
    
    matrix = []

    if choice == "1":
        for i in range(rows):
            row = []
            for j in range(rows):
                element = int(input(f"введите элемент матрицы [{i}][{j}]: "))
                row.append(element)
            matrix.append(row)
    else:
        low = int(input("введите нижнюю границу интервала: "))
        high = int(input("введите верхнюю границу интервала: "))
        matrix = generate_random_matrix(rows, low, high)

    return matrix

def generate_random_matrix(rows : int, low : int, high : int) -> list[list[int]]:
    return [[random.randint(low, high) for _ in range(rows)] for _ in range(rows)]

def print_matrix(matrix : list[list[int]]):
    for row in matrix:
        print(" ".join(f"{val:4d}" for val in row))

def find_first_zero_in_first_row(matrix: list[list[int]]) -> int:
    first_row = matrix[0]
    for j in range(len(first_row)):
        if first_row[j] == 0:
            return j
    return -1

def swap_columns(matrix : list[list[int]], col1 : int, col2 : int):
    rows = len(matrix)
    for i in range(rows):
        matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

def find_max_in_upper_triangle(matrix : list[list[int]]) -> int:
    rows = len(matrix)
    max_val = matrix[0][0]

    for i in range(rows):
        for j in range(i, rows):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
    return max_val


def main():
    print("лаб 3")
    rows = int(input("введите размер квадратной матрицы: "))
    if rows <= 0:
        print("размер должен быть > 0")
        return

    matrix = input_matrix(rows)
    print("\nначальная матрица")
    print_matrix(matrix)

    zero_col = find_first_zero_in_first_row(matrix)

    if zero_col != -1:
        print(f"\nноль найден в столбце {zero_col + 1}")
        if zero_col == 0:
            print("ноль в первом столбце. перестановка не нужна")
        else:
            swap_columns(matrix, 0, zero_col)
            print(f"сменили местами столбец {zero_col + 1} и столбец 1")
            print_matrix(matrix)
    else:
        print("\nв первой строке нет нулей")

    max_element = find_max_in_upper_triangle(matrix)
    print(f"\nмаксимальный элем-т верхнего прав треуг: {max_element}")

main()'''
