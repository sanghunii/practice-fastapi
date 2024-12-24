## FastAPI에서는 pydantic을 활용하여 들어오는 데이터와 나가는 데이터의 형태에 대한 검증을 한다.

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field

app = FastAPI()

class DataInput(BaseModel):
    name: str

class PredictOutput(BaseModel):
    prob: float
    prediction: int

@app.post("/pydantic", response_model=PredictOutput) ##response_model은 output_data의 형을 검증한다.
def pydantic_post(data_request: DataInput): ##data_request는 input_data의 형을 검증한다.
    return {"prob": 0.1, "prediction": "string"}
