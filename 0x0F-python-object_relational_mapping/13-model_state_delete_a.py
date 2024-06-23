#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} mysql_username mysql_password "
              "database_name".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine_url = (
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(mysql_username, mysql_password, database_name)
    )
    engine = create_engine(engine_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%'))
    states_to_delete = query.all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
