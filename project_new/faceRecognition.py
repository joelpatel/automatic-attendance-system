import cv2
import os
import numpy as np
import faceRecognition as fr

def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_haar_cascade=cv2.CascadeClassifier('C:/Users/vrush/PycharmProjects/project_new/HaarCascade/haarcascade_frontalface_default.xml')

    faces=face_haar_cascade.detectMultiScale(gray_img,1.2,10)

    return faces,gray_img


def labels_for_training_data(directory):
    faces=[]
    faceID=[]

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("skipping system file")
                continue
            id=os.path.basename(path)
            img_path=os.path.join(path,filename)
            print("img_path: ",img_path)
            print("id:",int(id))
            print("type id",type(id))
            test_img=cv2.imread(img_path)
            if test_img is None:
                print('Ing not loaded properly')
                continue
            faces_rect,gray_img=faceDetection(test_img)
            if len(faces_rect)!=1:
                continue #since we are assuming only single person  img are being fed to classifier

            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]
            faces.append(roi_gray)
            faceID.append(int(id))

    return faces,faceID


def train_classifier(faces,faceID):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer

def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=1)


def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,5,(255,255,255),6)
