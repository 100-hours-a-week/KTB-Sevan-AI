# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # 접속할 데이터베이스의 경로와 인증 정보를 담은 문자열
# DATABASE_URL = "mysql+pymysql://root:@localhost:3306/fast_db"
# engine = create_engine(
#     DATABASE_URL, 
#     pool_size=20,          # 기본 커넥션 풀 크기
#     max_overflow=10,       # 최대 추가 커넥션 허용치
#     pool_recycle=3600      # 1시간마다 커넥션 재연결 (MySQL 타임아웃 방지)
# )
# # 데이터베이스와 물리적인 커넥션 풀을 관리하고 SQL 명령을 전달하는 통로 역할
# # 이제 연결할 준비는 완료
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # DB 세션을 생성하고 안전하게 닫아주는 Dependency Injection (의존성 주입) 함수
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import DATABASE_URL

# MySQL 연결 시에는 별도의 connect_args가 필요 없습니다.
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()