'''
    0         pan left                  300   320         pan right                     640
  0 +------------------------------------+-----+-----+------------------------------------+
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |          tilt up                   | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
225 +------------------------------------+-----+-----+------------------------------------+ 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    |  
240 +------------------------------------+-----+-----+------------------------------------+ 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    |  
255 +------------------------------------+-----+-----+------------------------------------+ 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |          tilt down(tilt++)         | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    |  
480 +------------------------------------+-----+-----+------------------------------------+ 
import cv2
import numpy as np

# step2.카메라 열기 - 0은 기본 카메라를 의미
cap = cv2.VideoCapture(0)
"""
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
"""

# step3.무한 반복
while True:
    # 카메라 연결 여부(True/False)와 현재 프레임 이미지를 읽음
    retval, src = cap.read()
    
    # 만약 카메라가 연결되어 있지 않으면 while 반복문 종료
    if retval == False:
        break
    
    # 'frame'이란 창 이름으로 현재 프레임 출력
    
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) 
    lower_blue = np.array([100,100,120])          # range of blue
    upper_blue = np.array([150,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(src, src, mask=mask)
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
        if largest_area > 500:  # draw only larger than 500
            x, y, width, height = cv2.boundingRect(largest_contour)       
            cv2.rectangle(src, (x, y), (x + width, y + height), COLOR, 2)
            center_x = x + width//2
            center_y = y + height//2
            print("center: ( %s, %s )"%(center_x, center_y)) 
    
    
    cv2.imshow('frame', src)

    # 10초가 지나거나, ESC 키가 입력되면 while 반복문 종료
    if cv2.waitKey(10) == 27:
        break

# step4.카메라 닫고 모든창 종료
 
cap.release()

cv2.destroyAllWindows()