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
       return "<Problem(id='{}', value='{}')>".format(self.id, self.value)

class ProblemMapping(Base):
    __tablename__ = 'problem_mappings'

    id         = Column(Integer, primary_key=True)
    seed       = Column(Integer)
    user_id    = Column(Integer, ForeignKey('users.id'))
    problem_id = Column(Integer, ForeignKey('problems.id'))

    def __repr__(self):
       return "<ProblemMapping(seed='{}', user_id='{}', problem_id='{}')>".format(self.seed, self.user_id, self.problem_id)

class Answer(Base):
    __tablename__ = 'answers'

    id                 = Column(Integer, primary_key=True)
    value              = Column(String)
    user_id            = Column(Integer, ForeignKey('users.id'))
    problem_mapping_id = Column(Integer, ForeignKey('problem_mappings.id'))

    def __repr__(self):
       return "<Answer(value='{}', user_id='{}', problem_mapping='{}')>".format(self.value, self.user_id, self.problem_mapping_id)
