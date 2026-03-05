#!/usr/bin/python3
"""
Script that changes the name of the State object with id = 2
to 'New Mexico' in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state():
    """Update the name of State with id=2 to 'New Mexico'"""
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".
              format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(username, password, database),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the state with id=2
    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "main":
    update_state()
