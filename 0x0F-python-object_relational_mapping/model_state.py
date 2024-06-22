#!/usr/bin/python3
"""
Python file that contains the class definition of a State and establishes
a connection to a MySQL server.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    Represents a State with an id and a name column.

    Attributes:
        id (int): The state's unique identifier, auto-generated, unique,
                  non-null, and primary key.
        name (str): The state's name, a string with a maximum length of
                    128 characters and cannot be null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


DATABASE_URI = 'mysql+mysqldb://username:password@localhost:3306/database_name'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
