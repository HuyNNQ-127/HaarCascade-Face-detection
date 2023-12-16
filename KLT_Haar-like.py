import cv2
import numpy as np

# KLT parameters
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

face_cascade = cv2.CascadeClassifier(r'E:\Python\CV\HaarCascade-Face-detection\haar-like_model.xml')

cap = cv2.VideoCapture(r'E:\Python\CV\haar-like_dataset\test_video\classroom3.mp4')
#cap = cv2.VideoCapture(0)

ret, old_frame = cap.read()
gray_old = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

output_width = 1000
output_height = 500


while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi = (x, y, w, h)

        mask = np.zeros_like(gray_frame)
        mask[y:y+h, x:x+w] = 255

        p0 = cv2.goodFeaturesToTrack(gray_frame, mask=mask, **feature_params)

        if p0 is not None:
            p0 = p0.reshape(-1, 1, 2).astype(np.float32)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # KLT
            p1, st, err = cv2.calcOpticalFlowPyrLK(gray_old, gray_frame, p0, None, **lk_params)

            good_new = p1[st == 1]

            roi_x, roi_y, roi_w, roi_h = cv2.boundingRect(good_new)
            roi = (roi_x, roi_y, roi_w, roi_h)

            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    resized_frame =  cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
    cv2.imshow('Tracking', resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
