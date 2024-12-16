from fastapi import FastAPI #for use FastAPI
from starlette.middleware.cors import CORSMiddleware #for solve CORS problem

#SQLAlchemy-ORM
##여기서 데이터 가져와서 창 띄워보기 

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


##APIs
@app.get("/")
async def root():
    return {"message": "Test api"}

@app.get("/items")
async def root():
    return {"message": "this is items page"}

@app.get("/test")
async def test():
    return {"test FastAPI"}