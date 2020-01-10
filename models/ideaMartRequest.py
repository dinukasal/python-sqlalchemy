from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy import Sequence
from db import Base
import datetime


class IdeaMartRequest(Base):
    __tablename__ = 'ideaMartRequest'
    id = Column(Integer, Sequence('id'), primary_key=True)
    hash = Column(String(250))
    content = Column(JSON(1000))
    dateTime = Column(DateTime, default=datetime.datetime.utcnow)
