#!/usr/bin/python3
"""This script changes the name of a State object from the database
hbtn_0e_6_usa"""
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
    state_to_update = session.query(State).filter_by(id=2).first()
    state_to_update.name = "New Mexico"
    session.commit()
