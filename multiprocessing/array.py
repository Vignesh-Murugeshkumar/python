from multiprocessing import Process, Queue, current_process, Value , Lock, Array
import os
import time
def squarnumber(q, num):
    for i in num:
        print(
            "Square of", i, "is", i * i,
            "from process", current_process().name
        )
        q.put(i * i)
def add100(shared_Array, lock):
    for _ in range(100):
        with lock:
            time.sleep(0.01)
            for i in range(len(shared_Array)):
                shared_Array[i] += 1
if __name__ == "__main__":
    lock=Lock()
    shared_array=Array('d',[10,20,30,40,50])
    print("Main process started:", shared_array[:])
    p1 = Process(target=add100, args=(shared_array, lock))
    p2 = Process(target=add100, args=(shared_array, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Main process ended:", shared_array[:])