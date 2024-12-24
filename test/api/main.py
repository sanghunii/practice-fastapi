from fastapi import FastAPI #for use FastAPI
from starlette.middleware.cors import CORSMiddleware #for solve CORS problem

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    rsenet = "resnet"
    lenet = "lenet"

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

@app.get("/test/{id}")
async def test(id : int):
    return {id}



###Test code
@app.get("/models/{model_name}")
async def get_model(model_name : ModelName): ##python typehint사용
    if model_name is ModelName.alexnet:
        return {"model_name" : model_name, "message": "Deep Learning FTW"}
    if model_name is ModelName.lenet:
        return {"model_name" : model_name.value}
    
    return {"model_name" : model_name, "message": "Have some residuals"}