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
	password_hash= Column(String(255))
	sessions= relationship("Session", back_populates="person")
	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)
	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

class Session(Base):
	__tablename__ = 'sessions'
	id = Column(Integer, primary_key=True)
	time = Column(String)
	Date= Column(String)
	location = Column(String)
	person_id = Column(Integer, ForeignKey('person.id'))
	person = relationship("Person", back_populates="sessions")
	intructor_id = Column(Integer, ForeignKey('instructors.id'))
	instructors = relationship("Instructors", back_populates="sessions")



class Instructors(Base):
	__tablename__ = 'instructors'
	id = Column(Integer, primary_key=True)
	name= Column(String)
	instrument=Column(String)
	description = Column(String)
	sessions= relationship("Session", back_populates="instructors")



engine = create_engine('sqlite:///musicTeachers.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


if __name__ == '__main__':
	engine = create_engine('sqlite:///musicTeachers.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine, autoflush=False)
	session = DBSession()

	instructor=Instructors(name="nada", instrument="piano", description="i teach piano fml fml fml fml ")
	session.add(instructor)
	session.commit()
	lesson=Session(time="1:30", Date="13/4/2017", location="nazareth")
	session.add(lesson)
	session.commit
