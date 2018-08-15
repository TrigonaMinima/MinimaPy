# 1. Creates multiple threads
# 2. Threads share global variables
# 3. Not really parallel
import threading
import time
import random


def hello(n):
    time.sleep(random.randint(1, 3))
    print("[{0}] Hello!".format(n))


threads = []
for i in range(10):
    t = threading.Thread(target=hello, args=(i,))
    threads.append(t)
    t.start()


# To print "Done!" at the end
for one_thread in threads:
    one_thread.join()

print("Done!")
