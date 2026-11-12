'''
    0         pan left(pan++)           300   320         pan right(pan--)               640
  0 +------------------------------------+-----+-----+------------------------------------+
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |          tilt up(tilt--)           | 
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
'''
import cv2
import numpy as np
import serial
import time

margin_x = 60
margin_y = 45

sp  = serial.Serial('COM3', 115200, timeout=0.125)
cascade_filename = 'haarcascade_frontalface_alt.xml'
# 모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)

def up():
    sp.write(b'w'); print("tilt up")
def down():
    sp.write(b's'); print("tilt down")
def left():
    sp.write(b'a'); print("pan_left")
def right():
    sp.write(b'd'); print("pan_right")


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 1 means 2nd camera

if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#cap.set(cv2.CAP_PROP_FRAME_FPS, 10)

def up():
    sp.write(b'w')
def down():
    sp.write(b's')   
def left():
    sp.write(b'a')
def right():
    sp.write(b'd')

while cap.isOpened():
    time.sleep(0.01)
    status, img = cap.read() #  read camera frame
    
    
    # 영상 압축
    img = cv2.resize(img,dsize=None,fx=1.0,fy=1.0)
    # 그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # cascade 얼굴 탐지 알고리즘 
    results = cascade.detectMultiScale(gray,            # 입력 이미지
                                           scaleFactor= 1.1,# 이미지 피라미드 스케일 factor
                                           minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                           minSize=(20,20)  # 탐지 객체 최소 크기
                                           )
    for box in results:
        x, y, w, h = box
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), thickness=2)
        center_x = x + w//2
        center_y = y + h//2
        print("center: ( %s, %s )"%(center_x, center_y))
        if center_x <= 320-margin_x:### need pan left ###########
                left()
        elif center_x > 320+margin_x: ### need pan right ########
            right()
        else:
            pass
        '''---------------------------------------------------'''
        if center_y <= 240-margin_y:### need tilt up ##########
            up()
        elif center_y > 240+margin_y: ### need tilt down ##########
            down()
        else: ########################### no need move tilt
            pass
    
    cv2.imshow('facenet',img)
    k = cv2.waitKey(10) & 0xFF

    if k == 27:
        break