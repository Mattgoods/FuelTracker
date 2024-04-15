from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def create_app():
    app = Flask(__name__)
    return app

app = Flask(__name__)

Base = declarative_base()

# Use an environment variable or a secured method to store the actual password
# NEVER hardcode sensitive information like passwords in your source code
password = 'BTnup3sP9GzEcT64Tec4pLBD'  # Consider using os.environ to get this from an environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://ncomatas:{password}@oracle.cise.ufl.edu:1521/orcl'

# Create the engine with the provided database URI
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

Base.metadata.bind = engine

# Create a scoped session for your database interactions
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

Base.metadata.create_all(bind=engine)

from app import routes  # Import routes after the app has been initialized
