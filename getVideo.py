import cv2
import time
import datetime
import math

# 웹캠에서 영상을 가져오기 위한 객체 생성
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# 비디오 코덱 및 VideoWriter 객체 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID' depending on the platform
out = cv2.VideoWriter('video/original.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
start = time.time()
while (cap.isOpened()):
    end = time.time()
    set = (end - start)
    curtime = datetime.timedelta(seconds = set)
    print(curtime)
    ret, frame = cap.read()
    if ret:
        # 프레임을 동영상 파일에 쓰기
        out.write(frame)

        # 프레임을 화면에 보여주기
        cv2.imshow('frame', frame)

        # 'q' 키를 누르면 루프에서 벗어나기
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 모든 것을 정리
cap.release()
out.release()
cv2.destroyAllWindows()
