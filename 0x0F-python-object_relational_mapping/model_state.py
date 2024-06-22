#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance Base.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy(create_engine)

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


def main():
    engine = create_engine('sqlite:///states.db', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()


if __name__ == "__main__":
    main()
