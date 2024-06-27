#!/usr/bin/python3
"""
Script that creates the State “California” with
the City “San Francisco” in the database.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from model_city import City

    if len(sys.argv) != 4:
        print("Usage: 100-relationship_states_cities.py "
              "<username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database
            ),
            pool_pre_ping=True
        )
        connection = engine.connect()
        connection.close()
    except Exception as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"Error creating tables: {e}")
        sys.exit(1)

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
        print(f"Error adding records: {e}")
    finally:
        session.close()
