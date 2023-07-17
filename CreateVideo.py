import os
import cv2

path = "Images/"

image = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    if ext in ['.gif', '.png', '.jpg', '.pdf', '.jpeg']:
        file_name = path+"/"+file
        
        print(file_name)

        image.append(file_name)

print(len(image))
count = len(image)

frame = cv2.imread(image[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    frame = cv2.imread(image[i])
    out.write(frame)
    
out.release()
print("Done")


