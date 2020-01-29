from model import Base,News
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = scoped_session(sessionmaker(bind=engine,autoflush=False))
session = DBSession()



def add_News( header, body, images, link):

	info_object= News(header= header, body= body, images= images, link= link)
	session.add(info_object)
	session.commit()

# add_News("left", "hi", "hello", "school.jpg", "http://www.youtube.com")
# add_News("middle", "hi", "hello", "school.jpg", "http://www.youtube.com")
# add_News("right", "hi", "hello", "school.jpg", "http://www.youtube.com")

def change(position, header, body, images, link):
	info_object = session.query(News).filter_by(position= position).first()
	info_object.header = header
	info_object.body = body	
	info_object.images = images
	info_object.link = link
	session.commit()


def query_by_position(position):

   info = session.query(
       News).filter_by(
       position= position).first()
   return info

def query_by_header(header):
	news = session.query(News).filter_by(header = header).first()
	return news

def edit_image(header, image, body, link):
	query_by_header(header).images = image
	session.commit()

	query_by_header(header).body = body
	session.commit()

	query_by_header(header).link = link
	session.commit()


def query_all():

   info = session.query(News).all()
   return info

def delete_News(choose):

	info = session.query(
		News).filter_by(
		header= choose).delete()
	session.commit()
	return info
