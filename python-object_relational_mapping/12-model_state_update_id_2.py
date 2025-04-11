#!/usr/bin/python3
"""
Script que actualiza el nombre de un State en la base de datos
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    Se = sessionmaker(bind=engine)
    session = Se()

    st_to_up = session.query(State).filter(State.id == 2).first()

    if st_to_up:
        st_to_up.name = "New Mexico"
        session.commit()

    session.close()
