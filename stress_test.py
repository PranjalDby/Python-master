import multiprocessing
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np


def cpu_heater(dimensions):
    rand_generator = np.random.MT19937(int(time.time()))
    print("Matrix Multiplication......")
    for i in range(50):
        mat1 = rand_generator.random_raw(dimensions)
        mat2 = rand_generator.random_raw(dimensions)
        res = np.matmul(mat1, mat2)
    return res

def cross_product(dimensions: list[int]):
    with multiprocessing.Pool() as p:
        p.map(cpu_heater, [dimensions])
    
    print("Call Complete")


if __name__ == "__main__":
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SYSTEM INFO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("Platform:{}".format(sys.platform))
    start_time = time.time()
    cross_product([1000,1000])
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
    print("Hello World")