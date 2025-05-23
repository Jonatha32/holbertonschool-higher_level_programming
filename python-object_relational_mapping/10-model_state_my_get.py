#!/usr/bin/python3
"""
search an state for the name and show the ID
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_to_search = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Se = sessionmaker(bind=engine)
    session = Se()

    state = session.query(State)\
                  .filter(State.name == state_to_search)\
                  .first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
