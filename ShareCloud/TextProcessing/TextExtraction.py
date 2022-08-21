import cv2
import pytesseract

'''
All functions for extracting text from image.
'''

def return_ImgStr(cvImage):
    return pytesseract.image_to_string(cvImage)

def return_ImgData(cvImage):
    return pytesseract.image_to_data(cvImage)

def Draw_a_Box(cvImage):
    imgInfo = return_ImgData(cvImage)
    cvImage = cvImage.copy()

    for i, line in enumerate(imgInfo.splitlines()):
        if i != 0:
            line = line.split()
            if len(line) == 12:
                left, top, width, height = int(line[6]), int(line[7]), int(line[8]), int(line[9])
                cv2.rectangle(cvImage, (left, top), (left+width, top+height), (0,0,255), 1)
    return cvImage