#######20241213 FastAPI써서 DB에서 값 꺼내와서 front로 전달하기 -> 실패! ㅋ 



##improt fastapi
from fastapi import FastAPI
##CORS
from starlette.middleware.cors import CORSMiddleware

##for use DB (+ ORM)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
##from sqlalchemy_declarative import Base, Address, Person
from database.sqlalchemy_declarative import Base, Address, Person

##FastAPI를 이용하기 위한 준비
app = FastAPI()

##CORS
origins = [
    "http://localhos:3000",
]
##CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


##Connect DataBase(SQLite)
#create engine
engine = create_engine('sqlite:///sqlalchemy_example.db')
#Bind DataBase
Base.metadata.bind = engine


##API구현 
"""
API request url (request form)
"/person"

API resonse form
{person: response}

QueryParameter
id, int, 1이상 

실제 fastapi logic을 저달되는 url은 아래와 같다.
/person?id={int값}
"""
@app.get("/person")
##async def get_data(id: int):
def get_data(id: int):
    DBSession = sessionmaker(bind = engine)  ##connect sessionmaker to DataBase
    session = DBSession() ##Open DB session.
    res = session.get(Person,1)
    return {'person': res.name}