#!/usr/bin/python3
""" create class """
from sys import argv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ create table """
    __tablename__ = "states"
    id = Column("id", Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    cities = relationship('City', backref='state')
