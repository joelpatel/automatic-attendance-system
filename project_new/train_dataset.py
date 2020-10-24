import os
import cv2
import numpy as np
import faceRecognition as fr
import time

faces,faceID=fr.labels_for_training_data('C:/Users/vrush/PycharmProjects/project_new/trainingImages')
# print(faceID)
# print(faces)
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.save('trainingData.yml')