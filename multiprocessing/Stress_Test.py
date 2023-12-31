import multiprocessing
import timeit
from concurrent.futures import ThreadPoolExecutor
def cpu_heater(number):
    return sum(i * i for i in range(number))

def find_sums(lists):
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(cpu_heater,lists)

if __name__ == "__main__":
    numbers = {5_000_000 + x for x in range(8000)}
    start_time = timeit.default_timer()
    find_sums(numbers)
    endtime = timeit.default_timer()
    duration =  endtime - start_time
    print(f"Duration {duration} seconds")
