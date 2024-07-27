import platform 
def executeInfo():
    mysys = platform.uname()
    fields_name = mysys._fields

    for i in range(len(fields_name)):
        print(f'{fields_name[i]}:{mysys.__getattribute__(fields_name[i])}')


if __name__ == "__main__":
    executeInfo()