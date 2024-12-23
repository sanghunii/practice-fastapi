##improt fastapi
from fastapi import FastAPI

##for use DB (+ ORM)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .database.sqlalchemy_declarative import Base, Address, Person


app = FastAPI()


"""
1.
여기다가 DB(SQlite)에서 데이터 가져와서 
react test page연결해서
데이터 잘 가져오는지 테스트

2. 
fastapi프로젝트 하나 새로 생성

DB - PostGreSQL만들기

API CRUD 다 구현

postgreSQL이랑 연동해서 CRUD잘 돌아가는지 테스트


3.
postgreSQL구현한거에다가 
celery + redis추가 



3번까찌 하면 온르할 거 끝
"""