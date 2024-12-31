from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://postgres:7777@localhost:5432/mspotifyclone'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()