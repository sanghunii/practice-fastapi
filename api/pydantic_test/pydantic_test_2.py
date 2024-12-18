from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel, Field

class Movie(BaseModel):
    mid: int
    genre: str
    rate: Union[int, float] #rate는 int아니면 float
    tag: Optional[str] = None
    date: Optional[datetime] = None
    some_variable_list: List[int] = [] 


class User(BaseModel):
    '''
    gt: 설정된 값보다 큰
    ge: 설정된 값보다 크거나 같은
    lt: 설정된 값보다 작은
    le: 설정된 값보다 작거나 같은. 
    '''
    uid: int
    name: str = Field(min_length=2, max_length=7) ##ORM에서 DB Table class로 정의할 때랑 비슷함
    age: int = Field(gt = 1, le=130)


tmp_movie_data = {
    'mid': '1',
    'genre': 'action',
    'rate': '1.5',
    'tag': None,
    'date': '2024-12-18 18:45:11'
}

tmp_user_data = {
    'uid': '100',
    'name': 'soojin',
    'age': '12'
}

tmp_movie = Movie(**tmp_movie_data)
tmp_user_data = User(**tmp_user_data)
print(tmp_movie.json())
print(tmp_user_data.json())