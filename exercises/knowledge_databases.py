from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,title, rating):
    article_object = Knowledge(
        name=name,
        title=title,
        rating=rating)
    session.add(article_object)
    session.commit()


add_article("Noam", "music", 9)
add_article("Rakan", "chemistry", 8)
add_article("Leen", "architecture", 7)

def query_all_articles():
    pass

def query_article_by_topic():
    pass

def delete_article_by_topic():
    pass

def delete_all_articles():
    pass

def edit_article_rating():
    pass
