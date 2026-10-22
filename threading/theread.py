from threading import Thread, Lock
import time

database_value = 0
lock = Lock()

def increment():
    global database_value
    with lock:  # using context manager automatically handles acquire/release
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy

if __name__ == "__main__":
    print("Main thread started:", database_value)
    thread1 = Thread(target=increment)
    thread2 = Thread(target=increment)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    print("Main thread ended:", database_value)