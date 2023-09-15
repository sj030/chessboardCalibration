import cv2 as cv
import sys

cap = cv.VideoCapture(1, cv.CAP_DSHOW)
step = 2
imgNum = 0
temp = 0

if not cap.isOpened():
    sys.exit("The camera is not connected")

while imgNum < 250:
    ret, frame = cap.read()

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다. ')
        break

    cv.imshow('Video display', frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

    if temp == step:
        cv.imwrite('images/img' + str(imgNum) + '.png', frame)
        print(str(imgNum) + " : image saved!")
        imgNum += 1
        temp = 0
    else:
        temp += 1

cap.release()
cv.destroyAllWindows()