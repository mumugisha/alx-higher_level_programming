#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py
that contains the class definition of a City
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    if len(sys.argv) != 4:
        print('Usage: username, password, database')
        sys.exit()

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_query = session.query(State, City.id, City).filter(
        City.state_id == State.id
    ).order_by(City.id).all()

    for row in cities_query:
        print(f'{row.State.name}: ({row.City.id}) {row.City.name}')

    session.close()


if __name__ == "__main__":
    main()
