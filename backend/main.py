from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Student
from schemas import StudentCreate, StudentResponse
from recommendation import recommend_career
from skill_gap import analyze_skill_gap
from courses import recommend_courses
from ml_prediction import predict_career

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerAI Student API",
    description="Student Career and Skill Recommendation Backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "CareerAI Backend is running!"}


@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(**student.model_dump())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@app.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}


@app.get("/students/{student_id}/recommendation")
def career_recommendation(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return recommend_career(student)


@app.get("/students/{student_id}/skill-gap")
def skill_gap_analysis(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return analyze_skill_gap(student)


@app.get("/students/{student_id}/courses")
def course_recommendation(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return recommend_courses(student)


@app.get("/students/{student_id}/ml-prediction")
def ml_career_prediction(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return predict_career(student)