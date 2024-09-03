import multiprocessing

counter = multiprocessing.Value('i', 0) # Переменная целоги типа, работающая в разных процессах


def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock(): # на время выполнения операции прибавления блокируется значение переменной в текущем виде
            cnt.value += 1 # по завершении with - разблокируется
    print(f'Значение счётчика: {cnt.value:_}')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(counter, ))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'Значение счётчика в финале: {counter.value:_}')

