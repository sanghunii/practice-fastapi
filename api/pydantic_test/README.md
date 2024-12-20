# pydantic
pyton annotation을 이용해서 input data, output data에 대한 검증을 손쉽게 할 수 있게 해주는 python 패키지 


## BaseModel 

`pydantic.BaseModel`을 상속하여 클래스 각 멤버에 대한 데이터 검증을 손쉽게 할 수 있다.

[예제코드1](pydantic_test_1.py)
[예제코드2](pydantic_test_1.py)


## BaseSettings
`pydantic-settings.BaseSettings`를 상속한 클래스를 이용해서 Settings와 관련된 것들(env등)에 대한 정의를 할 수 있다.

`load_env()`를 사용하지 않고 env값을 쉽게 가져올 수 있다.

[예제코드](BaseSettings_test.py)


## BaseModel과 BaseSettings 동시에 사용
[예제코드](pydantic_example.py)

## fastapi에서 pydantic 사용

fastapi에서는 pydantic을 이용해서 데이터의 검증을 진행한다. 

[예제코드](pydantic-fastapi.py)
