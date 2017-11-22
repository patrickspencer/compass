import time
from faker import Factory
from datetime import date
from random import randint
from models import User, Problem, ProblemMapping
from django.conf import settings
from django.contrib.auth.hashers import make_password
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, ForeignKey

settings.configure()

engine = create_engine('postgresql://compass_webapp:password@localhost:5432/compass_webapp_db', echo=False, pool_timeout=1)
session = sessionmaker(bind=engine)
Session = session()

fake = Factory.create()

def create_users():
    for n in range(0,200):
        userid = 'user%d' % (n+1)
        user = User(
          username=userid,
          password=make_password('password'),
          last_login=date.fromtimestamp(time.time()),
          date_joined=date.fromtimestamp(time.time()),
          first_name=fake.first_name(),
          last_name=fake.last_name(),
          email=fake.free_email(),
          is_staff=False,
          is_active=True,
          is_superuser=False
        )
        if not Session.query(exists().where(User.username==userid)).scalar():
            Session.add(user)
# Session.commit()

def create_problems():
    for n in range(0,20):
        problem_value = 'problem value %d' % (n+1)
        problem = Problem(
          value=problem_value
        )
        if not Session.query(exists().where(Problem.value==problem_value)).scalar():
            Session.add(problem)

def create_problem_mappings():
    for n in range(1,30):
        for m in range(1, 20):
            problem_mapping = ProblemMapping(
              user_id = n,
              problem_id = m,
              seed = randint(1,100)
            )

            # if not 0
            if Session.query(ProblemMapping).filter_by(problem_id=(m),user_id=n).count()==0:
                Session.add(problem_mapping)

create_users()
create_problems()
create_problem_mappings()

Session.commit()
