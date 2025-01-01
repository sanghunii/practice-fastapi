## sqlalchemy 써서 테이블 만들기
## DB - PostgreSQL사용하기 (DB name : test-db)

import os 
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# 환경변수 값들 불러오기
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)



##postgresql이랑 연결하기 
DB_USER = os.environ.get('db_user')
DB_PASSWORD = os.environ.get('db_password')
DB_HOST = os.environ.get('db_host')
DB_PORT = os.environ.get('db_port')
DB_DATABASE = os.environ.get('db_database')


SQLALCHEMY_DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

#만들어놓은 DB랑 연결해주는 engine 만들기 
engine = create_engine(SQLALCHEMY_DB_URL, echo=False)

Base.metadata.create_all