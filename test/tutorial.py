from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{items_id}")
def root(items_id: int):
    return {"items_id": f"return value is {items_id}"}