#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
else:
    class State(BaseModel):
        """ State class """
        name = ''

        @property
        def list_city(self):
            cities = models.storage.all(City)
            return cities
