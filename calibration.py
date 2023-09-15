import numpy as np
import cv2 as cv
import glob
import json

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 체스 보드의 모서리 수 설정
CHECKERBOARD = (5, 4)

# 세계 좌표계 기준 체스 보드 좌표 ( z는 항상 0 )
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = (np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)) * 5
print(objp)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('Images\*.png')
for image in images:
    img = cv.imread(image)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, CHECKERBOARD, None) # corners에 특정 상수 넣었을 때, 값이 달라지는지

    #If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        # chess 점들의 2D상 좌표 획득
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria) # 이 함수 이해 못함 ;;
        imgpoints.append(corners2) # 근데 보드의 점의 2D상 좌표를 저장 하는 것 같군

         # Draw and display the corners
#         cv.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
#         cv.imshow('img', img)
#         cv.waitKey(500)
#
# cv.destroyAllWindows()
print("done get coner")

# 2D, 3D 상의 좌표 획득 완료. 이를 기반으로 calibration, matixs 획득 진행
ret, mtx, dist, rVecs, tVecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("done calibration")
file_path = 'files/mtx.json'
# Convert objpoints and imgpoints to lists for JSON serialization
objpoints_list = [op.tolist() for op in objpoints]
imgpoints_list = [[ip_point.tolist() for ip_point in ip] for ip in imgpoints]

# Create a dictionary to hold all the data
data = {
    'mtx': mtx.tolist(),
    'dist': dist.tolist(),
    'rVecs': [rvec.tolist() for rvec in rVecs],
    'tVecs': [tvec.tolist() for tvec in tVecs],
    'objpoints': objpoints_list,
    'imgpoints': imgpoints_list
}

# Save the dictionary to a JSON file
with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("done making file")

import winsound as sd
def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 5000     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)
beepsound()