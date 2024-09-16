#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class using declarative_base
Base = declarative_base()


# Define an ORM model (a database table)
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())


if __name__ == '__main__':
    # Create a SQLite engine
    engine = create_engine('sqlite:///students.db')

    # Create all tables defined in the Base subclasses
    Base.metadata.create_all(engine)
