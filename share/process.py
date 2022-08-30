import os
import cv2
import easyocr
import pandas as pd
import pillow_heif
from hashlib import sha256
import googlemaps
import requests
import numpy as np



# image, video, text 분류하기
def ContType(file):
    def GetExt():
        _root, _ext = os.path.splitext(file)
        return _ext
    img = [".bmp", ".jpg", ".jpeg", ".png"]
    vid = []
    txt = []

    c_type = ""
    ext = GetExt()
    if ext in img:
        c_type = "img"
    elif ext in vid:
        c_type = "vid"
    elif ext in txt:
        c_type = "txt"

    return c_type


# pk로 전달받은 RoomNum 암호화
def RoomNumEncrypt(pk):
    encrypt = sha256(str(pk).encode()).hexdigest()
    return encrypt


def get_the_image(ImagePath):
    image_nparray = np.asarray(bytearray(requests.get(ImagePath).content), dtype=np.uint8)
    real_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
    return real_image


# Text 추출
def Text_Detection(img_fn):
    img = get_the_image(img_fn)
    reader = easyocr.Reader(['en'], gpu=True)
    results = reader.readtext(img)
    results = pd.DataFrame(results, columns=["bbox", "text", "conf"])

    # img에 텍스트 영역 표시
    for bbox, text in zip(results["bbox"], results["text"]):
        top_left, bottom_right = bbox[0], bbox[2]
        cv2.rectangle(img, (int(top_left[0]), int(top_left[1])), (int(bottom_right[0]), int(bottom_right[1])),
                      (0, 255, 0), 2)
        cv2.putText(img, text, (int(top_left[0]), int(top_left[1])), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, color=(255, 0, 0), thickness=2)

    text_results = results["text"]
    return (img, text_results)




