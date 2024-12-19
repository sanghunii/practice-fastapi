from typing import List, Optional, Union
from datetime import datetime

from pydantic_settings import BaseSettings
from pydantic import Field, field_validator

class DBConfig(BaseSettings):
    ##env의 환경 변수 이름이랑 DBConfig class의 변수이름이랑 동일해야함. 
    db_host: str = Field(default='127.0.0.1', env='db_host')
    db_port: int = Field(default=3306, env='db_port')

    class Config:
        env_file = '.env_ex'

    @field_validator("db_port")
    def check_port(port_input):
        if port_input not in [3306, 8080]:
            raise ValueError("port error")
        return port_input
    


print(DBConfig().model_dump())