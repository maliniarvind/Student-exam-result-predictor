import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
data = pd.read_csv("dataset.csv")

# Features (inputs)
X = data[['study_hours', 'attendance']]

# Target (output)
y = data['result']

# Create and train model
model = DecisionTreeClassifier()
model.fit(X, y)

print("Student Exam Result Predictor")

# Take user input
study_hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))

# Predict result
prediction = model.predict([[study_hours, attendance]])

print("Predicted Result:", prediction[0])