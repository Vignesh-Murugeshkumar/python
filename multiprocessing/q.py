from multiprocessing import Process, Queue, current_process, Value , Lock, Array
import os
from multiprocessing import Process, Queue, current_process, Value , Lock
import time
def squarnumber(numbers, queue):
    for i in numbers:
        print(
            "Square of", i, "is", i * i,
            "from process", current_process().name
        )
        queue.put(i * i)
def add100(shared_Array, lock):
    for _ in range(100):
        with lock:
            time.sleep(0.01)
            for i in range(len(shared_Array)):
                shared_Array[i] += 1
if __name__ == "__main__":
    q=Queue()
    numbers = [1, 2, 3, 4, 5]
    p1 = Process(target=squarnumber, args=(numbers,q))
    p2 = Process(target=squarnumber, args=(numbers, q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Main process ended:", q.get())