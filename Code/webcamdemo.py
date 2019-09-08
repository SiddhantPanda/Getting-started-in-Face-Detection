import cv2
camera = cv2.VideoCapture(0)

while True:
	ret,frame = camera.read()
	if ret == False:
		continue

	face_detector = cv2.CascadeClassifier('template_data.xml')
	faces = face_detector.detectMultiScale(frame,1.3,5)

	for face in faces:
		x,y,w,h = face
		color = (0,240,0)
		cv2.rectangle(frame,(x,y),(x+w,y+h),color,6)
		
	cv2.imshow("Title",frame)
	cv2.waitKey(1)