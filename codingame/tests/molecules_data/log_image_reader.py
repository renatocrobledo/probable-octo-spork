import os
import cv2
import pytesseract


# get list of .png image files in the actual folder
# for each one try to represent as text, push it into a file and save the file with the same name of the image without extension

r = input('which file(s)?\n')

if r == 'all':
    stream = os.popen('ls | grep .png')
    image_files = stream.read().split('\n')[:-1]
else:
    image_files = [r]

for image in image_files:

    img = cv2.imread(image)
    text = pytesseract.image_to_string(img)
    text_file_name = image.split('.')[0]
    f = open(text_file_name,"w+")
    f.write(text)
    f.close()

