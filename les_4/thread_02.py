import threading
import time

def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, ))
    threads.append(t)

for t in threads:
    t.start() # после старта каждого потока, программа ждёт его завершения
    t.join()

print("Все потоки завершили работу")

# Теперь 5 потоков работают последовательно. Программа работает синхронно, преимущество многопоточности сведено к нулю