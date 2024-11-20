# parallel_processing/parallel.py

import numpy as np
from concurrent.futures import ThreadPoolExecutor

# Функція для обчислення квадрату числа
def calculate_square(number):
    return number ** 2

# Функція для паралельного обчислення квадратів чисел
def run_parallel_computations():
    numbers = [1, 2, 3, 4, 5]
    
    # Використовуємо ThreadPoolExecutor для паралельного виконання задач
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(calculate_square, numbers))
    
    return results

if __name__ == "__main__":
    # Викликаємо паралельні обчислення та виводимо результати
    results = run_parallel_computations()
    for num, square in zip([1, 2, 3, 4, 5], results):
        print(f"The square of {num} is {square}")
