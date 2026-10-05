import joblib

model = joblib.load("career_model.pkl")


def predict_career(student):

    data = [[
        student.python,
        student.sql,
        student.machine_learning,
        student.power_bi,
        student.cgpa
    ]]

    prediction = model.predict(data)

    return {
        "predicted_career": prediction[0]
    }