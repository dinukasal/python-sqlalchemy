from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Sequence
from db import Base
import datetime


class User(Base):
    __tablename__ = 'users'
    userId = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    phoneNumber = Column(Integer)
    name = Column(String(50))
    dateTime = Column(DateTime, default=datetime.datetime.utcnow)
