import cv2

# face classifier:
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

# grab webcam feed:
webcam = cv2.VideoCapture(0)

# set window size:
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# show current frame
while True:
	# read current frame from webcam video stream:
	(successful_frame_read, frame) = webcam.read()

	# if there's an error, abort:
	if not successful_frame_read:
		break

	# change to grayscale:
	frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect faces first:
	faces = face_detector.detectMultiScale(frame_grayscale, minNeighbors=20)

	# run face detection within each of those faces:
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

		# get sub frame (using numpy N-dimensional array slicing):
		the_face = frame[y:y+h, x:x+w]

		face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

		smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=4.0, minNeighbors=30)

		for (xx, yy, ww, hh) in smiles:
			cv2.rectangle(the_face, (xx, yy), (xx + ww, yy + hh), (0, 0, 255), 5)

		# label this text as smiling:
		if len(smiles) > 0:
			cv2.putText(
				frame, 'SMILING', (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255)
			)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
		else:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

	# show current frame:
	cv2.imshow('Smile Detector', frame)

	# display:
	key = cv2.waitKey(10)

	if key == 27:
		break

# cleanup:
webcam.release()
cv2.destroyAllWindows()

# code run without errors:
print('Code is done')
