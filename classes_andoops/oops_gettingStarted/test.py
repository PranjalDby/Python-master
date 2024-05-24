
name = "Pranjal Dubey"
print(name)

def changeName():
    global name
    print(name)
    name = "Hello! Your Name Changed"
    print(name)

changeName()