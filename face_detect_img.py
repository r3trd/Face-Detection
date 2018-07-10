
import cv2 as cv
from matplotlib import pyplot as plt
import time
import copy

path = input("Enter the path of the image to be processed: ")
img = cv.imread(path) # reads image in GBR mode
img_copy = copy.copy(img)
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
face = face_cascade.detectMultiScale(gray_img, 1.2, 5)

for (x,y,w,h) in face :
    cv.rectangle(img_copy,(x,y),(x+w,y+h), color = (0,0,255), thickness=4)
plt.axis("off")
plt.imshow(cv.cvtColor(img_copy, cv.COLOR_BGR2RGB))
plt.title('Image')
plt.show()
