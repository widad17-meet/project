from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

jack=Person(name='jack', birthday='24/3/2000', gender='male', username='jack33', passwaord='jack33')s
DBSession = sessionmaker(bind=engine)
session = DBSession()

