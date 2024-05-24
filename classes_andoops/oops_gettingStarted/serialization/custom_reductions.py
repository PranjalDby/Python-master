# Custom Reduction for Types,Functions, and Other Objects.
# customize the pickling of functions and classes.

import io
import pickle

class MyClass:
    my_attribute = 1
    name = "Pranjal"
# custom pickler
    
class MyPickler(pickle.Pickler):

    def reducer_override(self, obj):
        print("reducer_ovveride called")
        """Custom reducer for MyClass."""
        if getattr(obj,"__name__",None) == "MyClass":
            return type ,(obj.__name__,obj.__bases__,{'my_attribute':obj.my_attribute,'name':obj.name})

        else:
            return NotImplemented


f = io.BytesIO()
p = MyPickler(f)
p.dump(MyClass)
print(f.readline())
print(object.__dict__)
print(globals())
del MyClass
print("After Deleting class from current scope.")
print(globals())
unpickled_class = pickle.loads(f.getvalue())
print(unpickled_class.__name__)
assert isinstance(unpickled_class,type)
assert unpickled_class.__name__ == "MyClass"
assert unpickled_class.my_attribute == 1
