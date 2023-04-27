from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base, User, GameHistory, ScoreHistory
from sqlalchemy.pool import QueuePool
import configparser

def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()

config = configparser.ConfigParser()
config.read('config.ini')

# Access database configuration options
DATABASE_URL = config.get('database', 'DATABASE_URL')

# create an engine for connecting to your database
#engine = create_engine(DATABASE_URL)

engine = create_engine(DATABASE_URL,
                       poolclass=QueuePool,
                       pool_size=10,
                       max_overflow=20)

# create a sessionmaker object for managing database sessions
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(sessionmaker(bind=engine))

# helper function for getting a new database session
"""def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""
def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
def create_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_db()
