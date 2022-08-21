import cv2
import pytesseract
import TextExtraction

img = cv2.imread("TextImage/EngText1.jpg")

print(img.shape)
cv2.imshow("Text", img)

# return_ImgStr(cvImage)
s = TextExtraction.return_ImgStr(img)
print(s)

# return_ImgData(cvImage)
s = TextExtraction.return_ImgData(img)
print(s)

# Draw_a_Box(cvImage)
box = TextExtraction.Draw_a_Box(img)
cv2.imshow("Box", box)

cv2.imshow("Text2", img)

cv2.waitKey(0)