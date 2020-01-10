from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Sequence
from db import Base
import datetime


class Guess(Base):
    __tablename__ = 'guess'
    crushRequestId = Column(Integer, Sequence('id'), primary_key=True)
    guessedName = Column(String(100))
    respondedDate = Column(DateTime, default=datetime.datetime.utcnow)
