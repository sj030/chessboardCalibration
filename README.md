# Camera Calibration Using OpenCV
<br>
Python scripts for camera calibration.<br>
<br>
step
1. getImages.py 실행 <br>
   input : 웹캠 비디오 (카메라 고정. chessboard를 최대한 다양한 각도, 위치에서 움직이며 촬영) <br>
   output : images 폴더의 250장 이미지.<br>
   켈리브레이션에 사용할 이미지 수집.<br>
   (step 조절 가능. q키 종료. images 폴더 생성 필요)<br>
2. calibration.py 실행<br>
   input : chessboard images<br>
   output : json file with camera matrix and dist data (files/mtx.json 파일 생성)<br>
   체스 보드 모서리 수 설정 필요. <br>
3. getVideo.py 실행<br>
   input : 웹캠 비디오 (chessboard를 고정. 카메라를 움직이며 촬영)<br>
   output : original.mp4<br>
   q키를 눌러서 종료 가능.<br>
4. getResult.py 실행<br>
   input : 3의 original.mp4<br>
   output : 체스보드의 (0,0,0)에 axis가 고정된 영상<br>
<br><br>

result Example
<br>


https://github.com/sj030/Calibration_withchessboard/assets/127181878/bd12f811-2359-4f4e-b7c7-69dc2dfbd267

