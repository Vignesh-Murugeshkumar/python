from multiprocessing import Pool, Process, Queue, current_process, Value , Lock, Array
import os

import time
def squarnumber(numbers):
    for i in numbers:
        print(
            "Square of", i, "is", i * i,
        )
def add100(shared_Array, lock):
    for _ in range(100):
        with lock:
            time.sleep(0.01)
            for i in range(len(shared_Array)):
                shared_Array[i] += 1
if __name__ == "__main__":
   shared_Array = Array('i', [0, 0, 0, 0, 0])
   lock = Lock()
   numbers = [1, 2, 3, 4, 5]
   num=[4,5,6,7,8]
   p = Pool(processes=2)
   p.map(squarnumber, [numbers, num])
   p.apply(add100, args=(shared_Array, lock))
   p.close()
   p.join()
