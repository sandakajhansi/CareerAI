from sqlalchemy import Column, Integer, String, Float
from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    branch = Column(String)
    cgpa = Column(Float)

    python = Column(Integer, default=0)
    sql = Column(Integer, default=0)
    machine_learning = Column(Integer, default=0)
    power_bi = Column(Integer, default=0)

    career_goal = Column(String)