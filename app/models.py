
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, CHAR

Base = declarative_base()

class State(Base):
    __tablename__ = 'STATE'
    YEAR = Column(Integer, primary_key=True)
    STATEID = Column(CHAR(3), nullable=False)
    STATE_NAME = Column(String, nullable=False)
    POPULATION = Column(Integer, nullable=False)

class StateGovernors(Base):
    __tablename__ = 'STATE_GOVERNORS'
    YEAR = Column(Integer, primary_key=True)
    STATENAME = Column(String, nullable=False)
    GOVERNOR_NAME = Column(String, nullable=False)
    GOVERNOR_PARTY = Column(String, nullable=True)

class Stock(Base):
    __tablename__ = 'STOCK'
    STOCKID = Column(String, primary_key=True)
    STOCKDATE = Column(Date, nullable=False)
    PRICE_PER_SHARE = Column(Float, nullable=True)

class CrudeOil(Base):
    __tablename__ = 'CRUDE_OIL'
    PRICE = Column(Float, nullable=False)
    YEAR = Column(Integer, primary_key=True)

class FederalGovernment(Base):
    __tablename__ = 'FEDERAL_GOVERNMENT'
    YEAR = Column(Integer, primary_key=True)
    HOUSE_MAJORITY = Column(CHAR(1), nullable=True)
    PRESIDENT_PARTY = Column(CHAR(1), nullable=True)
    SENATE_MAJORITY = Column(CHAR(1), nullable=True)

class GasPrice(Base):
    __tablename__ = 'GAS_PRICE'
    GASID = Column(Integer, primary_key=True)
    FUEL_TYPE = Column(String, nullable=False)
    REGION = Column(String, nullable=False)
    PRICE = Column(Float, nullable=False)
    GASDATE = Column(Date, nullable=False)

class Inflation(Base):
    __tablename__ = 'INFLATION'
    YEAR = Column(Integer, primary_key=True)
    VALUE_OF_DOLLAR = Column(Float, nullable=True)
    CPI = Column(Float, nullable=False)

# Depending on the SQLAlchemy version and cx_Oracle dialect, the String and Integer types might need to be replaced with String and Integer.
