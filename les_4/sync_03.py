import random
import time

def long_run_task(n: int):
    for i in range(n):
        print(f'Выполнение задачи {i}')
        time.sleep(random.randint(1, 3))


def main():
    print('Начало программы')
    long_run_task(10)
    print('Конец программы')


main()