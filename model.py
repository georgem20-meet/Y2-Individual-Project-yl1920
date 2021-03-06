from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base= declarative_base()

class User(Base):
	__tablename__ = 'users'
	user_id = Column (Integer, primary_key= True)
	username = Column(String)
	password = Column(String)

class News(Base):
	__tablename__='news'
	user_id = Column (Integer, primary_key= True)
	images = Column(String)	
	header = Column(String)
	body = Column(String)
	link = Column(String)
	# position = Column(String)


	# def hash_password(self, password):
	# 	self.password_hash= pwd_security.encrypt(password)

	# def verify_password(self, password):
	# 	return pwd_security.verify(password, self.password_hash)
