#!/usr/bin/python3
"""This script lists all State objects that contain the letter a from
the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    uri = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                   sys.argv[2],
                                                   sys.argv[3])
    engine = create_engine(uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in (session.query(State)
                       .filter(State.name.like("%a%"))
                       .order_by(State.id)):
        print("{}: {}".format(row.id, row.name))
