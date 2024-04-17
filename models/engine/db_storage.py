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
            Base.metatdate.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session return a dictionary"""
        objs = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

        db_dict = {}
        for o in objs:
            if cls is None:
                ob = self.__session.query(objs[o]).all()
                for k in ob:
                    v = k.__class__.__name__ + '.' +k.id
                    db_dict[v] = k
                    return (db_dict)

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
        curr_db = Sessionmaker(bind=self.__engine, expire_on_commit=False)
        sess = scoped_session(curr_db)
        self.__session = sess

    def close(self):
        """call remove() method """
        self.__session.remove()

