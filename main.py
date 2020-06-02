# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:21:32 2019

@author: saw-b
"""
import face_recognition
import cv2
import csv
import Face_Detection as detect
import Image_from_Video as iv
import Number_of_Persons as num

image_video_name = 'club1.jpg'

merkmale = [['faces', 'eyes', 'bodies', 'upperbodies', 'lowerbodies', 'leftears', 'rightears']]

if image_video_name.find('.mp4') > 0:
    image, data_name, counter = iv.Image_from_Video(image_video_name)
    for x in range(0, counter):
        merkmale.append(detect.face_detection(image[x], data_name[x]))
    data_find = image_video_name.find('.mp4')
    data_name = image_video_name[0:data_find]

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

img_name = 'club1'
img_help = img_name + '.jpg'
img = cv2.imread(img_help)

detect.face_detection(img, img_name)

screen_res = 1280, 720
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

print("Click 's' to save it and exit or ESC to exit")

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', window_width, window_height)

cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    img_help = img_name + '_detection.png'
    cv2.imwrite(img_help, img)
    cv2.destroyAllWindows()


           


