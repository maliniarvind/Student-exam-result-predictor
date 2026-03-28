# Student Exam Result Predictor (Machine Learning)

## Overview

This is a beginner machine learning project that predicts whether a student will **PASS or FAIL** based on two factors:

* Study hours per day
* Attendance percentage

The project demonstrates a basic machine learning workflow using a **Decision Tree classifier**.

## Problem Statement

Students often want to know whether their current study habits are sufficient to pass an exam. This project uses simple academic indicators to predict exam outcomes and demonstrate how machine learning can be applied to educational data.

## Technologies Used

* Python
* Pandas
* Scikit-learn

## Machine Learning Algorithm

Decision Tree Classifier

## Dataset

The dataset contains sample records with the following fields:

* study_hours
* attendance
* result (Pass or Fail)

Example:

study_hours,attendance,result
1,40,Fail
5,70,Pass

## How to Run the Project

1. Install required libraries

python -m pip install pandas scikit-learn

2. Navigate to the project folder

cd AI_Project

3. Run the program

python main.py

4. Enter the inputs when prompted.

Example:

Enter study hours per day: 5
Enter attendance percentage: 70

Output:

Predicted Result: Pass

## Learning Outcomes

This project demonstrates:

* Loading datasets using Pandas
* Training a machine learning model
* Making predictions with Scikit-learn
* Basic AI/ML project structure

## Future Improvements

* Use a larger dataset
* Add graphical visualization
* Improve prediction accuracy
* Deploy as a web application

## Author

Malini Arvind
