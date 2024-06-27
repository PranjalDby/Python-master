import functools
import os
from pathlib import Path
import platform
import pyaudio
# slowing Down Code, revisited

def slow_down(func = None,sleep_time = 1):
    """sleep given amount of seconds before calling functions"""
    def slow_down_decorator(func):
        import time
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print(f"Waiting for {sleep_time} s")
            time.sleep(sleep_time)
            return func(*args,**kwargs)
        
        return wrapper
    
    if func:
        return slow_down_decorator(func)
    
    else:
        return slow_down_decorator


from pydub import *
from pydub.playback import *
platform_name = platform.system()

def path_to_ffmpeg():
    SCRT_DIR = Path(__file__).parent
    print(Path(__file__).stat)
    if platform_name == "Windows":
        return str(Path(SCRT_DIR,"win","ffmpeg","ffmpeg.exe"))
    
def play_audio():
    AudioSegment.ffmpeg = path_to_ffmpeg()
    
    if AudioSegment.ffmpeg != None:
        print(f'FFMPEG FOUND LOCA = {str(Path(Path(__file__).parent,"win","ffmpeg","ffmpeg.exe"))}')
        song = AudioSegment.from_mp3('classes_andoops/oops_gettingStarted/python_classes/decorator_revisit/rocket-launch.mp3')
        play(song)
    else:
        print("Please Install FFMPEG")


@slow_down(sleep_time=1)
def count_down(from_number):
    
    if from_number < 1:
        print("LiftOff")
        play_audio()
    else:
        print(from_number)
        count_down(from_number-1)



            
@slow_down(sleep_time=4)
def printCheese():
    print("Printing cheese 🧀🍕🍕🍕")


# -------------------------------- creating singleton (singleton class) ------------------------------------------------------------------

def singleton(cls):
    """Make a class a Singleton class"""
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        if wrapper.instance is None:
            wrapper.instance = cls(*args,**kwargs)
        
        
        return wrapper.instance
        
    wrapper.instance = None

    return wrapper

@singleton
class Single:
    def __init__(self,name):
        self.name = name

if __name__ == "__main__":

    # count_down(5)
    # path_to_ffmpeg()

    ss1 = Single("Single 1")
    ss2 = Single("Single 2")

    print(ss1)
    print(ss2)