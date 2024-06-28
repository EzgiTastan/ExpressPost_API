# we have to import BASE from database.py
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default = 'TRUE', nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
    #we are referencing the class.
    #it'll fetch the user based on the user id.


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, nullable = False)
    email = Column(String, nullable=False, unique=True)
    # unique=True çünkü aynı maille 2 yeni hesap oluşturmamak için.
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))   

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True) 
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)