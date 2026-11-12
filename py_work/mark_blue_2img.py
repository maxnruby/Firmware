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
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
_, bin = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = None
largest_area = 0
COLOR = (0, 255, 0)
for cnt in contours:                # find largest blue object
    area = cv2.contourArea(cnt)
    if area > largest_area:
         largest_area = area
         largest_contour = cnt
if largest_contour is not None:
    #if largest_area > 500:  # draw only larger than 500
        x, y, width, height = cv2.boundingRect(largest_contour)
        cv2.rectangle(src, (x, y), (x + width, y + height), COLOR, 2)
    
while True:
    cv2.imshow("origin",src)       # show original img

    k = cv2.waitKey(10) & 0xFF
        
    if k == 27:
        break
        
cv2.destroyAllWindows()
cv2.imwrite('blue.png', res)
