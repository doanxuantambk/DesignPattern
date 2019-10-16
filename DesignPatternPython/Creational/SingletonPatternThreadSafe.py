import threading
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import time
from random import randint

threadLock = threading.Lock()
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    """ Python khong co private constructor"""
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is singleton")
        else:
            Singleton.__instance = self

def main():
    s2 = Singleton()
    print(s2)

    s = Singleton.getInstance()
    print(s)

    s2 = Singleton.getInstance()
    print(s2)

sum = 0
def task():
    for i in range(100):
        threadLock.acquire()
        global sum
        sum = sum + 1
        print("Task Executed {}".format(threading.current_thread()), "result:", sum)
        threadLock.release()
        time.sleep(0.1)
        return 1

def syn_task_sample():
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)

def return_after_5_secs(num):
    tsleep = randint(1, 5)
    time.sleep(tsleep)
    return "Return of {} sleep {}s".format(num, tsleep)

def get_value_threadpool():
    pool = ThreadPoolExecutor(5)
    futures = []
    for x in range(5):
        futures.append(pool.submit(return_after_5_secs, x))

    for x in as_completed(futures):
        print(x.result())

if __name__ == "__main__":
    main()
    syn_task_sample()
    get_value_threadpool()