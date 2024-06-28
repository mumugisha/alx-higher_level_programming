#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def get_engine(username, password, database):
    """Create and return a SQLAlchemy engine."""
    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
        )
        return engine
    except Exception as e:
        print(f'Error creating engine: {e}')
        sys.exit(1)


def get_session(engine):
    """Create and return a SQLAlchemy session."""
    try:
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        print(f'Error creating session: {e}')
        sys.exit(1)


def fetch_cities(session):
    """Fetch and print city information from the database."""
    try:
        cities_query = session.query(
            City.id, City.name, State.name
        ).join(
            State, City.state_id == State.id
        ).order_by(City.id).all()

        for city_id, city_name, state_name in cities_query:
            print(f'{state_name}: ({city_id}) {city_name}')
    except Exception as e:
        print(f'Error fetching cities: {e}')
        sys.exit(1)


def main():
    if len(sys.argv) != 4:
        print('Usage: username password database')
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = get_engine(username, password, database)
    Base.metadata.create_all(engine)

    session = get_session(engine)
    fetch_cities(session)
    session.close()
    engine.dispose()


if __name__ == "__main__":
    main()
