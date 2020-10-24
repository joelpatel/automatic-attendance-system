import os
import cv2
import numpy as np
import faceRecognition as fr
import time


#This module captures images via webcam and performs face recognition
# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read('C:/Users/vrush/PycharmProjects/project_new/trainingData.yml')#Load saved training data

# name = {0: "Donald Trump", 1: "Bill Gates",2: "Elon Musk", 3: "Jeff",4: "Obama",5:"Kirtan",6:"Vrushang",7:"Adesh"}
sem=input("Enter Semester of student:")
rollno=input("Enter rollno of student")

take_name=sem+" "+rollno
cap=cv2.VideoCapture(0)
os.mkdir('C:/Users/vrush/PycharmProjects/project_new/trainingImages/'+sem+" "+rollno)
num=1
while True:
    ret,test_img=cap.read()# captures frame and returns boolean value and captured image

    temp_img=test_img.copy()
    faces_detected,gray_img=fr.faceDetection(test_img)

    # num=num+1
    # if(num<=50):
    #     break
    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)



    font = cv2.FONT_HERSHEY_SIMPLEX
    for face in faces_detected:
        (x, y, w, h) = face
        roi_gray = gray_img[y:y + h, x:x + h]
        font = cv2.FONT_HERSHEY_SIMPLEX
        if(num==51):
            break


        if(num<=50):
            cv2.imwrite('C:/Users/vrush/PycharmProjects/project_new/trainingImages/' + take_name + '/' + str(num) + '.jpg',roi_gray)
            cv2.putText(test_img, str(num), (x, y), font, 1, (200, 255, 255))
            # time.sleep(1)


        num=num+1

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ', resized_img)
    cv2.waitKey(10)
    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break
    if num==51:
        break
# q
cap.release()
cv2.destroyAllWindows()


# take_name=input("Enter name of student")
# cap=cv2.VideoCapture(0)
# os.mkdir('C:/Users/vrush/PycharmProjects/project_new/trainingImages/'+take_name)
# num=1
# while True:
#     ret,test_img=cap.read()# captures frame and returns boolean value and captured image
#
#     # num=num+1
#     #     if(num<=50):
#     #         break
#     for (x, y, w, h) in test_img:
#         cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)