#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <username> <password> <database>".format(
                sys.argv[0]
            )
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_query = session.query(City, State.name).join(
        State, State.id == City.state_id
    ).order_by(City.id).all()

    for city, state_name in cities_query:
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()
