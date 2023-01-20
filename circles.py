import cv2 as cv
import numpy as np

img = cv.imread("C:\Users\kevin\OneDrive\Desktop\geometric-shapes-with-labels-set-12-basic-vector-31590940.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.medianBlur(gray_img, 5)
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, param1=100, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0, :] :
    # Outer Circles
    cv.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
    
    # Center
    cv.circle(img, (i[0], i[1]), 2, (0,255,0), 3)
    
cv.imshow("Circles", img)
cv.waitKey(0)
cv.destroyAllWindows