from multiprocessing import Process, Queue, current_process, Value , Lock
import os
import time
def squarnumber(num):
    for i in num:
        print(
            "Square of", i, "is", i * i,
            "from process", current_process().name
        )
def add100(shared_number, lock):
    for _ in range(100):
        with lock:
            time.sleep(0.01)
            shared_number.value += 1
if __name__ == "__main__":
    lock=Lock()
    shared_number = Value('i', 0)
    print("Main process started:", shared_number.value)
    p1 = Process(target=add100, args=(shared_number, lock))
    p2 = Process(target=add100, args=(shared_number, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Main process ended:", shared_number.value)