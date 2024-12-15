##sqlalchemy tutorial code(1)
##Create Table

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

##declarative_base()는 데이터베이스 모델을 정의할 수 있는 기반 클래스를 만드는 역할을 한다. 
##declarative_base()는 함수이지만 클래스 객체를 반환한다. 
##즉 declarative_base()는 새로운 클래스 객체를 생성하는 함수이다. 
Base = declarative_base()

class Person(Base):
    __tablename__= 'person'
    ## Here we define columns for the table person
    ## Notice that each column is also a normal Python instance attribute 
    id = Column(Integer, primary_key=True) ##id를 primary key로 설정
    name = Column(String(250), nullable=False) ##String(250)이 django orm에서 max_length=250이랑 같은 거인 듯? 

class Address(Base):
    __tablename__='address'
    ##Here we define columns for the table address.
    ##Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False) ##nullable=False가 django ORM에서 null=True인듯
    

## Create an engine that stores data in the local directory's sqlalchemy_example.db file
engine = create_engine('sqlite:///sqlalchemy_example.db')

## Create all tables in the engine. This is equivalent to "Create Table"
## statements in raw SQL.
Base.metadata.create_all(engine)