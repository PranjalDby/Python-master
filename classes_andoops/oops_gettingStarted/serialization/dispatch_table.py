import copyreg
import io
import pickle
from sys import setrecursionlimit

setrecursionlimit(10000)
# --------------- this codes only handles the pickling of our ClassToBePickled Class and hence. it will create private dispatch table which handles ClassToBePickled specially.
# in this code we are creating private dispatch_table
class ClassToBePickled:
    def __init__(self,name,value) -> None:
        self.name = name
        self.val =value
        self.lamb = lambda x : x * x

    def __getstate__(self):
        dict_attr = self.__dict__.copy()
        del dict_attr['lamb']
        return dict_attr
    

    def __setstate__(self,state):
        self.__dict__.update(state)
        lamb = lambda x : x * x
        state['lamb'] = lamb
        print("__setstate__ is called = ",state)


# define a reduction function that tell pickle to how to pickle our class object
def pickle_my_class_red(my_class_inst):
    return (ClassToBePickled,(my_class_inst.name,my_class_inst.val))


print("reduction function for our class = ",pickle_my_class_red(ClassToBePickled('pickled',22)))
# Registering a reduction function to copyreg
copyreg.pickle(ClassToBePickled,pickle_my_class_red)
# create BytesIO Object and Pickler
f = io.BytesIO()
p = pickle.Pickler(f,pickle.DEFAULT_PROTOCOL)

# Copy the dispatch table from copyreg to the picker
p.dispatch_table = copyreg.dispatch_table.copy()

my_inst = ClassToBePickled("Pickled Class",20)
p.dump(my_inst) #using picler to pickle class instance

f.seek(0) #reset the byte object to begining

unpicklerr =pickle.Unpickler(f).load();
print('unpickled ClassTobePickled Instance = ',unpicklerr.__dict__)
print("-------------------------------------------------------------------------------------------------------")

# pickling using global dispatch_table --------------------------------------------


class Helper:
    TAG = "PICKLED BY CUSTOM PICKLER AND CUSTOM DISPATCH TABLE"
    def __init__(self,name,ids) -> None:
        self.name = name
        self.id = ids
        self.lambd = lambda x : x**3

    def __getstate__(self):
        attribute = self.__dict__.copy()
        del attribute['lambd']
        return attribute

def recreate_object(name, id, lambd):
    obj = Helper(name, id)
    obj.lambd = lambd
    return obj

def reduction_func_helper(class_inst:Helper):
    
    state = (class_inst.name,class_inst.id,class_inst.lambd(20))

    return (recreate_object,state)

# copyreg.pickle(Helper,reduction_func_helper) #register our reduction function to the pickling of class
# f2 = io.BytesIO()
# p1 = pickle.Pickler(f2)

# obj2 = Helper("Pickling Using Global Dispatch Table",[10221,230221,34411,45011])
# p1.dump(obj2)
# print('Pickled class using global dispatch_table = ',p1)
# f2.seek(0)
# print('Unpickling our Class')

# unpickling = pickle.Unpickler(f2).load()
# print(unpickling.id)

# -------------------------- creating our custom dispatch table in our custom Pickler Class
        
class PicklerClass(pickle.Pickler):

    dispatch_table = {}
    def __init__(self,cls,reduction_func,file, protocol: int | None = ...):
        super().__init__(file, protocol)
        self.class_to_be_pickled = cls
        self.reduc_func = reduction_func
        self.dispatch_table[self.class_to_be_pickled] = self.reduc_func
    

file3 = io.BytesIO()

custom_pickler = PicklerClass(Helper,reduction_func_helper,file3,pickle.DEFAULT_PROTOCOL)
helper_obj = Helper("Pranjal22",[12,34,111,39,70])
custom_pickler.dump(helper_obj)
print(custom_pickler)
file3.seek(0)
unpickler1 = pickle.Unpickler(file3)
unpickled_class = unpickler1.load()
print(unpickled_class.__dict__)