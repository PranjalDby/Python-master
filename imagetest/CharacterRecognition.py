from email.mime import image
from tkinter import Image
from tkinter.filedialog import *
import pytesseract

import cv2
import matplotlib.pyplot as plot
from pytesseract import Output

print(pytesseract.__version__)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,1)


filename = askopenfilename(defaultextension='jpeg')
img = cv2.imread(filename)
imge = img.copy()
filtered_img = remove_noise(imge)
# filtered_img = get_grayscale(imge)
target = str(input('Enter the word tha you want to find: '))
d = pytesseract.image_to_data(filtered_img,output_type=Output.DICT)
print(d)
occurances = [ i for i,word in enumerate(d["text"]) if word == target]
# n_boxes= len(d['text'])
# print('len',n_boxes)
print(d)
for i in occurances:
    if int(d['conf'][i]) >= 0:
        (x,y,w,h) = (d['left'][i],d['top'][i],d['width'][i],d['height'][i])
        imge = cv2.rectangle(imge,(x,y),(x+w,y+h),color=(255,0,0),thickness=1)

cv2.imshow('img',imge)
cv2.waitKey(0)



