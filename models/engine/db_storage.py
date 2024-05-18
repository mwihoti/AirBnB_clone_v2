#!/usr/bin/python3
"""Defines New engine DBStorage"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

objs = {"Amenity": Amenity, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage():

    """Defines DbStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if ("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session return a dictionary"""
        if not self.__session:
            self.reload()
        objects = {}
        if isinstance(cls, str):
            cls = objs.get(cls, None)
        if cls:
            for ob in self.__session.query(cls):
                objects[ob.__class__.__name__ + '.' + ob.id] = ob
        else:
            for cls in objs.values():
                for ob in self.__session.query(cls):
                    objects[ob.__class__.__name__ + '.' + ob.id] = ob
        return objects

    def new(self, obj):
        """add the object to the current database """
        self.__session.add(obj)

    def save(self):
        """Commits all changes of database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from database"""
        Base.metadata.create_all(self.__engine)
        curr_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        sess = scoped_session(curr_db)
        self.__session = sess

    def close(self):
        """call remove() method """
        self.__session.remove()
