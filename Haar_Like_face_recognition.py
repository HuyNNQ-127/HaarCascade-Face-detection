import cv2

face_cascade = cv2.CascadeClassifier(r'E:\Python\CV\HaarCascade-Face-detection\haar-like_model.xml')


cap = cv2.VideoCapture(r'E:\Python\CV\haar-like_dataset\test_video\classroom3.mp4')
#cap = cv2.VideoCapture(0) 

counter = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    #frame = cv2.resize(frame, (0, 0), fx=1.2, fy=1.2)
    frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    humans = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        counter +=1

    cv2.putText(frame, f'Number of Student: {counter}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    
    cv2.imshow('Student Detection', frame)
    
    counter = 0

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cap.release()
cv2.destroyAllWindows()

