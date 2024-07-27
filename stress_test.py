import multiprocessing
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import random
def cpu_heater(mat1,mat2):
    print("Matrix Multiplication......")
    res = np.matmul(mat1,mat2);
    return res

def cross_product(dimensions):
    rand_generator = np.random.MT19937(int(time.time()))

    for i in range(1,10):
        matrix = rand_generator.random_raw((10000,1000))
        matrix2 = rand_generator.random_raw((1000,10000))
        executor = ThreadPoolExecutor(i,"MAT_MUL")
        res = executor.submit(cpu_heater,matrix,matrix2)
        print(res.result())
    
    print("Call Complete")


if __name__ == "__main__":
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SYSTEM INFO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("Platform:{}".format(sys.platform))
    start_time = time.time()
    cross_product((1000,1000))
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
    print("Hello World")

