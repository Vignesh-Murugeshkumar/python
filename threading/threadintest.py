import threading
import time
def sq(num):
  print(num**2)
  time.sleep(1)
def cube(num):
  print(num**3)
  time.sleep(2)
t1=threading.Thread(target=sq,args=(4,))
t2=threading.Thread(target=cube,args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()


