##sqlalchemy tutorial code 2
##Insert data into database what named sqlalchemy_example.db

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker ##이거 뭐지?

from test_sqlalchemy1 import Address, Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db')
#Bind the engine to the metadata of the Base class so 
# that the declaratives can be accessed through a DBSession instance Base.metadata.bind = engine 
