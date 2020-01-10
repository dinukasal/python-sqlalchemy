from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123@localhost/py', pool_recycle=3600)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models.users
    import models.ideaMartRequest
    import models.guess
    import models.crushRequest
    Base.metadata.create_all(bind=engine)