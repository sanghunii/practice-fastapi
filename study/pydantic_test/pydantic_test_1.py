from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel

class Movie(BaseModel):
    mid: int
    genre: str
    rate: Union[int, float]  ##c/c++에서 봤던 union이랑 동일한 듯 int, float둘 중 하나의 데이터 값이 들어갈 수 있다.
    tag : Optional[str] = None ##tag는 string형이고 기본 값은 None
    date: Optional[datetime] = None ##date는 datetime형이고 기본 값은 None
    some_variable_list: List[int] = [] #임의의 변수. 리스트 값을 가지고 그 값들은 int여야 함. 기본 값은 []

tmp_data = {
    'mid': '1',
    'genre': 'action',
    'rate': '1.5',
    'tag': None,
    'date': '2024-12-18 15:46:07'
}

tmp_movie = Movie(**tmp_data)
print('tmp_movie : ', tmp_movie, '\n\n\n')
print('temp_movie_model_dump : ', tmp_movie.model_dump())