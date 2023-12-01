#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    
    # Checking if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)
    
    # Creating SQLAlchemy engine and establishing connection
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Querying for all City objects and printing them
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State.name).filter_by(id=city.state_id).scalar()
        print("{}: ({}) {}".format(state_name, city.id, city.name))
