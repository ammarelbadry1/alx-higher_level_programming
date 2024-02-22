#!./venv/bin/python3
"""This module contains the class definition of a State."""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """Defines a class State."""

    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine("mysql://localhost:3306")
    Base.metadata.create_all(engine)
