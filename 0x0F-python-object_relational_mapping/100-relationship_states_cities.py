#!/usr/bin/python3
"""
Script that creates the State “California” with
the City “San Francisco” in the database.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        new_state = State(name='California')
        new_city = City(name='San Francisco', state=new_state)
        session.add(new_state)
        session.add(new_city)
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
