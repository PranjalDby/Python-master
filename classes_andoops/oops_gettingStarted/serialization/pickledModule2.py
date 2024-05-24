from pickle_module import ExampleClass
import pickle
import os
from pickle_module import pickle_object
def unpickle_object(file):
    if os.path.exists(file):
        if os.path.getsize(file) > 0:
            with open(file,'rb') as f:
                # unpickling
                unpiclker = pickle.Unpickler(f)
                unpickled_obj = unpiclker.load()
                unp_obj2 = pickle.load(f)
                print(unp_obj2)
                # with open('unpickled_file','wb') as uf:
                #     unp_obj2 = pickle.load(f)
                #     uf.writelines(unp_obj2)


    else:
        print("Error")


def pickle_object():
    print(os.getcwd())
    my_object = ExampleClass("Machine Learning","Artificial Intelligence","Discrete Mathematics")
    # pickling the object it creates the files containing the serialization result
    file_name = ""
    with open('serializedFile1.txt', 'wb') as file:
        pickle.dump(my_object, file)
        file_name = file.name
    return file_name


if __name__ == "__main__":
    filename = pickle_object()

    # unpickle_object(filename)