import multiprocessing
import os
import time
import random
from datetime import datetime

def task():
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    print(f"Process {os.getpid()} took {wait_time:.2f} seconds and the current time is {datetime.now()}")

if __name__ == "__main__":
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

