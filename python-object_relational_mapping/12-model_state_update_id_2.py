#!/usr/bin/python3
"""
script that changes the name of the State object with id = 2
to 'New Mexico' in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state():
    """Update the name of State with id=2 to 'New Mexico'"""
    arg = sys.argv
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer l'état avec id=2
    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()


if name == "main":
    update_state()
