import sys
import gc # garbage collector module
def example_func(a):
    return a ** 3


ref = example_func

ref2 = example_func

gc.garbage.append(ref2)
print("reference count = ",sys.getrefcount(ref))
print("list of refferer = ",gc.get_referrers(ref))



#! --------------------------------------------------------- using garbage collector module in debug mode ------------------------------------------------------------------
gc.set_debug(gc.DEBUG_STATS) # this will print the statisitics whenever the garbage collector is run.

#getting the threshold
print(gc.collect(2))
print(gc.get_threshold())