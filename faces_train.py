import numpy as np
import os
from PIL import Image
import cv2
import pickle


def trainit():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "images")
    face_cascade = cv2.CascadeClassifier('C:\\Users\\Admin\\buttonpython\\buttonpython\\cascades\\data\\haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()


    current_id = 0
    label_ids = {} #dict to store vals
    y_labels = []
    x_train = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
                path = os.path.join(root, file)
                label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
                #print(label,path)
                #y_labels.append(label)
                #x_train.append(path)
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]
                print(label_ids)
                pil_image = Image.open(path).convert("L")#greyscale conversion
                image_array = np.array(pil_image, "uint8")
                print(image_array)
                faces = face_cascade.detectMultiScale(image_array, scaleFactor = 1.57, minNeighbors = 5)

                for(x,y,w,h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)

    with open("C:\\Users\\Admin\\buttonpython\\buttonpython\\labels.pickle", 'wb') as f:
        pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainner.yml")

trainit()
