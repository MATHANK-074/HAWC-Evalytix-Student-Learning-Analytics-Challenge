# Developer Guide

# Student Learning Analytics System

**Version:** 1.0

**Technology Stack:** Python, Jupyter Notebook, Scikit-learn, Streamlit

---

# Table of Contents

1. Introduction
2. Project Overview
3. Technology Stack
4. Project Structure
5. Development Environment Setup
6. Project Workflow
7. Module Description
8. Machine Learning Pipeline
9. Dashboard Architecture
10. Adding New Features
11. Model Retraining
12. Coding Standards
13. Testing
14. Future Improvements

---

# 1. Introduction

The **Student Learning Analytics System** is a Machine Learning project developed to analyze student academic performance, identify learning gaps, predict future performance, and provide personalized recommendations.

This guide is intended for developers who want to understand, maintain, modify, or extend the project.

---

# 2. Project Overview

The project consists of the following major modules:

- Data Generation
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Learning Gap Analysis
- Machine Learning Model
- Recommendation Engine
- Streamlit Dashboard

Each module is independent and can be updated without affecting the entire system.

---

# 3. Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computation |
| Matplotlib | Data Visualization |
| Scikit-learn | Machine Learning |
| Joblib | Model Serialization |
| Streamlit | Interactive Dashboard |
| Jupyter Notebook | Development Environment |
| Git | Version Control |
| GitHub | Project Repository |

---

# 4. Project Structure

```
Student-Learning-Analytics/

│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── students.csv
│   ├── attendance.csv
│   ├── assignments.csv
│   ├── engagement.csv
│   ├── quiz_attempts.csv
│   ├── mock_tests.csv
│   └── video_logs.csv
│
├── models/
│   └── student_model.pkl
│
├── notebooks/
│   ├── 01_Data_Generation.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Model_Training.ipynb
│   └── 05_Model_Evaluation.ipynb
│
├── docs/
│
├── images/
│
├── requirements.txt
│
└── README.md
```

---

# 5. Development Environment Setup

## Step 1

Clone the repository.

```bash
git clone https://github.com/your-username/HAWC-Evalytix-Student-Learning-Analytics-Challenge.git
```

---

## Step 2

Move into the project directory.

```bash
cd HAWC-Evalytix-Student-Learning-Analytics-Challenge
```

---

## Step 3

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Step 4

Launch Jupyter Notebook.

```bash
jupyter notebook
```

---

## Step 5

Run notebooks sequentially.

```
01_Data_Generation.ipynb

↓

02_Data_Preprocessing.ipynb

↓

03_Exploratory_Data_Analysis.ipynb

↓

04_Model_Training.ipynb

↓

05_Model_Evaluation.ipynb
```

---

## Step 6

Run the dashboard.

```bash
cd dashboard

streamlit run app.py
```

---

# 6. Project Workflow

```
Synthetic Data Generation
            │
            ▼
Data Preprocessing
            │
            ▼
Exploratory Data Analysis
            │
            ▼
Learning Gap Analysis
            │
            ▼
Feature Selection
            │
            ▼
Random Forest Model
            │
            ▼
Prediction
            │
            ▼
Recommendation Engine
            │
            ▼
Streamlit Dashboard
```

---

# 7. Module Description

## Module 1 – Data Generation

**Purpose**

- Generate synthetic educational datasets.

**Input**

None

**Output**

- students.csv
- attendance.csv
- assignments.csv
- engagement.csv
- quiz_attempts.csv
- mock_tests.csv
- video_logs.csv

---

## Module 2 – Data Preprocessing

**Purpose**

Prepare datasets for analysis.

### Operations

- Load datasets
- Remove duplicates
- Handle missing values
- Merge datasets
- Feature selection

---

## Module 3 – Exploratory Data Analysis

Purpose

- Visualize learning patterns
- Understand data distribution
- Generate graphs

Examples

- Attendance Distribution
- Assignment Analysis
- Quiz Analysis
- Correlation Matrix

---

## Module 4 – Learning Gap Analysis

Purpose

Identify students requiring intervention.

Indicators

- Attendance
- Assignments
- Quizzes
- Mock Tests
- Engagement
- Study Hours

---

## Module 5 – Machine Learning

Algorithm

```
Random Forest Classifier
```

Purpose

Predict student performance.

Outputs

- Good
- Average
- At Risk

---

## Module 6 – Recommendation Engine

Generates personalized recommendations based on:

- Attendance
- Assignments
- Quiz performance
- Study hours
- Engagement
- Predicted category

---

## Module 7 – Dashboard

Displays

- Dataset overview
- Visualizations
- Predictions
- Recommendations

---

# 8. Machine Learning Pipeline

```
Dataset
   │
   ▼
Feature Selection
   │
   ▼
Train-Test Split
   │
   ▼
Random Forest
   │
   ▼
Training
   │
   ▼
Prediction
   │
   ▼
Evaluation
   │
   ▼
Save Model
```

---

# 9. Dashboard Architecture

```
User
   │
   ▼
Streamlit Interface
   │
   ▼
Load Dataset
   │
   ▼
Load ML Model
   │
   ▼
Generate Prediction
   │
   ▼
Display Recommendation
```

---

# 10. Adding New Features

Developers can extend the project by:

- Adding new datasets.
- Creating additional visualizations.
- Implementing new Machine Learning algorithms.
- Improving recommendation logic.
- Integrating real-world student datasets.
- Connecting to a Learning Management System (LMS).
- Adding authentication and user roles.
- Deploying the dashboard to the cloud.

---

# 11. Model Retraining

Whenever the dataset changes:

1. Run **02_Data_Preprocessing.ipynb**
2. Run **03_Exploratory_Data_Analysis.ipynb**
3. Run **04_Model_Training.ipynb**
4. Run **05_Model_Evaluation.ipynb**

A new model file will be created:

```
models/student_model.pkl
```

Replace the old model with the newly trained model.

---

# 12. Coding Standards

To maintain code quality:

- Follow **PEP 8** coding conventions.
- Use meaningful variable names.
- Add comments where necessary.
- Organize code into reusable functions.
- Avoid duplicate code.
- Keep notebooks modular and well-documented.

---

# 13. Testing

Before committing changes, verify:

- All notebooks execute without errors.
- Required CSV files are generated.
- The model is successfully trained and saved.
- The dashboard launches correctly.
- Predictions are displayed without errors.
- Recommendations are generated correctly.

---

# 14. Future Improvements

Potential enhancements include:

- Integration with real LMS platforms.
- Deep Learning-based prediction models.
- Cloud deployment (AWS, Azure, GCP).
- REST API integration.
- Student and faculty login.
- Automated email notifications.
- Real-time analytics.
- Explainable AI (XAI) for prediction interpretation.
- Mobile application support.

---

# Conclusion

The Student Learning Analytics System is designed with a modular architecture, allowing developers to maintain, extend, and improve individual components independently. By following this guide, developers can understand the project structure, execute the complete workflow, retrain the Machine Learning model, integrate new features, and contribute effectively to the project's development.