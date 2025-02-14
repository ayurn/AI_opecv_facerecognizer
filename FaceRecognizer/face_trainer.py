import cv2
import numpy as np 
from PIL import Image
import os
path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def getImagesAndLables(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSample = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePaths).convert('l')
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSample.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,idsprint ("\n [INFO] Traning faces. It will take some seconfs. Wait....")

    faces,ids = getImagesAndLables(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer/trainer.yml')
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    
