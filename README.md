# practie FastAPI 

## study/api/
간단한 get/post api 테스트 코드 <br><br>

## study/async/
비동기 예제 코드 - 비동기 처리가 왜 필요한지 <br><br>

## study/database1/
### sqlite사용
sqlalchemy 예제 코드 <br>
sqlalchemy는 python에서 사용할 수 있는 ORM(Objective Relational Mapping) 중 하나이다.<br>
django는 자체적으로 orm을 지원하지만 자체적으로 ORM을 지원하지 않는 대부분의 python framework들은 sqlalchemy를 사용해서 ORM을 사용한다. <br>
FastAPI에서 sqlalchemy를 사용하여 DB(Sqlite)에서 값을 꺼내와서 front로 넘겨주는 간단한 `get`api 구현 코드. <br><br>

## study/database2/
### postgreSQL사용
database1 학습 내용에서 몇가지가 추가됨 추가된 것은 아래와 같음
> 1. uvicorn worker class이용한 비동기 처리 구현 <br>
> 2. redis + celery 이용해서 비동기 처리 구현.

<br><br>


## study/pydantic_test
pydantic 예제 코드 <br>
pydantic이란 python type hint를 이용해서 Input/Ouput 데이터의 검증을 손쉽게 할 수 있게 지원해주는 패키지 이다. <br>
또한 데이터 타입 뿐만 아니라 Filed를 이용해서 데이터의 범위나 크기 등을 지정해 줄 수도 있다.  <br><br>

## study/tutorial
fastapi공식문서에 있는 tutorial 따라 해본 것 
