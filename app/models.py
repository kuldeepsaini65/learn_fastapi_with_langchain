from sqlalchemy import Column, Integer, Float, String
from database import Base


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, unique=True, primary_key=True, index = True)
    name = Column(String(100))
    phone = Column(String(15), unique=True, index=True)