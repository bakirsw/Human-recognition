# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 11:44:38 2019

@author: saw-b
"""
import cv2
import face_recognition

def face_detection(img, img_name):

    face_cascade = cv2.CascadeClassifier('/Users/bakirsawalha/Documents/recognition/Human-recognition/data/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/Users/bakirsawalha/Documents/recognition/Human-recognition/data/haarcascade_eye.xml')
    fullbody_cascade = cv2.CascadeClassifier('/Users/bakirsawalha/Documents/recognition/Human-recognition/data/haarcascade_fullbody.xml')
    upperbody_cascade = cv2.CascadeClassifier('/Users/bakirsawalha/Documents/recognition/Human-recognition/data/haarcascade_upperbody.xml')
    lowerbody_cascade = cv2.CascadeClassifier('/Users/bakirsawalha/Documents/recognition/Human-recognition/data/haarcascade_lowerbody.xml')
    leftear_cascade = cv2.CascadeClassifier('/Users/bakirsawalha/Documents/recognition/Human-recognition/data/haarcascade_mcs_leftear.xml')
    rightear_cascade = cv2.CascadeClassifier('/Users/bakirsawalha/Documents/recognition/Human-recognition/data/haarcascade_mcs_rightear.xml')



    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 1)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 3)
    fullbodies = fullbody_cascade.detectMultiScale(gray, 1.1, 1)
    upperbodies = upperbody_cascade.detectMultiScale(gray, 1.1, 1)
    lowerbodies = lowerbody_cascade.detectMultiScale(gray, 1.1, 1)
    leftears = leftear_cascade.detectMultiScale(gray, 1.05, 1)
    rightears = rightear_cascade.detectMultiScale(gray, 1.05, 1)
    
    face_counter = 0
    eye_counter = 0
    fullbody_counter = 0
    upperbody_counter = 0
    lowerbody_counter = 0
    leftear_counter = 0
    rightear_counter = 0
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        face_counter += 1
        
    for (x,y,w,h) in eyes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        eye_counter += 1
        
    for (x,y,w,h) in fullbodies:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        fullbody_counter += 1
    
    for (x,y,w,h) in upperbodies:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        upperbody_counter += 1
    
    for (x,y,w,h) in lowerbodies:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        lowerbody_counter += 1
    
    for (x,y,w,h) in leftears:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,40,125),2)
        leftear_counter += 1
    
    for (x,y,w,h) in rightears:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,40,125),2)
        rightear_counter += 1
      
    print('Anzahl an Gesichtern: ' , face_counter)
    print('Anzahl an Augen: ' , eye_counter)
    print('Anzahl an Körper: ' , fullbody_counter)
    print('Anzahl an Oberkörper: ' , upperbody_counter)
    print('Anzahl an Unterkörper: ' , lowerbody_counter)
    print('Anzahl an linke Ohren: ', leftear_counter)
    print('Anzahl an rechte Ohren: ', rightear_counter)
    
    merkmale = []
    merkmale.append(face_counter)
    merkmale.append(eye_counter)
    merkmale.append(fullbody_counter)
    merkmale.append(upperbody_counter)
    merkmale.append(lowerbody_counter)
    merkmale.append(leftear_counter)
    merkmale.append(rightear_counter)
    
    return merkmale

