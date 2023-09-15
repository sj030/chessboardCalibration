# Camera Calibration Using OpenCV
<br>
Python scripts for camera calibration.

step
1. getImages.py 실행
   input : 웹캠 비디오 (카메라 고정. chessboard를 최대한 다양한 각도, 위치에서 움직이며 촬영)
   output : images 폴더의 250장 이미지.
   켈리브레이션에 사용할 이미지 수집.
   (step 조절 가능. q키 종료. images 폴더 생성 필요)
2. calibration.py 실행
   input : chessboard images
   output : json file with camera matrix and dist data (files/mtx.json 파일 생성)
   체스 보드 모서리 수 설정 필요. 
3. getVideo.py 실행
   input : 웹캠 비디오 (chessboard를 고정. 카메라를 움직이며 촬영)
   output : original.mp4
   q키를 눌러서 종료 가능.
4. getResult.py 실행
   input : 3의 original.mp4
   output : 체스보드의 (0,0,0)에 axis가 고정된 영상


result Example


https://github.com/sj030/Calibration_withchessboard/assets/127181878/bd12f811-2359-4f4e-b7c7-69dc2dfbd267

