#!/usr/bin/python3
"""
Script that deletes all State objects with a name
containing the letter a from
the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_delete = session.query(State).filter(State.name.like('%a%'))
    for state in states_delete:
        session.delete(State)
    session.commit()
    session.close()
