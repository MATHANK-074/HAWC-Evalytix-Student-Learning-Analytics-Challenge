# Project Report

# Student Learning Analytics System

**Project Name:** Student Learning Analytics System

**Challenge:** HAWC Evalytix Student Learning Analytics Challenge

**Domain:** Educational Data Analytics & Machine Learning

**Project Type:** Learning Analytics Dashboard

**Technology Stack:** Python, Pandas, NumPy, Scikit-learn, Streamlit, Matplotlib

---

# Table of Contents

1. Abstract
2. Introduction
3. Problem Statement
4. Objectives
5. Proposed Solution
6. System Architecture
7. Project Workflow
8. Dataset Description
9. Data Preprocessing
10. Exploratory Data Analysis
11. Learning Gap Analysis
12. Machine Learning Model
13. Recommendation Engine
14. Streamlit Dashboard
15. Results
16. Advantages
17. Limitations
18. Future Scope
19. Conclusion
20. References

---

# 1. Abstract

Educational institutions generate large amounts of student academic data, but extracting meaningful insights from this data is often challenging. Manual analysis is time-consuming and makes it difficult to identify students who require academic support at an early stage.

The **Student Learning Analytics System** addresses this problem by applying Machine Learning and Learning Analytics techniques to analyze student performance. The system generates synthetic educational datasets, preprocesses the data, performs exploratory analysis, predicts student performance using a Random Forest Classifier, and provides personalized recommendations through an interactive Streamlit dashboard.

The project demonstrates how data-driven analytics can support educators in monitoring student progress and making informed academic decisions.

---

# 2. Introduction

Learning Analytics is the process of collecting, analyzing, and interpreting educational data to improve learning outcomes.

This project analyzes multiple aspects of student performance, including:

- Attendance
- Assignment scores
- Quiz performance
- Mock test scores
- Study hours
- Student engagement

By analyzing these indicators, the system predicts academic performance and identifies students who may need additional academic support.

---

# 3. Problem Statement

Educational institutions often rely on manual methods to monitor student performance, making it difficult to identify learning gaps early.

Key challenges include:

- Lack of centralized student analytics.
- Difficulty identifying at-risk students.
- Limited use of predictive analytics.
- Delayed academic intervention.
- Absence of personalized recommendations.

---

# 4. Objectives

The main objectives of the project are:

- Generate realistic synthetic educational datasets.
- Analyze student learning behaviour.
- Identify learning gaps.
- Predict academic performance using Machine Learning.
- Provide personalized recommendations.
- Visualize insights through an interactive dashboard.

---

# 5. Proposed Solution

The proposed solution consists of the following components:

- Synthetic Data Generation
- Data Preprocessing
- Exploratory Data Analysis
- Learning Gap Analysis
- Machine Learning Prediction
- Recommendation Engine
- Streamlit Dashboard

This workflow enables educators to monitor student progress and take timely action.

---

# 6. System Architecture

```
Synthetic Dataset
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
Performance Prediction
        │
        ▼
Recommendation Engine
        │
        ▼
Streamlit Dashboard
```

---

# 7. Project Workflow

The project follows these steps:

1. Generate synthetic datasets.
2. Preprocess and clean the data.
3. Perform exploratory data analysis.
4. Analyze learning gaps.
5. Train the Machine Learning model.
6. Evaluate the model.
7. Generate personalized recommendations.
8. Display results through the Streamlit dashboard.

---

# 8. Dataset Description

The project uses synthetic educational datasets representing different aspects of student learning.

Datasets include:

- students.csv
- attendance.csv
- assignments.csv
- quiz_attempts.csv
- mock_tests.csv
- engagement.csv
- video_logs.csv

These datasets are merged into a processed dataset for analysis and model training.

---

# 9. Data Preprocessing

Data preprocessing ensures that the dataset is suitable for analysis.

The following steps are performed:

- Loading datasets
- Removing duplicate records
- Handling missing values
- Merging multiple datasets
- Feature selection
- Creating the final processed dataset

---

# 10. Exploratory Data Analysis

EDA helps understand the characteristics of the dataset.

Visualizations include:

- Attendance distribution
- Assignment score distribution
- Quiz performance
- Mock test analysis
- Engagement analysis
- Correlation heatmap

These insights help identify performance trends and learning behaviour.

---

# 11. Learning Gap Analysis

Learning Gap Analysis identifies students who may require academic support.

Indicators considered include:

- Low attendance
- Poor assignment performance
- Low quiz scores
- Weak mock test results
- Low study hours
- Reduced engagement

The analysis enables early intervention by educators.

---

# 12. Machine Learning Model

The project uses the **Random Forest Classifier** for student performance prediction.

### Input Features

- Attendance Percentage
- Assignment Average
- Quiz Average
- Mock Test Average
- Study Hours Per Week
- Engagement Score

### Output

The model predicts one of the following categories:

- Good
- Average
- At Risk

The trained model is saved as:

```
models/student_model.pkl
```

---

# 13. Recommendation Engine

The recommendation engine generates personalized suggestions based on:

- Attendance
- Assignments
- Quiz scores
- Mock test scores
- Study hours
- Engagement score
- Predicted performance

Example recommendations include:

- Improve attendance.
- Increase study hours.
- Practice additional quizzes.
- Complete assignments on time.
- Participate actively in learning activities.

---

# 14. Streamlit Dashboard

The dashboard provides an interactive interface for users to explore the analysis.

Dashboard features include:

- Project overview
- Dataset statistics
- Data visualizations
- Student performance prediction
- Personalized recommendations

The dashboard makes complex analytical results easy to understand.

---

# 15. Results

The project successfully demonstrates:

- Student data generation
- Data preprocessing
- Exploratory data analysis
- Learning gap detection
- Performance prediction
- Personalized recommendations
- Interactive visualization

These components work together to provide meaningful educational insights.

---

# 16. Advantages

- Supports data-driven academic decisions.
- Detects at-risk students early.
- Provides personalized recommendations.
- Interactive and user-friendly dashboard.
- Modular architecture for easy extension.
- Demonstrates practical application of Machine Learning in education.

---

# 17. Limitations

- Uses synthetic data instead of real institutional data.
- Recommendation engine is rule-based.
- Limited to selected academic indicators.
- Does not integrate with real Learning Management Systems.

---

# 18. Future Scope

Possible future enhancements include:

- Integration with real educational datasets.
- Learning Management System (LMS) integration.
- Deep Learning models for improved prediction.
- Cloud deployment.
- REST API development.
- User authentication.
- Faculty and student portals.
- Explainable AI (XAI) for model interpretation.
- Mobile application support.

---

# 19. Conclusion

The **Student Learning Analytics System** demonstrates how Machine Learning and Learning Analytics can be combined to improve educational decision-making. By analyzing attendance, assignments, quizzes, mock tests, study habits, and engagement, the system predicts student performance and provides personalized recommendations.

The modular design, interactive dashboard, and predictive capabilities make this project a strong demonstration of educational analytics and can serve as a foundation for future research and real-world academic support systems.

---

# 20. References

1. Scikit-learn Documentation – https://scikit-learn.org/
2. Streamlit Documentation – https://streamlit.io/
3. Pandas Documentation – https://pandas.pydata.org/
4. NumPy Documentation – https://numpy.org/
5. Matplotlib Documentation – https://matplotlib.org/
6. Python Documentation – https://docs.python.org/3/

---

## Appendix

### Project Folder Structure

```
Student-Learning-Analytics/
│
├── data/
├── notebooks/
├── models/
├── dashboard/
├── docs/
├── images/
├── requirements.txt
└── README.md
```

### Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git
- GitHub