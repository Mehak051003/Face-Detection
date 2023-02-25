import cv2 as cv
#reading image
img = cv.imread('Photos/man.jpg')
cv.imshow('Man',img)

#reading video

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)