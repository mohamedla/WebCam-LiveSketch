import cv2
import numpy

def sketch(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray_blur = cv2.GaussianBlur(image_gray, (5,5), 0)
    canny_edges = cv2.Canny(image_gray_blur, 10, 70)
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if(cv2.waitKey(1) == 13): #13 is Enter Key
        break

cap.relase()
cv2.destroyAllWindows