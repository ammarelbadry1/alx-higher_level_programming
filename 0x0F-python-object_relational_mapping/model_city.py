#!/usr/bin/python3
"""This module contains the class definition of a City"""
from model_state import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Defines a class City."""

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    relation = relationship("State")
