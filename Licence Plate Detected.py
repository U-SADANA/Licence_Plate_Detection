import cv2
import numpy as np


###############################
frameWidth=840
frameHeight=580
nPlateCascade=cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea=500
color=(0,128,0)
##################33333
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
count=0
while True:
    success,img=cap.read()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates=nPlateCascade.detectMultiScale(imgGray,1.1,4)

    for(x,y,w,h) in numberPlates:
        area=w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,128,0),2)
            cv2.putText(img,"Licence Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,color,2)

            imgReg = img[y:y+h,x:x+w] #region of number plate
            resize=cv2.resize(imgReg,(250,150))
            cv2.imshow("Licence Number",resize)

    cv2.imshow("Vehicle Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg",resize)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"LICENCE NUMBER CAPTURED",(150,265),cv2.FONT_HERSHEY_DUPLEX,1,(10,10,10),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1


