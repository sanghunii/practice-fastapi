## get, post 만들기
## jjanggu_nextjs/app/fastapi_postgres 페이지에서 테스트

##improt fastapi
from fastapi import FastAPI
##CORS
from starlette.middleware.cors import CORSMiddleware

##for use DB (+ ORM)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
##from sqlalchemy_declarative import Base, Address, Person
from model import Base, Person


##pydnatic-for I/O data validation
from pydantic import BaseModel


##환경변수 
from dotenv import load_dotenv
import os

load_dotenv()


##FastAPI를 이용하기 위한 준비
app = FastAPI()

##CORS
origins = [
    "http://localhost:3000",
]

##CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


##Connect DataBase(postgreSQL)
##postgresql이랑 연결하기 
DB_USER = os.environ.get('db_user')
DB_PASSWORD = os.environ.get('db_password')
DB_HOST = os.environ.get('db_host')
DB_PORT = os.environ.get('db_port')
DB_DATABASE = os.environ.get('db_database')

#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname" 이걸 써야하나 .. ? 
#dsn = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}" 이걸 써야하나? 

SQLALCHEMY_DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

engine = create_engine(SQLALCHEMY_DB_URL, echo=False)
#Bind DataBase
Base.metadata.bind = engine


##validate input data (for post api)
class Item(BaseModel):
    name: str



##GET & POST API for postgreSQL
@app.get("/person", status_code=200)
##async def get_data(id: int):
def get_data(id: int):
    DBSession = sessionmaker(bind = engine)  ##connect DB Session
    session = DBSession() ##Open DB session.
    res = session.get(Person,id)
    session.close() ##close db session.

    return {'person': res.name}


@app.post("/new_person", status_code=201)
async def post_data(request: Item):
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