from collections import namedtuple
import copy
import io
import pickle
import os
import pprint
import sqlite3
import stat

class ExampleClass:
    __slots__ = ('name','age','roll','subjects')
    
    def __init__(self,*subject):
        print('Executing Some Malicious Code')
        self.name = "Pranjal"
        self.age = 40
        self.roll = 33
        self.subjects =subject


def pickle_object():
    print(os.getcwd())
    my_object = ExampleClass("Machine Learning","Artificial Intelligence","Discrete Mathematics")
    # pickling the object it creates the files containing the serialization result
    file_name = ""
    with open('serializedFile.txt', 'wb') as file:
        pickle.dump(my_object, file)
        file_name = file.name
    return file_name


# deserializing the serialized object structure

if __name__ == "__main__":

    # pickled_file = pickle_object()
    # if os.path.getsize(pickled_file) > 0:
    #     # unpickled = pickle.load(pickled_file)
    #     # print(unpickled)
    #     with open(pickled_file, 'rb') as file:
    #         # same as pickle.load()
    #         # unpickler = pickle.Unpickler(file)
    #         our_data = pickle.load(file)
    #         print("pickling completed",our_data.__slotnames__)

    # else:
        print('file is Empty.')

    # Without file argument

    # obj = ExampleClass()
    # my_pickled_obj = pickle.dumps(obj)  # Pickling Object
    
    # print(my_pickled_obj)
    
    # print('Unpickling above pickled object')
    
    # unpicked_obj = pickle.loads(my_pickled_obj)
    # # "".startswith(["__","__"])
    # for only_attr in unpicked_obj.__dir__():
    #     if not only_attr.startswith(('__', '__')):
    #         res = only_attr
    #         print(res)

# / stands for Position-only argument separator  and it is not allowed after "*" parameter and any parameter appear before / this is positional only argument.this means we can't use that argument as keyword-argument.

# only * in parameter of function stands for only single postional argument is allowed
def add(a,/, *, b=10, c=10):
    print(1)
    return a + b + c


# print(add(10,b =20,c = 40))

# Pickable and unpickable Objects...........

"""
the list of unpickable objects includes database connections,opened network sockets,running threads and others.

if we find yourself with an unpickable objects.we can do couple of things that you can do. the first option is to use third-party library liked (dill)...

1.it helps us to serialize less common types like functions with yields,nested functions,lambdas,and many others.
"""

# Using dill module

# Testing this module, we can try to pickle lambda function

square = lambda x: x * x
# my_pickle = pickle.dumps(square) # Throws Error: PicklingError

# Now We are Trying to replace the pickle module with dill.

import dill

# my_pickle_dill = dill.dumps(square,pickle.HIGHEST_PROTOCOL)

# print(my_pickle_dill)

# -------------------------------- Serializing an interpreter session ----------------------------

# a = square(45)
# import math
# b = math.sqrt(343)
# dill.dump_session('test.pk1') # dumps the entire session of interpreter into single file 
# exit() # denotes that here our code ends


# ------------------------------- Restoring an the last interpreter session using our file ----------

# print('global items of this session = ',globals().items())

# print()
# print("----------------------------------------------------------------")
# dill.load_session('test.pk1')
# print('after loading last session of interpreter = ',globals().items())
# print(a,b)


# In below Example, we see how we can define a class with several attributes and exclude one attribute from serialization with __getstate__().

class foobar:
    def __init__(self) -> None:
        self.a = 35
        self.b = "test"
        self.c = lambda x: x * x
        print("class foobar init method will called")

    
    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['c']
        return attributes
    
class classWithDictAndSlots:
    __slots__ = ('name','age','__dict__')


    def __init__(self):
        print('class with dict and slots are instantiated')

    
    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes
    

# foo_instance = foobar()

# my_foobar_pickled = pickle.dumps(foo_instance)
# print(my_foobar_pickled)
# my_foobar_unpickled = pickle.loads(my_foobar_pickled)

# print(my_foobar_unpickled.__dict__)


ff = classWithDictAndSlots()
ff.name = "Pranjal"
ff.age = 32
ff.gender = "male"
pickled_ff = pickle.dumps(ff)
print(pickled_ff)

print('unpickling our pickled classWithDictAndSlots = ',pickle.loads(pickled_ff))

# Pickling class instances ...........................

"""
in this section,we describes the general mechanism available to you to define, customize and control how class instances are pickled and unpickled
"""

# def save(obj):
#     return (obj.__class__,obj.__dict__)

# def restore(cls,attributes):
#     obj = cls.__new__(cls)
#     obj.__dict__.update(attributes)
#     return obj


# saved_instance = save(foo_instance)

# print(f'Saving the instance of class = {saved_instance}')

# print(f'restoring the instance of class = {restore(saved_instance[0],saved_instance[1])}')

"""--------------------------------- Using __getstate__() and __setstate__() in class -------------------------------------------------------------------------------"""


