from threading import Thread, Lock
from queue import Queue
if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 5
    def worker(q):
        while True:
            item = q.get()
            with lock:
             if item is None:
                q.task_done()
                break

            print(item)
            q.task_done()
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,))
        thread.daemon = False
        thread.start()
    for item in range(20):
        q.put(item)
    for i in range(num_threads):
        q.put(None)
    q.join()
    print("All tasks completed!")