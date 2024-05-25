from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g, Flask

# Load environment variables from a .env file
load_dotenv()

# Print the DB_URL to verify it's loaded correctly
db_url = getenv('DB_URL')
print(f'Database URL: {db_url}')

# Connect to database using env variable
engine = create_engine(db_url, echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db(app):
    """Initialize the database."""
    Base.metadata.create_all(engine)
    app.teardown_appcontext(close_db)

def get_db():
    """Get a database session."""
    if 'db' not in g:
        # Store db connection in app context
        g.db = Session()
    return g.db

def close_db(e=None):
    """Close the database session."""
    db = g.pop('db', None)
    if db is not None:
        db.close()