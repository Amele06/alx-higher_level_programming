#!/usr/bin/python3
"""Module that contains the class definition of a State and an instance Base"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Importing Base before calling declarative_base()
# as it must be imported before calling Base.metadata.create_all(engine)
Base = declarative_base()


class State(Base):
    """Class definition of a State"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


# If executed directly, create the tables in the database
if __name__ == "__main__":
    from sqlalchemy import create_engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
