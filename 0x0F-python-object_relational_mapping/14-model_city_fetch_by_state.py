#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py
that contains the class definition of a City
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    import sys

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_name = session.query(
        City.id, City.name, State.name
    ).join(
        State, State.id == City.state_id
    ).order_by(City.id).all()

    for row in cities_name:
        print("{}: ({}) {}".format(row.State.name[2], row.id[0], row.city.name[1]))
    session.close()
