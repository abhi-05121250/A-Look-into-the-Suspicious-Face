import cv2
import numpy as np 
import face_recognition
import os
import imutils
from datetime import datetime
from datetime import date
from PIL import ImageGrab

path="C:\\Users\\HP\\Downloads\\Ai and ml\\code\\a"
images= []
classNames= []
myList=os.listdir(path)
print(myList)
for cl in myList:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList=[]
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    filePath="C:\\Users\\HP\\Downloads\\Ai and ml\\code\\attendance.csv"
    with open(filePath,'r+')as f:
        myDataList=f.readlines()
        nameList=[]
        for line in myDataList:
            entry=line.split(',')
            nameList.append(entry[0])
        
        if name not in nameList:
            now=datetime.now()
            today = date.today()
            dtString=now.strftime('%H:%M:%S')
            f.writelines(f'{name},{today},{dtString}')
            f.writelines(f'\n')
        

#def captureScreen(bbox=(300,300,690+300,530+300)):
    #capScr=np.array(ImageGrab.grab(bbox))
    #capScr=cv2.cvtColor(capScr,cv2.COLOR_RGB2BGR)
    #return capScr

encodeListKnown=findEncodings(images)
print('Encoding Complete')

#so now tird step is that we have to find the matches betweeen our encodings 
 #but we dont have an images to match with 
#and now that image will be coming from our webcam so lets initialize the webcam

cap= cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    success, img=cap.read()
    #img=captureScreen()
    #making the size of image small for better matching
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB) #converting the image into rgb
    facesCurFrame=  face_recognition.face_locations(imgS)
    encodesCurFrame =face_recognition.face_encodings(imgS,facesCurFrame)
    
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
     matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
     faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
     print(faceDis)
     matchIndex= np.argmin(faceDis)
     if faceDis[matchIndex]<0.50:
         name=classNames[matchIndex].upper()
         #print(name)
         y1,x2,y2,x1=faceLoc
         y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
         cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
         cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
         cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
         markAttendance(name)
    
     else: 
      name='unknown' 
      y1,x2,y2,x1 = faceLoc
      y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
      cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
      cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
      cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
      markAttendance(name)
      
    

    #  
    cv2.imshow('cctv',img)
    cv2.waitKey(1) 

    
 








    #
    
    
    
   
    













#faceLoc =  face_recognition.face_locations(imgabhi)[0]
#encodeAbhi =face_recognition.face_encodings(imgabhi)[0]
#cv2.rectangle(imgabhi,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,225),2)

#faceLocTest =  face_recognition.face_locations(imgTest)[0]
#encodeTest =face_recognition.face_encodings(imgTest)[0]
#cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,225),2)

#results = face_recognition.compare_faces([encodeAbhi],encodeTest)


#faceDis= face_recognition.face_distance([encodeAbhi],encodeTest)








