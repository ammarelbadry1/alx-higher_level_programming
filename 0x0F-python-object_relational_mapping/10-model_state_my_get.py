#!./venv/bin/python3
"""This script prints the State object with the name passed as argument
from the database hbtn_0e_6_usa."""
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

    result = session.query(State.id)\
                    .filter(State.name == sys.argv[4])
    if len(result[:]) == 0:
        print("Not found")
    else:
        print(result[0].id)
