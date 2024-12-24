from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Address, Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db')

# Bind the engine to the metadata of the Base class so that the
# decalratives can be accessed through a DBSession instance
Base.metadata.bind = engine


# sessionmaker()는 세션 객체를 생성하는 팩토리 함수를 반환한다. 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the 
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# rever all of them back to the last commit by calling 
# session.rollback()

# sessionmaker()로 부터 생성된 팩토리 함수를 이용해서 실제 session object를 생성
session = DBSession()


# Insert a person in the person table
new_person = Person(name='new person')
session.add(new_person)
session.commit()


# Insert an Address in the address table
new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()