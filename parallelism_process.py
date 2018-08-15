# 1. Creates multiple processes
# 2. Processes can't share global variables in a straigh-forward way
# 3. Utilizes all the cores
# 4. To shared some variables across the processes use
#    multiprocessing.Queue
import multiprocessing
import time
import random


def hello(n):
    time.sleep(random.randint(1, 3))
    print("[{0}] Hello!".format(n))


processes = []
for i in range(10):
    process = multiprocessing.Process(target=hello, args=(i,))
    processes.append(process)
    process.start()


# Waiting for each process to end
for one_proc in processes:
    one_proc.join()

print("Done!")
