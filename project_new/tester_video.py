import os
import cv2
import numpy as np
import faceRecognition as fr
import requests
from gtts import gTTS
from playsound import playsound
import excel
import requests
import json
import time
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:/Users/vrush/PycharmProjects/project_new/trainingData.yml')#Load saved training data

name={

}
enroll={

}

res=requests.get(url="http://localhost:3000/users/get_student_data")
resdata=json.loads(res.text)
# print(resdata)
for i in range(len(resdata)):
    name[resdata[i]['rollno']]=resdata[i]['name']
    enroll[resdata[i]['rollno']] = resdata[i]['enrollment']

# name = {7063 : "kirtan" , 59 : "vrushang"}
print(enroll)
print(name)
done={

}
cap=cv2.VideoCapture("multiple new.mp4")
# cap=cv2.VideoCapture(0)
count=0

count1=0
temp_name=""
while True:

    ret,test_img=cap.read()# captures frame and returns boolean value and captured image
    faces_detected,gray_img=fr.faceDetection(test_img)
    for (x,y,w,h) in faces_detected:
      cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+w, x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
        # print("confidence:",confidence)
        # print("label:",label)
        sem=str(label)[0]
        rollno=str(label)[1:]
        # print("type label:",type(label))
        fr.draw_rect(test_img,face)
        predicted_name=name[int(rollno)]


        # print("predicted",predicted_name)
        font = cv2.FONT_HERSHEY_SIMPLEX

        t = time.localtime()
        hour = time.strftime("%H", t)
        min = time.strftime("%M", t)
        if (int(hour) > 12):
            hour = int(hour)
            hour = hour - 12
        main_time = str(hour) + ":" + str(min)
        # if ((main_time >= "8:40" and main_time <= "8:50") or (main_time >= "9:45" and main_time <= "9:50") or (main_time >= "11:30" and main_time <= "11:35") or (main_time >= "12:30" and main_time <= "12:35") or (main_time >= "1:30" and main_time <= "1:35") or (main_time >= "4:00" and main_time <= "6:35")):
        if confidence > 70:
           #fr.put_text(test_img,predicted_name,x,y)
           if (temp_name != predicted_name):
               temp_name = predicted_name
               count=0
           else:

               count = count + 1
               print("temp name:", temp_name," count:",count)
           if((str(predicted_name)) not in done):

               if(count>10):
                   excel.output('attendance', 'class1', int(rollno), predicted_name, 'yes');
                   count1=count1+1
                   done[str(predicted_name)]=str(predicted_name)
                   print("Attendance done of:",str(predicted_name))
                   data = {
                       "name": predicted_name,
                       "enroll": enroll[int(rollno)],
                       "time": main_time,
                       "rollno": rollno
                   }
                   res_log = requests.post(url="http://localhost:3000/users/attendance_log", data=data)
                   res = requests.post(url="http://localhost:3000/users/add_attendance", data=data)
                   resdata = res.text

           # print(sem)
           cv2.putText(test_img,predicted_name, (x, y), font, 1, (200, 255, 255))
           cv2.imwrite('C:/Users/vrush/PycharmProjects/project_new/attendance_files/detected_faces/' + sem+str(rollno)+'.jpg', test_img)

           # cv2.imwrite(
           # 'C:/Users/vrush/PycharmProjects/project_new/attendance_files/images/' + hour + " " + min + " " + sec + " " + '.jpg',
           # test_img)

        else:
            t = time.localtime()
            hour = time.strftime("%H", t)
            min = time.strftime("%M", t)
            sec = time.strftime("%S", t)
            if(int(hour)>12):
                hour=int(hour)
                hour=hour-12

            cv2.putText(test_img, 'Unknown', (x, y), font, 1, (200, 255, 255))
            cv2.imwrite('C:/Users/vrush/PycharmProjects/project_new/attendance_files/undetected_faces/' +str(hour)+" "+min+" "+sec+" "+ '.jpg', test_img)
        # else:
        #     print("not")
        # if (count >= 100):
        #     break
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Detecting Live ',resized_img)
    # if ((main_time >= "8:40" and main_time <= "8:50") or (main_time >= "9:45" and main_time <= "9:50") or (main_time >= "11:30" and main_time <= "11:35") or (main_time >= "12:30" and main_time <= "12:35") or (main_time >= "1:30" and main_time <= "1:35") or (main_time >= "4:00" and main_time <= "6:35")):
    # if count>=10:
        # playsound('thanks.mp3')
        # print("In if")
        # print(predicted_name)
        # print(enroll[int(rollno)])
        # data = {
        #     "name": predicted_name,
        #     "enroll": enroll[int(rollno)],
        #     "time":main_time,
        #     "rollno":rollno
        # }
        # res_log=requests.post(url="http://localhost:3000/users/attendance_log", data=data)
        # res = requests.post(url="http://localhost:3000/users/add_attendance", data=data)
        # resdata = res.text
        # if(resdata):
        #     print("attendance done")
        #     # break
        # else:
        #     print("attendance exist")
            # break
        # break
    # else:
    #     print("else")
    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break


print("count:",count)
cap.release()
cv2.destroyAllWindows()

