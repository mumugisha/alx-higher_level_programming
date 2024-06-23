#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine, exc
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name>".format(sys.argv[0]))
        sys.exit(1)

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

    try:
        states_delete = session.query(State)\
                               .filter(State.name.like('%a%'))\
                               .all()
        for state in states_delete:
            session.delete(state)
        session.commit()
    except exc.SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()
