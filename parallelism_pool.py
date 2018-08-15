# 1. Creates multiple processes
# 2. Processes can't share global variables in a straigh-forward way
# 3. Utilizes all the cores
# 4. To shared some variables across the processes use
#    multiprocessing.Queue
# 5. Usually for simple multiprocessing tasks
import multiprocessing
import time
import random


def hello(n):
    time.sleep(random.randint(1, 3))
    print("[{0}] Hello!".format(n))


pool = multiprocessing.Pool(processes=10)

# Returns everything in order, waiting for all the processes to end
results = [pool.apply(hello, args=(i,)) for i in range(10)]

# Returns as and when a process gets over
results = pool.map(hello, range(10))

print("Done!")
