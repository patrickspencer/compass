from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from models import User, Problem, ProblemMapping
from faker import Factory
import time
from datetime import date
from django.contrib.auth.hashers import make_password
from django.conf import settings
from random import randint

settings.configure()


engine = create_engine('postgresql://compass_webapp:password@localhost:5432/compass_webapp_dev', echo=False, pool_timeout=1)
session = sessionmaker(bind=engine)
Session = session()

fake = Factory.create()

# for n in range(0,4):
#     userid = 'user%d' % (n+1)
#     user = User(
#       username=userid,
#       password=make_password('password'),
#       last_login=date.fromtimestamp(time.time()),
#       date_joined=date.fromtimestamp(time.time()),
#       first_name=fake.first_name(),
#       last_name=fake.last_name(),
#       email=fake.free_email(),
#       is_staff=False,
#       is_active=True,
#       is_superuser=False
#     )
#     if not Session.query(exists().where(User.username==userid)).scalar():
#         Session.add(user)
# Session.commit()
#
# for n in range(0,4):
#     problem_value = 'problem value %d' % (n+1)
#     problem = Problem(
#       value=problem_value
#     )
#     if not Session.query(exists().where(Problem.value==problem_value)).scalar():
#         Session.add(problem)
# Session.commit()

for n in range(0,4):
    problem_mapping = ProblemMapping(
      user_id = 1,
      problem_id = n+1,
      seed = randint(1,20)
    )

    # if not 0
    if Session.query(ProblemMapping).filter_by(problem_id=(n+1),user_id=1).count()==0:
        Session.add(problem_mapping)
Session.commit()

# Session.commit()
