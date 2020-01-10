from models.users import User
from db import engine, Base
from models.crushRequest import CrushRequest
from models.guess import Guess
from models.ideaMartRequest import IdeaMartRequest

Base.metadata.drop_all(bind=engine,
                       tables=[User.__table__, CrushRequest.__table__, Guess.__table__, IdeaMartRequest.__table__])
