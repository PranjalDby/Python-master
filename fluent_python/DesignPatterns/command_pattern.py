# Command Method is behavioral Design pattern that encapsulates a request as an object, thereby allowing for the parameterization of clients with different requests and queuing or logging of requests. Parametrizing other objects with different requests in our analogy means that button can be used to turn on the light can later be used turn on the stereo or maybe open the garage door.

# Main Motive hear is the command pattern suggests that object shouldn't send these request directly.instead they should extract all the request details, such as object being called, the name of the method and list of arguments into seperate command class with single method that triggers this request.

# Command Pattern contains : Command Abstract class,Invoker,Receiver 

from abc import ABC,abstractmethod

#this is a abstract class
class Command(ABC):
    def __init__(self,receiver):
        self.reciever = receiver
    
    #abstract method
    def process(self):
        pass

# class dedicated to Command Impelementation
class SysInfoPrint(Command):
    def __init__(self, receiver):
        self.reciever = receiver

    def process(self):
        self.reciever.perform_action(self)

#Receiver
class Receiver:
    def perform_action(self,obj):
        if isinstance(obj,SysInfoPrint):
            import platform
            print('Current System info Cpu')
            def executeInfo():
                mysys = platform.uname()
                print(f'System: {mysys.system}')
                print(f'Node Name: {mysys.node}')
                print(f'Release Ver: {mysys.release}')
                print(f'System Ver: {mysys.version}')
                print(f'Machine: {mysys.machine}')
                print(f'Processor: {mysys.processor}')

            executeInfo()
            print(executeInfo.__dir__())
            print('Action performed by Reciever.')

# Invoker Class takes the command and invoke it to the valid reciever
class Invoker:
    def command(self,cmd:Command):
        self.cmd = cmd

    def execute(self):
        self.cmd.process()


"""  Main method """
if __name__ == "__main__":
    receiver = Receiver()
    cmd = SysInfoPrint(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
    
