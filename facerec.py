import numpy as np
import cv2
import pickle
import random
from random import seed
from random import choice
def verify():

    name = "Unknown"
    count = 0
    seq = [33,44,55,66,77,88,99,111]
    face_cascade = cv2.CascadeClassifier('C:\\Users\\Admin\\buttonpython\\buttonpython\\cascades\\data\\haarcascade_frontalface_alt2.xml')
    eye_cascade = cv2.CascadeClassifier('C:\\Users\\Admin\\buttonpython\\buttonpython\\cascades\\data\\haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('C:\\Users\\Admin\\buttonpython\\buttonpython\\cascades\\data\\haarcascade_smile.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("C:\\Users\\Admin\\buttonpython\\buttonpython\\trainner.yml")

    labels = {"person_name": 1}
    with open("C:\\Users\\Admin\\buttonpython\\buttonpython\\labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    val  = choice(seq)
    num = val
    print(val)
    while(True):

        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=6)
        for (x,y,w,h) in faces:
            #print(x,y,w,h)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            id_,conf = recognizer.predict(roi_gray)
            if conf>=60 and conf<=97:
                #print(id_)
                #print(labels[id_])
                #font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255,255,255)
                stroke = 2
                cv2.putText(frame, name, (x,y), font, .8, color, stroke, cv2.LINE_AA)
            
            color =  (0,255,0)
            stroke = 2
            width = x+w
            height = y+h
            cv2.rectangle(frame,(x, y), (width, height), color, stroke)
            cv2.putText(roi_color,'Face Detected', (0,10), font, .4, (255,200,0), stroke, cv2.LINE_AA)
            cv2.putText(frame, 'Smile-Stop-Smile: '+str(val), (0,20), font, .8, (200,0,255), 2, cv2.LINE_AA)
            cv2.putText(frame, 'Please Maintain a Distance of 1-2 feet from the camera ', (0,40), font, .4, (0,0,255), 1, cv2.LINE_AA)
            eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=9)        
            for (ex, ey, ew, eh) in eyes:
                    #cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                    cv2.putText(roi_color, 'Eye_Detected', (0,30), font, .4, (200,255,255), 2, cv2.LINE_AA)

            smile = smile_cascade.detectMultiScale(roi_gray, scaleFactor= 1.54, minNeighbors=6, minSize=(24,24))
        
            for (xx, yy, ww, hh) in smile:
                    cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 255, 0), 2)
                    cv2.putText(roi_color, 'Smile', (0,50), font, .5, (200,0,255), 2, cv2.LINE_AA)
                    count += 1
        
        if(count>=num): 
            cv2.putText(frame, 'Done: Hit Escape', (0,50), font, .8, (0,0,255), 2, cv2.LINE_AA) 
            break
        #elif()




        cv2.imshow('frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return name

#verify()