""" in above Example we ignored the object `c` becuause it can't be pickled. but if you want to do some additional initialization while unpickling, say by adding the excluded `c` object back to deserialized instance"""

class updatedFoobar:

    __slots__ = ('var_a','var_b','lambda_func')

    def __init__(self,a,b) -> None:
        self.var_a = a
        self.var_b = b
        self.lambda_func = lambda x: x * x

    def __getstate__(self):

        # pickle helper
        # Our class contains __slots__ not dict
        attributes = (None,{})
        for i in self.__slots__:
            if self.__getattribute__(i) != None:
                attributes[1][i] = self.__getattribute__(i)
        

        print(attributes)
        del attributes[1]['lambda_func']
        return attributes
    
    def __setstate__(self,state):
        """It is Called When we unpickle the pickled object"""
        """ if __setstate__() is called with unpickled state. in that case there is no requirement for the state object to be dictionary"""
        print('__setstate__ is called')
        for k,v in state[1].items():
            setattr(self,k,v)

        setattr(self,'lambda_func',lambda x: x * x)

        

            

update_foobar_instance = updatedFoobar(10,'Pranjal')
# Pickling
pickled_updated_foobar_ins = pickle.dumps(update_foobar_instance)
print("Pickled updatedFoobar = ",pickled_updated_foobar_ins)


# Unpickling
unpickled_updated_foobar = pickle.loads(pickled_updated_foobar_ins)
print(f'unpickled updateFoobar instance = ',unpickled_updated_foobar.lambda_func(30))


#--------------------------------------- Some other Examples -------------------------------------------------------------

data = {
    'a':[1,2.0,3+4j],
    'b':("character string",b'byte string'),
    'c':{None,True,False}
}

# pickling a dictionary object

with open('pickled_dict','wb') as file:
    pickler = pickle.Pickler(file,pickle.HIGHEST_PROTOCOL)
    pickler.dump(data)


# unpickling pickled dict obj
with open('pickled_dict','rb') as readable:
    unpickled_dict = pickle.Unpickler(readable)
    print(unpickled_dict.load())


# --------------------------- Persistence of external objects ---------------------------------
    

# simple class reperesenting a record in our db

MemoRecord = namedtuple("MemoRecord",("key","task"))
print("Our named tuple = ",MemoRecord)

class DBPickler(pickle.Pickler):
 
    def persistent_id(self, obj):

        if isinstance(obj,MemoRecord):
            # here our persistent id is a simply tuple, containing a tag and key, which refers to specific record in the database

            return ("MemoRecord",obj.key)
        
        else:
            # if obj does not have persistent ID, return None
            # this means obj will pickled as usual
            return None
        

class DBUnpickler(pickle.Unpickler):

    def __init__(self,file,connection):
        super().__init__(file)
        self.connect = connection


    # unpickler will have to implement persitent_load(pid);
        
    def persistent_load(self, pid):
        # this method is invoked whenever persistent id is encountered.
        # here pid is the tuple returned by DBPickler.

        cursor = self.connect.cursor() # to navigate to our db
        print(f'our pid = {pid}')
        type_tag,key_id = pid

        if type_tag == "MemoRecord":
            # Fetch the reffrence record from the db and returned it.
            cursor.execute("SELECT * FROM memos WHERE KEY=?",(str(key_id),))
            key,task = cursor.fetchone()
            return MemoRecord(key,task)
        
        else:
            # Always raises an error if you cannot return the correct object.
            # Otherwise, the unpickler will think None is the object referenced
            # by the persistent ID.

            raise pickle.UnpicklingError("unsupported persitent object")
        

def main():
    
    # initialize and populate our database

    conn = sqlite3.connect("record2.sqlite")
    cursor = conn.cursor()
    try:
        table_exist = cursor.execute("SELECT * FROM memos")
        print(table_exist.fetchall())

    except sqlite3.OperationalError as e:
        print("Error Raised")
        cursor.execute("CREATE TABLE memos (key INTEGER PRIMARY KEY, task TEXT)")
        tasks = (
            "code and study",
            "eat",
            "play and enjoy",
            "sleep (IMP)",
            "repeat"
        )
        for i in tasks:
            cursor.execute(f"INSERT INTO memos VALUES(NULL,?)",(i,))
        
        conn.commit()
        conn.close()

    
    else:
        # Fetch the records to be pickled.
        print('Fetching the record from db')
        cursor.execute("SELECT * FROM memos")
        memos = [MemoRecord(k,t) for k,t in cursor]
        print(memos)

        # Saving the records using our custom DBPickler

        file = io.BytesIO()
        DBPickler(file,pickle.HIGHEST_PROTOCOL).dump(memos)
        print("Pickled records:")
        pprint.pprint(memos)

        # update the records, just for good measure.
        cursor.execute("UPDATE memos SET task='Watch Youtube' WHERE key=2")

        # Load the records from the pickle data stream.
        file.seek(0)
        memos = DBUnpickler(file,conn).load()
        print("Unpickled Records.")
        pprint.pprint(memos)
        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()

    


