# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:17:31 2019

@author: saw-b
"""

import cv2
import Face_Detection as detect

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

