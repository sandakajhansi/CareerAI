from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    age: int
    gender: str
    branch: str
    cgpa: float

    python: int = 0
    sql: int = 0
    machine_learning: int = 0
    power_bi: int = 0

    career_goal: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True