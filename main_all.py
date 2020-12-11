# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:21:32 2019

@author: ael-k
"""
import cv2
import csv
import Face_Detection as detect
import Image_from_Video as iv
import Number_of_Persons as num
import Audio_from_Video as av

image_video_name = 'Hochzeit.mp4'

merkmale = [['faces', 'eyes', 'bodies', 'upperbodies', 'lowerbodies', 'leftears', 'rightears']]

if image_video_name.find('.mp4') > 0:
    image, data_name, counter = iv.Image_from_Video(image_video_name)
    for x in range(0, counter):
        merkmale.append(detect.face_detection(image[x], data_name[x]))
    data_find = image_video_name.find('.mp4')
    data_name = image_video_name[0:data_find]
    audio = av.audio_from_video(data_name)

elif image_video_name.find('.jpg') > 0:
    image = cv2.imread(image_video_name)
    data_find = image_video_name.find('.jpg')
    data_name = image_video_name[0:data_find]
    merkmale.append(detect.face_detection(image, data_name))
    
elif image_video_name.find('.png') > 0:
    image = cv2.imread(image_video_name)
    data_find = image_video_name.find('.png')
    data_name = image_video_name[0:data_find]
    merkmale.append(detect.face_detection(image, data_name))

csv_data_name = data_name + '.csv'
csv_data = open(csv_data_name, 'w')
with csv_data as csvfile:
    filewriter = csv.writer(csv_data)
    for row in merkmale:
        filewriter.writerow(row)

anzahl = num.number(merkmale)
print(anzahl)
            
