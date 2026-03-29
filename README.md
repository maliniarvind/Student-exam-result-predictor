# Student Exam Result Predictor (Machine Learning)

## Overview

This project predicts whether a student will **PASS or FAIL** based on two factors:

* Study hours per day
* Attendance percentage

The model is built using a **Decision Tree classifier**.

---

## Project Structure

student-exam-result-predictor
│
├── main.py (Main Python program)
├── dataset.csv (Training dataset)             
└── README.md (Project documentation)

---

## Prerequisites

Before running the project, ensure the following are installed:

* Python (version 3.8 or later)
* pip (Python package installer)

You can download Python from the official website.

---

## Step 1: Clone or Download the Repository

Option 1 – Clone using Git

git clone https://github.com/maliniarvind/Student-exam-result-predictor.git

Option 2 – Download ZIP
Download the repository from GitHub and extract it.

---

## Step 2: Navigate to the Project Folder

Open terminal or command prompt and go to the project directory:

cd Student-exam-result-predictor

---

## Step 3: Install Required Dependencies

Install the required Python libraries:

pip install pandas scikit-learn

Libraries used:

* pandas (for data handling)
* scikit-learn (for machine learning model)

---

## Step 4: Run the Program

Execute the Python script:

python main.py

---

## Step 5: Provide Input Values

The program will ask for:

Enter study hours per day
Enter attendance percentage

Example:

Enter study hours per day: 5
Enter attendance percentage: 70

Output:

Predicted Result: Pass

---

## Dataset Description

The dataset contains student records with:

* study_hours
* attendance
* result (Pass or Fail)

Example:

study_hours,attendance,result
1,40,Fail
3,60,Fail
5,70,Pass
7,80,Pass

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Decision Tree Classifier

---

## Future Improvements

* Use a larger dataset
* Add visualization
* Deploy as a web application

---

## Author 
Malini Arvind

MALINI ARVIND
Malini Arvin
