import cv2 as cv
#from matplotlib import pyplot as plt
from time import gmtime, strftime
import time
import ctypes

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
#count = 0

def detect (frame, f_c, scale_factor, minneigh, count) :
    label = 'face'
    current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    current_time = current_time.strip(" ").split(" ")
    label = label + "     time : " + current_time[1]
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.putText(frame, " Press 'q' to quit", (0+2, 0+15),cv.FONT_HERSHEY_SIMPLEX, fontScale = 0.5, color=(255,0,0), thickness=1)
    faces = f_c.detectMultiScale(gray_img,scale_factor,minneigh)
    print(faces," ", count)
    if(faces == ()) :
        count = count + 1
        return count
    else :
        count = 0;
    for (x,y,w,h) in faces :
        cv.rectangle(frame,(x,y),(x+w,y+h), color = (0,0,255), thickness=2)
        cv.putText(frame, label, (x, y-10),cv.FONT_HERSHEY_SIMPLEX, fontScale = 0.4, color=(0,0,255), thickness=1)
    return 0

    
capture = cv.VideoCapture(0) # 0 -> webcam
frames = 500
start = time.time()
count = 0
end = 0
flag = True

while (True) :
    _ , frame = capture.read()
    
    count = detect(frame,face_cascade,1.2,3,count)
    
    cv.imshow('Video', frame)

    if (count == frames) :
        capture.release()
        flag = False
        end = time.time()
        cv.destroyAllWindows()
        break
        
    if (cv.waitKey(1) & 0xFF == ord('q')):
        end = time.time()
        capture.release()
        cv.destroyAllWindows()
        break

print("No. of frames captured : ", frames," ", count)
print("Total duration (in seconds) : ", end - start)
print("FPS : ", frames/(end - start))

if(flag == False) :
    ctypes.windll.user32.LockWorkStation()
