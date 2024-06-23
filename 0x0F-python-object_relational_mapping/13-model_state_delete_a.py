#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        state_delete = session.query(State).filter(
                  State.name.like('%a%')).all()

        for state in state_delete:
            session.delete(state)

        session.commit()
