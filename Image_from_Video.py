# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:14:26 2019

@author: saw-b
"""

import cv2 
  
# Read the video from specified path 
def Image_from_Video(video):

    cam = cv2.VideoCapture(video) 
    find_string = video.find('.mp4')
    frame_string = video[0:find_string]
    # frame 
    currentframe = 0
    img = [] 
    data_name = []
    
    while(True): 
          
        # reading from frame 
        ret,frame = cam.read() 
      
        if ret: 
            # if video is still left continue creating images 
            name_help = frame_string + str(currentframe)
            currentframe += 1
            img.append(frame)
            data_name.append(name_help)
        else: 
            break
      
    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows()     
    
    
    return img, data_name, currentframe
