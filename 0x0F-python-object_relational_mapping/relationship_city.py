#!/usr/bin/python3

"""Module that contains the class definition of a City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base


class City(Base):
    """Class definition of a City"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
