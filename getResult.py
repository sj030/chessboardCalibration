# cm, mm 관련해서는 어디에 있는거지 ??
import cv2 as cv
import numpy as np
import json
import sys

#json file upload
file_path = 'files/mtx.json'

with open(file_path, 'r') as infile:
    loaded_data = json.load(infile)

# 체스 보드의 모서리 수 설정
CHECKERBOARD = (5, 4)

mtx = np.array(loaded_data['mtx']) # camera matrix, 내부 행렬
dist = np.array(loaded_data['dist'])

objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
grid_points = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2) * 5
objp[:, 0] = grid_points[:, 0]  # x 값을 첫 번째 열에 설정
objp[:, 2] = grid_points[:, 1]  # z 값을 세 번째 열에 설정
axis_length = 10
axis = np.float32([[0, 0, 0], [axis_length, 0, 0], [0, axis_length, 0], [0, 0, axis_length]]).reshape(-1,3,1)

CHECKERBOARD = (5, 4)

print(mtx)

# prepare for making mp4 file
input_video_path = 'video/original.mp4'
output_video_path = 'video/result.mp4'

video = cv.VideoCapture(input_video_path)

if not video.isOpened():
    sys.exit("The video is not connected")

fps = int(video.get(cv.CAP_PROP_FPS))
width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

print(f"Video FPS: {fps}, Width: {width}, Height: {height}")  # Debugging line

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter(output_video_path, fourcc, fps, (width, height))

frame_count = 0

# start making result
def draw(img, corners, imgpts):
    corner = tuple(imgpts[0].ravel().astype(int))
    img = cv.line(img, corner, tuple(imgpts[1].ravel().astype(int)), (255,0,0), 3)
    img = cv.line(img, corner, tuple(imgpts[2].ravel().astype(int)), (0,255,0), 3)
    img = cv.line(img, corner, tuple(imgpts[3].ravel().astype(int)), (0,0,255), 3)
    return img


while True:
    ret, frame = video.read()
    # 내부 행렬은 기존의 것 사용.
    # 각 이미지마다 카메라 포즈 찾기 > 이 포즈를 이용하여 axis를 그린다 ?
    # x-axis 빨간색, y-axis 초록색, z-axis 파란색 순. (RGB니까 당연히 XYZ 순). x-axis, z-axis는 체커보드에 붙어 있어야 하고, y-axis는 체커보드에 수직인 (툭 튀어나온) 선
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, (CHECKERBOARD[0], CHECKERBOARD[1]), None)

    if ret:
        # solvePnP를 사용하여 단일 프레임의 rvecs와 tvecs를 계산합니다.
        # get rvec, tvec
        sucess, rvec_single, tvec_single = cv.solvePnP(objp, corners, mtx, dist)

        # get axis's 2D point from 3D point
        imgpts, _ = cv.projectPoints(axis, rvec_single, tvec_single, mtx, dist)
        frame = draw(frame, corners, imgpts)

    out.write(frame)
    frame_count += 1
    print(f"Processed {frame_count} frames.")  # Debugging line

video.release()
out.release()
