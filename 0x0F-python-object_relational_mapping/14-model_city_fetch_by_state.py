#!/usr/bin/python3
"""This script prints all City objects from the database
hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    uri = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                   sys.argv[2],
                                                   sys.argv[3])
    engine = create_engine(uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in (session.query(State, City)
                        .filter(State.id == City.state_id).all()):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
