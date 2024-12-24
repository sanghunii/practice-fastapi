##BaseModel과 BaseSettings를 활용한 pydantic전체 예제 
##pydantic-fastapi.py에서 pydantic을 이용해서 API를 만든 예제코드를 확인해 보자.

from pydantic import field_validator, BaseModel, Field
from pydantic_settings import BaseSettings


##BaseSettings를 상속한 클래스를 이용해서 Settings와 관련된 것들(env등)에 대한 정의를 할 수 있음
class DBConfig(BaseSettings):
    db_host: str = Field(default='127.0.0.1', env='db_host')
    db_port: int = Field(default=3306, env = 'db_port')

    class Config:
        env_file = '.env_ex'
    
    #db_host에 알맞은 값이 들어갔는지 검증
    @field_validator("db_host")
    def check_host(host_input):
        if host_input == 'localhost':
            return "127.0.0.1"
        return host_input
    
    #db_port에 알맞은 값이 들어갔는지 검증
    @field_validator("db_port")
    def check_port(port_input):
        if port_input not in [3306, 8080]:
            ##ValueError 내가 설정할 수 있음.
            raise ValueError("port error")
        return port_input



##BaseModel을 상속받은 class를 이용해서 python type hint를 활용하여 input data의 검증을 손 쉽게 할 수 있음 
class ProjectConfig(BaseModel):
    project_name: str = "sanghoon"
    db_info: DBConfig = DBConfig()



data = {
    'project_name': 'hoon\'s project',
    'db_info': {
        'host': 'localhost',
        'port': 3306
    }
}

my_pjt = ProjectConfig()
print(my_pjt.model_dump())
print(my_pjt.db_info) 