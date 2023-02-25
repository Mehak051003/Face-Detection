import cv2

haar_cascade = cv2.CascadeClassifier('haar_face.xml')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = haar_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


    cv2.imshow('img', img)

    esp = cv2.waitKey(30) & 0xff
    if esp==27:
        break
        
cap.release()