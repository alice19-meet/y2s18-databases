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


# add_article("Noam", "music", 9)
# add_article("Rakan", "chemistry", 8)
# add_article("Leen", "architecture", 7)

def query_all_articles():
    article=session.query(
        Knowledge).all()
    return article

#print (query_all_articles()) 

def query_article_by_topic(their_name):
    article=session.query(
        Knowledge).filter_by(
        name=their_name).first() 
    return article

#print(query_article_by_topic("Noam"))

def query_article_by_rating(threshold):
    rating=threshold
    knowledge= query_all_articles()
    rated_list=[]
    for article in knowledge:
        if article.rating<threshold:
            rated_list.append(article)
    return rated_list
#print(query_article_by_rating(8))

def query_article_by_primary_key(primary_key):
    article=session.query(
        Knowledge).filter_by(
            site_id=primary_key).first()
    return article

#print(query_article_by_primary_key(3))

# def delete_article_by_topic(topic):
#     session.query(Knowledge).filter_by(
#         title=topic).delete()
#     session.commit()

# def delete_all_articles():
#     session.query(Knowledge).delete()
#     session.commit()


def edit_article_rating(updated_rating, article_title):
    article = session.query(
        Knowledge).filter_by(
        title=article_title).all()
    for i in range(len(article)):
        article[i].rating=updated_rating
    session.commit()


edit_article_rating(10, "music")

    

print(query_all_articles())