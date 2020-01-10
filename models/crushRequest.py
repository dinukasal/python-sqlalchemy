from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import Sequence
from db import Base
import datetime


class CrushRequest(Base):
    __tablename__ = 'crushRequest'
    crushRequestId = Column(Integer, Sequence('id'), primary_key=True)
    senderName = Column(String(50))
    senderHash = Column(String(500))
    crushName = Column(String(50))
    crushNumber = Column(Integer)
    friend1 = Column(String(50))
    friend2 = Column(String(50))
    friend3 = Column(String(50))
    isForwarded = Column(Boolean)
    isResponseReceived = Column(Boolean)
    isSuccessful = Column(Boolean)
    receivedDate = Column(DateTime, default=datetime.datetime.utcnow)
