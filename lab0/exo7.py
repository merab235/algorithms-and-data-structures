import time


# Пример: вычисление последней цифры большого числа Фибоначчи
def fib_last_digit(n):
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10

    return current


# Чтение числа из файла
with open('input.txt', 'r') as infile:
    n = int(infile.readline())

# Начало замера времени
start_time = time.perf_counter()

# Вычисляем результат
result = fib_last_digit(n)

# Выводим результат
with open('output.txt', 'w') as outfile:
    outfile.write(f'{result}\n')

# Конец замера времени
end_time = time.perf_counter()

# Выводим время выполнения
print(f'Время выполнения: {end_time - start_time} секунд')
