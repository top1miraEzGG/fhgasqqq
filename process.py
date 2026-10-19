import os
import time
import multiprocessing


def func1():
    print(f"[Процесс 1] Запущен. ID процесса (PID): {os.getpid()}")
    time.sleep(2)  
    print(f"[Процесс 1] Завершен. ID процесса (PID): {os.getpid()}")

def func2():
    print(f"[Процесс 2] Запущен. ID процесса (PID): {os.getpid()}")
    time.sleep(3)
    print(f"[Процесс 2] Завершен. ID процесса (PID): {os.getpid()}")

def func3():
    print(f"[Процесс 3] Запущен. ID процесса (PID): {os.getpid()}")
    time.sleep(1)
    print(f"[Процесс 3] Завершен. ID процесса (PID): {os.getpid()}")

def func4():
    print(f"[Процесс 4] Запущен. ID процесса (PID): {os.getpid()}")
    time.sleep(4)
    print(f"[Процесс 4] Завершен. ID процесса (PID): {os.getpid()}")

if __name__ == '__main__':
    print(f"Главный процесс запущен. Его ID: {os.getpid()}\n")

    
    process1 = multiprocessing.Process(target=func1, name="Первый_процесс")
    process2 = multiprocessing.Process(target=func2, name="Второй_процесс")
    process3 = multiprocessing.Process(target=func3, name="Третий_процесс")
    process4 = multiprocessing.Process(target=func4, name="Четвертый_процесс")

    
    print(f"Создан процесс 1, ID: {process1.pid}, Имя: {process1.name}")
    print(f"Создан процесс 2, ID: {process2.pid}, Имя: {process2.name}")
    print(f"Создан процесс 3, ID: {process3.pid}, Имя: {process3.name}")
    print(f"Создан процесс 4, ID: {process4.pid}, Имя: {process4.name}")
    print("-" * 30)

    
    process1.start()
    process2.start()
    process3.start()
    process4.start()

    
    process1.join()
    process2.join()
    process3.join()
    process4.join()

    
    print("-" * 30)
    print("Все процессы завершены. Главный процесс завершает работу.")