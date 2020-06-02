# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:04:32 2019

@author: ael-k
"""
from moviepy.editor import *

def audio_from_video(video_name):
    
    video = VideoFileClip(video_name)
    audio = video.audio
    data_find = video_name.find('.mp4')
    data_name = video_name[0:data_find]
    audio_name = data_name + '.wav'
    audio.write_audiofile(audio_name)

    return audio
