#!./venv/bin/python3
"""state Module

This module represent a class State
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String
from print_colored import printc
from sqlalchemy.orm import aliased

engine = create_engine('mysql://localhost:3306/test_db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='{}', fullname='{}', \
nickname='{}')>".format(self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)

# Begin a session(transaction)
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
printc(ed_user)

session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()
printc(our_user)
printc(ed_user is our_user)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Swaniker', nickname='freddy')])

ed_user.nickname = 'eddie'
printc(session.dirty)
printc(session.new)

# Commit the session
session.commit()

printc(ed_user.id)

ed_user.name = 'Edwardo'

fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
session.add(fake_user)

printc(session.query(User).filter(User.name.in_(['Edwardo',
                                  'fakeuser'])).all())
printc(fake_user in session)

session.rollback()

printc(ed_user.name)
printc(fake_user in session)

printc(session.query(User).filter(User.name.in_(['ed',
                                  'fakeuser'])).all())

# Get all rows (multiple forms)
for instance in session.query(User):
    printc(instance)

for instance in session.query(User):
    printc(instance.id, instance.name)

for id, name, user_instance in session.query(User.id, User.name, User):
    printc(id, name, user_instance)

for row in session.query(User, User.name).all():
    printc(row.User, row.name)

for name, in session.query(User.name).all():
    printc(name)

# Get all rows ordered by ...
for instance in session.query(User).order_by(User.id):
    printc(instance.id, instance.name)

# Column alias => SELECT column AS alias FROM table
for row in session.query(User.name.label('name_label')).all():
    printc(row.name_label)

# Table alias => SELECT column FROM table AS alias
# from sqlalchemy.orm import aliased
user_alias = aliased(User, name='user_alias')
for row in session.query(user_alias, user_alias.name).all():
    printc(row.user_alias)

# SELECT query include issuing LIMIT and OFFSET => python array slices
for user_instance in session.query(User).order_by(User.id)[1:3]:
    printc(user_instance)

# Queries with filters
for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
    printc(name)

# This filter allow you to use regular Python operators with the
# class level attributes on your mapped class
for name, in session.query(User.name).filter(User.fullname == 'Ed Jones'):
    print(name)

# Joining criteria in filtering
for user in session.query(User).\
        filter(User.name == 'ed').\
        filter(User.fullname == 'Ed Jones'):
    printc(user)
