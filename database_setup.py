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
	photo= Column(String)
	age= Column(String)
	place= Column(String)
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

	instructor=Instructors(name="Nada", instrument="Piano", age="26", place="Nazareth", photo="http://media.istockphoto.com/photos/businesswoman-portrait-on-white-picture-id517496982?k=6&m=517496982&s=170667a&w=0&h=6PK3M4vD6dZbZ7054zSQTLVuhk85qRVFS_4XhPbH-nI=",
	description="Music is my passion, since a very young age and especailly piano. I've been learning piano for 10 years now and teaching for 2. Why i love teaching piano and music in general is because it is only through music that i see the world being a better place.")
	session.add(instructor)
	session.commit()
	instructor=Instructors(name="Leen", instrument="Violon", age="24", place="Nazareth" ,
	description="I grew up in a very musical family. My father, is the Director of Music Orchestras ; I have always played a very active role in the music ministry at our church. I began taking violon lessons from  when I was in seventh grade, and participated in concert band and orchestra throughout junior high and high school. I am very fortunate to have had some amazing and talented music teachers in my life who inspired me to become the teacher and musician that I am today.")
	session.add(instructor)
	session.commit()
	instructor=Instructors(name="Adam", instrument="Guitar", age="30", place="Afula")
	session.add(instructor)
	session.commit()
	instructor=Instructors(name="Bella", instrument="Drums", age="24", place="Nazareth" ,
	description="A very passionate musician and strong believer in music and it's power to change and make the future and be the best tool for communication.And so i play music and teach it to see that change that i've always longed for")
	session.add(instructor)
	session.commit()
	instructor=Instructors(name="Jack", instrument="Violon", age="28", place="Jerusalm" ,
	description="I started learning violin when I was around four years old. I'm a fifth generation violinist in my family. So playing the violin is part of my family history and I felt that keenly even as a little boy.I didn't set out to become a teacher, I just knew I wanted to play the violin,But by the time I was 21, teaching violin had become a big part of my life.")
	session.add(instructor)
	session.commit()
	instructor=Instructors(name="Ron", instrument="Cello", age="26", place="Haifa" ,
	description="Unlike most musicians i know, my music career didn't start at a young age, allthough learning the cello was always my dream but i didn't have the resourcer for that to happen. This is why i strongly encourage thos website for it gives oppurtunities that i never had.And that is why i teach music, to help make dreams come true. ")
	session.add(instructor)
	session.commit()


	lesson=Session(time="1:30", Date="13/4/2017", location="Nazareth", intructor_id=1)
	session.add(lesson)
	session.commit()
	lesson=Session(time="3:30", Date="15/5/2017", location="Nazareth", intructor_id=1)
	session.add(lesson)
	session.commit()
	lesson=Session(time="3:30", Date="18/4/2017", location="Nazareth", intructor_id=2)
	session.add(lesson)
	session.commit()
	lesson=Session(time="3:30", Date="21/4/2017", location="Nazareth", intructor_id=2)
	session.add(lesson)
	session.commit()
	lesson=Session(time="4:00", Date="27/2/2017", location="Afula", intructor_id=3)
	session.add(lesson)
	session.commit()
	lesson=Session(time="3:30", Date="3/3/2017", location="Afula", intructor_id=3)
	session.add(lesson)
	session.commit()
	lesson=Session(time="4:00", Date="23/3/2017", location="Nazareth", intructor_id=4)
	session.add(lesson)
	session.commit()
	lesson=Session(time="4:00", Date="1/4/2017", location="Nazareth", intructor_id=4)
	session.add(lesson)
	session.commit()
	lesson=Session(time="2:30", Date="28/2/2017", location="Jerusalem", intructor_id=5)
	session.add(lesson)
	session.commit()
	lesson=Session(time="3:30", Date="2/3/2017", location="Jerusalem", intructor_id=5)
	session.add(lesson)
	session.commit()
	lesson=Session(time="3:30", Date="3/3/2017", location="Haifa", intructor_id=6)
	session.add(lesson)
	session.commit()
	lesson=Session(time="3:30", Date="15/3/2017", location="Haifa", intructor_id=6)
	session.add(lesson)
	session.commit()



