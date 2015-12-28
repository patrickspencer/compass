from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean, DateTime, Date, Time, String, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id           = Column(Integer, primary_key=True)
    username     = Column(String)
    password     = Column(String)
    first_name   = Column(String)
    last_name    = Column(String)
    last_login   = Column(DateTime)
    date_joined  = Column(DateTime)
    email        = Column(String)
    is_staff     = Column(Boolean)
    is_active    = Column(Boolean)
    is_superuser = Column(Boolean)

    def __repr__(self):
       return "<User(username='%s')>" % (self.username)

class Problem(Base):
    __tablename__ = 'problems'

    id    = Column(Integer, primary_key=True)
    value = Column(String)

    def __repr__(self):
       return "<User(id='%s')>" % (self.id)

