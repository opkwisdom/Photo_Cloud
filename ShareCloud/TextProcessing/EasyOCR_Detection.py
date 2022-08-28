import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import easyocr
import cv2
import requests

def show_the_image(image, figsize=(12,10), title="Result"):
    plt.figure(figsize=figsize)
    plt.title(title)
    plt.imshow(image)
    plt.show()


def get_the_image(ImagePath):
    urlpattern = ["https://", "http://"]
    if type(ImagePath) == str:
        if ImagePath.startswith(urlpattern[0]) or ImagePath.startswith(urlpattern[1]):
            image_nparray = np.asarray(bytearray(requests.get(ImagePath).content), dtype=np.uint8)
            real_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        else:
            real_image = cv2.imread(ImagePath, 1)

    return real_image


def Text_Detection(img_fn):
    reader = easyocr.Reader(['en'], gpu=True)
    results = reader.readtext(img)
    results = pd.DataFrame(results, columns=["bbox", "text", "conf"])

    for bbox, text in zip(results["bbox"], results["text"]):
        top_left, bottom_right = bbox[0], bbox[2]
        cv2.rectangle(img, (int(top_left[0]), int(top_left[1])), (int(bottom_right[0]), int(bottom_right[1])),
                      (0, 255, 0), 2)
        cv2.putText(img, text, (int(top_left[0]), int(top_left[1])), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, color=(255, 0, 0), thickness=2)

    text_results = results["text"]
    return (img, text_results)


# 내장 사진과 url로 받아온 사진들 처리 과정 예시ㅅ
img_fns = ["TextImage/drake.png", "TextImage/EngText1.jpg", "TextImage/Phone Smarter.png",
          "TextImage/questions.jpg", "TextImage/yaytext.png",
          'https://user-images.githubusercontent.com/69428232/149087561-4803b3e0-bcb4-4f9f-a597-c362db24ff9c.jpg']

for img_fn in img_fns:
    img = get_the_image(img_fn)
    img, text_results = Text_Detection(img)

    show_the_image(img)
    print(text_results)

