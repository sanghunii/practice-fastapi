from fastapi import FastAPI

##pydantic - for validation
from pydantic import BaseModel
from pydantic import Field

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class DataInput(BaseModel):
    name: str



##해당 get을 이용해서 요청을 보낼 때 요청방식은 아래와 같다.
##http://127.0.0.1:8000/items/a?skip=0&limit=10
@app.get("/items/{item_id}")
def read_item(item_id: str, skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/")
def home():
    return {"Hello": "GET"}

@app.post("/")
def home_post(data_request: DataInput):
    return {"Hello": "POST", "msg": data_request.name}