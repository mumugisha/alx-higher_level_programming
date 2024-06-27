#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    if len(sys.argv) != 4:
        print('Usage: username password database')
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_query = session.query(
        City.id, City.name, State.name
    ).join(
        State, City.state_id == State.id
    ).order_by(City.id).all()

    for city_id, city_name, state_name in cities_query:
        print(f'{state_name}: ({city_id}) {city_name}')

    session.close()


if __name__ == "__main__":
    main()
