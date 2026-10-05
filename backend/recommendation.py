def recommend_career(student):

    scores = {
        "Data Analyst": student.sql + student.power_bi + student.python,

        "Machine Learning Engineer":
            student.python + student.machine_learning,

        "Python Developer":
            student.python * 2,

        "Business Intelligence Analyst":
            student.sql + (student.power_bi * 2)
    }

    recommended_career = max(scores, key=scores.get)

    return {
        "recommended_career": recommended_career,
        "scores": scores
    }