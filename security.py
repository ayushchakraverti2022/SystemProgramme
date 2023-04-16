import face_recognition
import cv2
import os
import numpy as np


vcapture=  cv2.VideoCapture(0)

AuthUserImage = face_recognition.load_image_file("ayush.jpg")
AuthUserImage_encoding = face_recognition.face_encodings(AuthUserImage)[0]
knowfaceEncoding = [AuthUserImage_encoding]
knownfaceName = ["ayush"]
facelocation = []
faceencodings = []
s = True


while True:
    _,frame = vcapture.read()
    smallframe = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_smallframe = smallframe[:,:,::-1]
    if s:
        facelocation = face_recognition.face_locations(rgb_smallframe)
        faceencodings = face_recognition.face_encodings(rgb_smallframe,facelocation)
        facename =[]
        for faceencoding in faceencodings:
            matches = face_recognition.compare_faces(knowfaceEncoding,faceencoding)
            names = ""
            facedistance = face_recognition.face_distance(knowfaceEncoding,faceencoding)
            best_matches_index =  np.argmin(facedistance)
            if matches[best_matches_index]:
                names = knownfaceName[best_matches_index]          

            if names in knownfaceName:
                os.system("shutdown /a")
            else:
               os.system("shutdown /s -t 10")

   
    if cv2.waitKey(1)&0xff==ord('q'):
        break
vcapture.release()
cv2.destroyAllWindows()
