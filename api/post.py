from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/{item_id}")
def read_item(item_id: str, skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]