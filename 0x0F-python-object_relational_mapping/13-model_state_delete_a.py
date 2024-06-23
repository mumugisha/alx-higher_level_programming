#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection_string = (
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost/{database_name}'
    )
    engine = create_engine(connection_string, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states_to_delete = session.query(State).filter(
                State.name.like('%a%')).all()
        for state in states_to_delete:
            session.delete(state)

        session.commit()
        print("Deletion completed successfully.")

    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

    finally:
        session.close()
