import time

def slow_func(n: int):
    print('Начало функции')
    time.sleep(n)
    print('Конец функции')


print('Начало программы')
slow_func(3)
print('Конец программы')