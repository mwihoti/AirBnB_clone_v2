#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
from os import getenv
from models.city import City


class State(BaseModel):
    """ State class """
    __table__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """returns the list of City"""
            list_city = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list_city.append(city)
                    return list_city
