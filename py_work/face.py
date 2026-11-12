import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml') 
cam = cv2.VideoCapture(0)
cam.set(3, 400)
cam.set(4, 350)

while(1):
	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

	print(len(faces)) 

	    
	for (x,y,w,h) in faces:
	    cv2.rectangle(frame,(x,y),(x+w,y+h),(300,300,300),3) 
	    for i in range(x, x + w):
	    	for j in range(y, y + h):
	    		for k in range(3):
		    		if(frame[j, i, k] + 50 > 255):
		    			frame[j, i, k] = 255
		    		else:
		    			frame[j, i, k] = frame[j, i, k] + 50

	
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('Q'):
		break

cam.release()
cv2.destroyAllWindows() # 창 닫기