import fnmatch
from tkinter.filedialog import askopenfiles

files = askopenfiles('r')
str1 = []
for i in files:
    str1.append(i.name.split('/'))
    
for i in str1:
    print(i[-1])