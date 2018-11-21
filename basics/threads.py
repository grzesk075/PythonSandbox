import threading
import time
# import queue - designed for inter-thread communication and synchronization


class AsyncPrinter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        for i in range(20):
            time.sleep(0.01)
            print('Async:', i)


AsyncPrinter().start()

for i in range(20):
    time.sleep(0.01)
    print('Main thread:', i)

# module weakref enables to create weak references for use in cache or tracking
# they don't prevent from garbage collector
