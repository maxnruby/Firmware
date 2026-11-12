import cv2
import numpy as np

src = cv2.imread("origin.png", cv2.IMREAD_COLOR)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)    # Convert from BGR to HSV

# define range of blue color in HSV
lower_blue = np.array([100,100,120])          # range of blue
upper_blue = np.array([150,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)     # make blue mask

# Bitwise-AND mask and original image
res = cv2.bitwise_and(src, src, mask=mask)      # apply blue mask
    
while True:
    cv2.imshow("origin",src)       # show original img
    cv2.imshow('blue', res)

    k = cv2.waitKey(10) & 0xFF
        
    if k == 27:
        break
        
cv2.destroyAllWindows()
cv2.imwrite('blue.png', res)
