def recommend_courses(student):

    courses = []

    if student.sql < 8:
        courses.append("Advanced SQL")

    if student.machine_learning < 7:
        courses.append("Machine Learning Basics")

    if student.python < 8:
        courses.append("Python for Data Analysis")

    if student.power_bi < 8:
        courses.append("Power BI")

    return {
        "career": student.career_goal,
        "recommended_courses": courses
    }