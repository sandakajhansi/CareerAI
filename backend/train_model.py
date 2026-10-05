import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("ml_data.csv")

X = data[
    ["python", "sql", "machine_learning", "power_bi", "cgpa"]
]

y = data["career"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Model trained successfully!")
print("Accuracy:", accuracy)

joblib.dump(model, "career_model.pkl")

print("Model saved as career_model.pkl")