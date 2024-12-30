## Create GET and POST fastapi and test

##improt fastapi
from fastapi import FastAPI
##CORS
from starlette.middleware.cors import CORSMiddleware

##for use DB (+ ORM)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
##from sqlalchemy_declarative import Base, Address, Person
from sqlalchemy_declarative import Base, Address, Person

##FastAPI를 이용하기 위한 준비
app = FastAPI()

##CORS
origins = [
    "http://localhost:3001",
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

실제 fastapi logic에 전달되는 url은 아래와 같다.
/person?id={int값}
"""
@app.get("/person", status_code=200)
##async def get_data(id: int):
def get_data(id: int):
    DBSession = sessionmaker(bind = engine)  ##connect DB Session
    session = DBSession() ##Open DB session.
    res = session.get(Person,id)
    session.close() ##close db session.

    return {'person': res.name}


@app.post("/new_person", status_code=201)
async def post_data(request: str):
    DBSession = sessionmaker(bind=engine) ##connect DB Session
    session = DBSession()
    new_person = Person(name = request.name)
    session.add(new_person)
    session.commit()
    ##DB에 새로운 행을 삽입(INSERT)하게 되면 ORM이 각각의 새 객체에 대하여 primary key식별자를 검색할 수 있는 효과를 가져온다. 
    ##이에 아래와 같이 INSERT한 객체를 DB상 primary key를 추적할 수 있다.
    id = new_person.id
    session.close() ##close DB session
    
    return {'id': id}