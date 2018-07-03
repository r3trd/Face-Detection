
import cv2 as cv
from matplotlib import pyplot as plt
from time import gmtime, strftime

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

def detect (frame, f_c, scale_factor, minneigh) :
    label = 'face'
    current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    current_time = current_time.strip(" ").split(" ")
    label = label + "     time : " + current_time[1]
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = f_c.detectMultiScale(gray_img,scale_factor,minneigh)
    for (x,y,w,h) in faces :
        cv.rectangle(frame,(x,y),(x+w,y+h), color = (0,0,255), thickness=2)
        cv.putText(frame, label, (x, y-10),cv.FONT_HERSHEY_SIMPLEX, fontScale = 0.4, color=(0,0,255), thickness=1)
        cv.putText(frame, " Press 'q' to quit", (0+2, 0+15),cv.FONT_HERSHEY_SIMPLEX, fontScale = 0.5, color=(255,0,0), thickness=1)

capture = cv.VideoCapture(0) # 0 -> webcam

while (True) :
    _ , frame = capture.read()
    
    detect(frame,face_cascade,1.2,3)
    
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    

