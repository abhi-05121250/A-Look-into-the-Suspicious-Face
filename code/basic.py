import cv2
import numpy as np 
import face_recognition
 
imgabhi = face_recognition.load_image_file('ImagesBasic/abhiraj.jpg')
imgabhi = cv2.cvtColor(imgabhi,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/test2.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc =  face_recognition.face_locations(imgabhi)[0]
encodeAbhi =face_recognition.face_encodings(imgabhi)[0]
cv2.rectangle(imgabhi,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,225),2)

faceLocTest =  face_recognition.face_locations(imgTest)[0]
encodeTest =face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,225),2)

results = face_recognition.compare_faces([encodeAbhi],encodeTest)

#print(results) shows the result that if the photo is true or not with the help of compare bit array which can be seeby blow code
faceDis= face_recognition.face_distance([encodeAbhi],encodeTest)
#we use the above line when we have more than one photo or video feed and wanted to check which is correct match so the lower the distance better the match is 
print(results,faceDis)

cv2.putText(imgTest,f'{results},{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,225),2)

cv2.imshow('abhiraj ',imgabhi)
cv2.imshow('test',imgTest)
cv2.waitKey(0)
cv2.waitKey(1)