import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # 데이터베이스 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy의 이벤트 처리하는 옵션. 얘는 파이보에 안필요해서 False로 비활성화 함.

# 여기까지 pybo.db라는 데이터베이스 파일을 프로젝트의 루트 디렉토리에 저장하는 것
# SQLite는 파이썬 기본 패키지에 포함됨. 소규모 프로젝트에서 사용하는 가벼운 파일을 기반으로 한 데이터베이스.
