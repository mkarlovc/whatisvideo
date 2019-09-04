import random
import cv2
import numpy as np
import glob

img_array = []
size_g = (0,0)

names = []
for filename in glob.glob('./out/frames/frame*.jpg'):
    print("name:")
    print(filename)
    names.append(filename)

random.shuffle(names)
for filename in names[0:1200]:
    print("read:")
    print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    size_g = size

print("video writer")
out = cv2.VideoWriter('./out/videos/random_1frame.avi', cv2.VideoWriter_fourcc(*'DIVX'), 20, size)
 
print("write array")
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
