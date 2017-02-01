from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE

class Person(Base):
	__tablename__ = 'person'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	#birthday = Column(Date)
	gender = Column(String)
	email= Column(String)
	password_hash= Column(String)
	sessions= relationship("Session", back_populates="person")

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

class Session(Base):
	__tablename__ = 'sessions'
	id = Column(Integer, primary_key=True)
	instructor = Column(String)
	description = Column(String)
	time = Column(String)
	location = Column(String)
	person_id = Column(Integer, ForeignKey('person.id'))
	person = relationship("Person", back_populates="sessions")
	intructor_id = Column(Integer, ForeignKey('intrucors.id'))
	instructor = relationship("Instructors", back_populates="sessions")



class Intructors(Base):
	__tablename__ = 'intructors'
	id = Column(Integer, primary_key=True)
	instrument=Column(String)
	description = Column(String)
	sessions= relationship("Session", back_populates="instructors")

instructor=Intructors(instrument="piano", description="i teach piano fml fml fml fml ")


engine = create_engine('sqlite:///musicTeachers.db')


Base.metadata.create_all(engine)