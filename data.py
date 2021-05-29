import os
import cv2

BASE_DIR = 'dataset/mp4'

count = 0

for mp4 in os.listdir(BASE_DIR):

    vidcap = cv2.VideoCapture(f'{BASE_DIR}/{mp4}')
    success,image = vidcap.read()

    while success:
        
        cv2.imwrite(f'dataset/frames/frame{count}.jpg', image)
        success,image = vidcap.read()

        print(f'Frame extracted: {count}')

        count += 1
