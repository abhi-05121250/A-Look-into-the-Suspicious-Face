import cv2
import numpy as np 
import face_recognition
import os
import imutils
from datetime import datetime
from datetime import date
from PIL import ImageGrab
import pandas as pd
def format_col_width(ws):
    ws.set_row('A:B', 20)

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': []})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('unknown_img_data.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Insert an image.
#worksheet.insert_image('D3', 'D:\python\Ai and ml\code\opencv_frame_1.png',{})

# Close the Pandas Excel writer and output the Excel file.



img_counter=0
path='AttendanceImages'
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
    with open('Attendance.csv','r+')as f:
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

#so now tird step is that we have to find the matches betweeen our encodings but we dont have an images to match with 
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
      img_name = "opencv_frame_{}.png".format(img_counter)
      cv2.imwrite(img_name, img)
      print("{} written!".format(img_name))
      img_counter += 1
      markAttendance(img_name)
      #path='D:\python\Ai and ml\code\opencv_frame_'+'img_counter'+'.png'

      #unkimg='D:\python\Ai and ml\code\opencv_frame_1.png'
    #   x_scale=0.2
    #   y_scale=0.1
    #   row=1
    #   col=1
    #   worksheet.insert_image(row,col, path,{'x_scale':x_scale , 'y_scale': y_scale})
    #   #worksheet.insert_image('A3', 'D:\python\Ai and ml\code\opencv_frame_2.png',{'x_scale':x_scale , 'y_scale': y_scale})
    #   row +=1
    #   #writer.save()

      
    

    #  
    cv2.imshow('cctv ',img)
    cv2.waitKey(1) 
    #writer.save()

    
 








    #
    
    
    
   
    













#faceLoc =  face_recognition.face_locations(imgabhi)[0]
#encodeAbhi =face_recognition.face_encodings(imgabhi)[0]
#cv2.rectangle(imgabhi,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,225),2)

#faceLocTest =  face_recognition.face_locations(imgTest)[0]
#encodeTest =face_recognition.face_encodings(imgTest)[0]
#cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,225),2)

#results = face_recognition.compare_faces([encodeAbhi],encodeTest)


#faceDis= face_recognition.face_distance([encodeAbhi],encodeTest)








