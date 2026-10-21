import random
import numpy as np

MAX_SIZE = 100

def input_size() -> int:
    while True:
        try:
            n = int(input(f"введите кол-во эл-тов (от 1 до {MAX_SIZE}): "))
            if 1 <= n <= MAX_SIZE:
                return n
            print(f"число должно быть от 1 до {MAX_SIZE}")
        except ValueError:
            print("нужно целое число")

def fill_array(arr: np.ndarray, n: int):
    choice = input("выберите способ заполнения (1. с клавиатуры; 2. случайные числа): ")
    
    if choice == "1":
        for i in range(n):
            while True:
                try:
                    arr[i] = int(input(f"введите эл-т [{i}]: "))
                    break
                except ValueError:
                    print("нужно целое число")
    else:
        while True:
            try:
                low = int(input("введите нижнюю границу интервала: "))
                high = int(input("введите верхнюю границу интервала: "))
                if low > high:
                    low, high = high, low
                break
            except ValueError:
                print("нужны целые числа")
                
        arr[:n] = np.random.randint(low, high + 1, size=n)

def print_array(arr: np.ndarray, n: int):
    print(" ".join(map(str, arr[:n])))

def count_even_indices(arr: np.ndarray, n: int):
    product = np.prod(arr[0:n:2])
    print(f"произведение эл-тов с чет индексами: {product}")

def count_sum_between_zeros(arr: np.ndarray, n: int):
    working_arr = arr[:n]
    zero_indices = np.where(working_arr == 0)[0]
    
    if zero_indices.size == 0:
        print("нет нулей")
    elif zero_indices.size == 1:
        print("одного нуля мало")
    else:
        first_zero = zero_indices[0]
        last_zero = zero_indices[-1]
        
        _sum = np.sum(working_arr[first_zero + 1 : last_zero])
        print(f"сумма эл-тов между нулями: {_sum}")

def transform_array(arr: np.ndarray, n: int):
    temp_arr = arr[:n]
    
    negatives = temp_arr[temp_arr < 0]
    positives = temp_arr[temp_arr >= 0]
    
    arr[:n] = np.concatenate([negatives, positives])

def fill_darray(n: int) -> np.ndarray:
    dynamic_arr = np.zeros(n, dtype=int)
    fill_array(dynamic_arr, n)
    return dynamic_arr


def main():
    print("статический массив")
    static_arr = np.zeros(MAX_SIZE, dtype=int)
    
    n = input_size()
    fill_array(static_arr, n)
    print("начальный массив")
    print_array(static_arr, n)
    
    count_even_indices(static_arr, n)
    count_sum_between_zeros(static_arr, n)
    transform_array(static_arr, n)
    print("измененный массив")
    print_array(static_arr, n)


    print("динамический массив")
    n = input_size()
    dynamic_arr = fill_darray(n)
    _len = len(dynamic_arr)
    print("начальный массив")
    print_array(dynamic_arr, _len)

    count_even_indices(dynamic_arr, _len)
    count_sum_between_zeros(dynamic_arr, _len)
    transform_array(dynamic_arr, _len)
    print("измененный массив")
    print_array(dynamic_arr, _len)

if __name__ == "__main__":
    main()



'''import random

MAX_SIZE = 100

def input_size() -> int:
    while True:
        try:
            n = int(input(f"введите кол-во эл-тов (от 1 до {MAX_SIZE}): "))
            if 1 <= n <= MAX_SIZE:
                return n
            print(f"число должно быть от 1 до {MAX_SIZE}")
        except ValueError:
            print("нужно целое число")

def fill_array(arr : list[int], n : int):
    choice = input("выберите способ заполнения (1. с клавиатуры; 2. случайные числа): ")
    
    if choice == "1":
        for i in range(n):
            while True:
                try:
                    arr[i] = int(input(f"введите эл-т [{i}]: "))
                    break
                except ValueError:
                    print("нужно целое число")
    else:
        while True:
            try:
                low = int(input("введите нижнюю границу интервала: "))
                high = int(input("введите верхнюю границу интервала: "))
                if low > high:
                    low, high = high, low
                break
            except ValueError:
                print("нужны целые числа")
                
        for i in range(n):
            arr[i] = random.randint(low, high)

def print_array(arr : list[int], n : int):
    print(" ".join(str(arr[i]) for i in range(n)))

def count_even_indices(arr: list[int], n: int):
    product = 1
    has_elements = False
    for i in range(0, n, 2):
        product *= arr[i]
        has_elements = True
        
    if has_elements:
        print(f"произведение эл-тов с чет индексами: {product}")
    else:
        print("нет эл-тов")

def count_sum_between_zeros(arr: list[int], n: int):
    first_zero = -1
    last_zero = -1
    
    for i in range(n):
        if arr[i] == 0:
            first_zero = i
            break
            
    if first_zero == -1:
        print("нет нулей")
    else:
        for i in range(n - 1, -1, -1):
            if arr[i] == 0:
                last_zero = i
                break

        if first_zero == last_zero: 
            print("одного нуля мало")  

        sum = 0
        for i in range(first_zero + 1, last_zero):
            sum += arr[i]
        print(f"сумма эл-тов между нулями: {sum}")

def count_dsum_between_zeros(arr: list[int], n : int):
    try:
        first_zero = arr.index(0)
        last_zero = n - 1 - arr[::-1].index(0)
        
        if first_zero == last_zero:
            print("одного нуля мало")
        else:
            _sum = sum(arr[first_zero + 1 : last_zero])
            print(f"сумма элементов между первым и последним нулями: {_sum}")
    except ValueError:
        print("нет нулей")

def transform_array(arr: list[int], n: int):
    for i in range(1, n):
        if arr[i] < 0:
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] >= 0:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key


def fill_darray(n: int) -> list[int]:
    choice = input("выберите способ заполнения (1. с клавиатуры; 2. случайные числа): ")
    dynamic_arr = []
    
    if choice == "1":
        for i in range(n):
            while True:
                try:
                    element = int(input(f"введите эл-т [{i}]: "))
                    dynamic_arr.append(element)
                    break
                except ValueError:
                    print("нужно целое число")
    else:
        while True:
            try:
                low = int(input("введите нижнюю границу интервала: "))
                high = int(input("введите верхнюю границу интервала: "))
                if low > high:
                    low, high = high, low
                break
            except ValueError:
                print("нужны целые числа")
                
        for _ in range(n):
            dynamic_arr.append(random.randint(low, high))
            
    return dynamic_arr


def main():
    print("статический массив")
    static_arr = [0] * MAX_SIZE
    
    n = input_size()
    fill_array(static_arr, n)
    print("начальный массив")
    print_array(static_arr, n)
    
    count_even_indices(static_arr, n)
    count_sum_between_zeros(static_arr, n)
    transform_array(static_arr, n)
    print("измененный массив")
    print_array(static_arr, n)


    print("динамический массив")
    n = input_size()
    dynamic_arr = fill_darray(n)
    _len = len(dynamic_arr)
    print(f"начальный массив: {' '.join(map(str, dynamic_arr))}")

    count_even_indices(dynamic_arr, _len)
    count_dsum_between_zeros(dynamic_arr, _len)
    transform_array(dynamic_arr, _len)
    print(f"измененный массив: {' '.join(map(str, dynamic_arr))}")

main()'''