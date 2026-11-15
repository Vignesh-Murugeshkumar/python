
import threading
import time

def analyze_log(filename):

    # Print started message

    print(f"Analyzing {filename}... ")

    # Simulate log analysis for 2 seconds
    time.sleep(2)

    # Print completed message
    print(f"Completed analyzing {filename}.")


if __name__ == "__main__":

    files = ["auth.log", "firewall.log", "server.log"]

    threads = []

    # Create three threads
    t1=threading.Thread(target=analyze_log, args=(files[0],))
    t2=threading.Thread(target=analyze_log, args=(files[1],))
    t3=threading.Thread(target=analyze_log, args=(files[2],))
    # Hint: Use threading.Thread()
    # Pass filename using args parameter

    # Start all threads
    t1.start()
    t2.start()
    t3.start()
    # Wait for all threads using join()
    t1.join()
    t2.join()
    t3.join()

    print("Security monitoring completed")
