from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean, DateTime, Date, \
        Time, String, ForeignKey

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
       return "<User(id='%d')>" % (self.id)

class ProblemMapping(Base):
    __tablename__ = 'problem_mappings'

    id         = Column(Integer, primary_key=True)
    seed       = Column(Integer)
    user_id    = Column(Integer, ForeignKey('users.id'))
    problem_id = Column(Integer, ForeignKey('problems.id'))

    def __repr__(self):
       return "<User(user_id='%d', problem_id='%d')>" % (self.user_id, self.problem_id)
