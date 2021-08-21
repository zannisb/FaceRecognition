# FacialRecognition
📢 : OpenCV를 이용하여 제작한 얼굴 인식 기능으로, 후 AutoClassroom 이라는 웹사이트에 적용 예정입니다.


본 어플리케이션은 다음과 같은 과정을 통하여 이용하실 수 있습니다.


0. 준비해야 할 것

파이썬, OpenCV

OpenCV는 cmd에서

pip install opencv-python

pip install opencv-contrib-python

을 입력하여 다운받으실 수 있습니다.

만약 Numpy가 없는 경우 pip install numpy로 다운받아주시기 바랍니다.


1. 본 소스코드를 다운로드한 후, faces라는 이름으로 폴더를 생성해주시기 바랍니다.


2. FaceRecognition1.py를 실행해주시기 바랍니다.

창에 자신의 이름을 입력하면 faces 폴더 안에 자신의 이름의 폴더가 생성됩니다.

카메라를 열어 얼굴 인식 한 후, 300장의 jpg 파일을 생성합니다.


3. FaceRecognition2.py를 실행하면 생성된 사진을 가지고 학습합니다.

학습된 결과는 "자신의 이름.xml" 파일을 생성한 후 저장됩니다. 

이미 학습된 결과가 있을 경우 "Facial data of 사용자이름 already exists." 라고 뜰 것입니다.


4. 마지막으로 FaceRecognition3.py를 실행하면 학습된 결과를 모두 추합한 다음, 현재 사용자의 얼굴을 인식하여 저장된 데이터와 비교합니다.

유사도가 85이상일 경우 Unlocked라고 뜨며, 그 미만은 Locked라고 뜹니다.

얼굴이 인식되지 않을 경우 Face Not Found 라고 뜹니다.


✨앞으로의 계획 : 

본 어플리케이션을 웹사이트의 로그인창에 넣어 Unlocked가 2초 이상 지속될 경우 잠금해제를 시킬 예정입니다.

이를 통하여 학생들이 온라인 수업을 듣는 과정을 간소화하고 편리하게 할 수 있을 것으로 보입니다.
