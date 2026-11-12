import cv2

src = cv2.imread('origin.png

while True:

    cv2.imshow('frame', src)

        # 10초가 지나거나, ESC 키가 입력되면 while 반복문 종료
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()