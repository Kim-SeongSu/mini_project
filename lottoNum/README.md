# 연금복권 예측 프로그램

## 개요
이 프로젝트는 연금복권 당첨 번호를 예측하는 프로그램입니다. <br>크롤링부터 데이터 전처리, 모델 학습 및 예측까지의 전 과정을 포함하고 있습니다.<br><br>

## 프로젝트 구조
project-directory/
│
├── data/                    # 크롤링한 데이터 파일
├── venv/                    # 가상 환경 디렉토리
├── dist/
│    └── main.exe
├── crawler.py               # 데이터 크롤링 스크립트
├── preprocess.py            # 데이터 전처리 스크립트
├── model.py                 # 모델 학습 및 예측 스크립트
├── main.py                  # 메인 실행 파일
├── requirements.txt         # 의존성 파일
├── LICENSE                  # # 라이선스 파일
└── README.md                # 프로젝트 설명 파일

<br><br>

## 개발 환경 설정
- 0. 프로젝트 디렉토리 경로
**path/to/your/project** <br>

- 1. 가상 환경 생성
**python -m venv venv** <br>

- 2. 가상 환경 활성화
**source venv/Scripts/activate  # Windows** <br>
**source venv/bin/activate  # MacOS/Linux** <br>

- 3. 라이브러리 설치
**pip install requests pandas scikit-learn** <br>

- 4. `requirements.txt` 파일 생성 (선택 사항)
**pip freeze > requirements.txt** <br>

- 5. Python 스크립트에서 라이브러리 임포트
**echo "import requests\nimport pandas as pd\nfrom sklearn.ensemble import RandomForestClassifier\n" > script.py** <br>

- 6. Python 스크립트 실행
**python script.py** <br><br>