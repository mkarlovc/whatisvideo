import random
import cv2
import numpy as np
import glob

img_array = []
size_g = (0,0)

print("read frames")
names = []
for filename in glob.glob('./out/frames/frame*.jpg'):
    print("name:")
    print(filename)
    names.append(filename)

frames_n = len(names)

print("random chunks")
for i in range(60):
    print i
    index = random.randint(1, frames_n-20)
    length = random.randint(10, 100)
    for j in range(length):
        fn = "./out/frames/frame_" + str(index+j) + "_.jpg"
        img = cv2.imread(fn)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
        size_g = size

print("video writer")
out = cv2.VideoWriter('./out/videos/random_1_100frames.avi', cv2.VideoWriter_fourcc(*'DIVX'), 20, size)
 
print("write array")
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
