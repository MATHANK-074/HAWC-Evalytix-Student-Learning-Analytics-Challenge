# System Architecture

## Overview

The **Student Learning Analytics System** is designed using a modular architecture that follows the complete Data Science lifecycle. The system generates synthetic educational datasets, preprocesses and analyzes the data, trains a Machine Learning model to predict student performance, and presents insights through an interactive Streamlit dashboard.

Each module performs a specific task, making the project scalable, maintainable, and easy to understand.

---

# Architecture Diagram

```
                    +---------------------------+
                    |   Synthetic Data Generation|
                    | (01_Data_Generation.ipynb)|
                    +------------+--------------+
                                 |
                                 v
                    +---------------------------+
                    |     CSV Dataset Files     |
                    | students.csv             |
                    | attendance.csv           |
                    | assignments.csv          |
                    | engagement.csv           |
                    | quiz_attempts.csv        |
                    | mock_tests.csv           |
                    | video_logs.csv           |
                    +------------+--------------+
                                 |
                                 v
                    +---------------------------+
                    | Data Cleaning &           |
                    | Preprocessing             |
                    +------------+--------------+
                                 |
                                 v
                    +---------------------------+
                    | Exploratory Data Analysis |
                    | (EDA & Visualization)     |
                    +------------+--------------+
                                 |
                                 v
                    +---------------------------+
                    | Learning Gap Analysis     |
                    +------------+--------------+
                                 |
                                 v
                    +---------------------------+
                    | Feature Engineering       |
                    +------------+--------------+
                                 |
                                 v
                    +---------------------------+
                    | Machine Learning Model    |
                    | (Random Forest)           |
                    +------------+--------------+
                                 |
                                 v
                    +---------------------------+
                    | Model Evaluation          |
                    | Accuracy, Precision,      |
                    | Recall, F1 Score          |
                    +------------+--------------+
                                 |
                                 v
                    +---------------------------+
                    | Recommendation Engine     |
                    +------------+--------------+
                                 |
                                 v
                    +---------------------------+
                    | Streamlit Dashboard       |
                    +---------------------------+
```

---

# System Workflow

The project follows a structured workflow where each phase depends on the output of the previous phase.

1. Generate synthetic student datasets.
2. Clean and preprocess the generated data.
3. Perform exploratory data analysis.
4. Identify learning gaps among students.
5. Train a Machine Learning prediction model.
6. Evaluate the model using performance metrics.
7. Generate personalized recommendations.
8. Display results through an interactive Streamlit dashboard.

---

# Architecture Components

## 1. Data Generation Module

This module creates realistic educational datasets representing student activities.

Generated datasets include:

- students.csv
- attendance.csv
- assignments.csv
- engagement.csv
- quiz_attempts.csv
- mock_tests.csv
- video_logs.csv

### Responsibilities

- Generate synthetic student information
- Simulate academic performance
- Create realistic learning behaviour
- Store datasets as CSV files

---

## 2. Data Preprocessing Module

The preprocessing module prepares the datasets for analysis and machine learning.

### Tasks Performed

- Merge datasets
- Handle missing values
- Remove duplicate records
- Convert data types
- Feature selection
- Feature engineering

### Output

A cleaned and processed dataset ready for analysis.

---

## 3. Exploratory Data Analysis Module

This module analyzes student behaviour using descriptive statistics and visualization.

### Analysis Performed

- Attendance distribution
- Assignment performance
- Quiz analysis
- Mock test analysis
- Student engagement
- Correlation analysis

### Output

Visual insights that help understand student learning behaviour.

---

## 4. Learning Gap Analysis Module

This module identifies students who may require additional academic support.

### Factors Considered

- Attendance percentage
- Assignment scores
- Quiz performance
- Mock test scores
- Student engagement

Students with consistently low performance are marked as **At-Risk Students**.

---

## 5. Feature Engineering Module

Important features are selected for machine learning.

Example features include:

- Attendance Percentage
- Assignment Average
- Quiz Average
- Mock Test Score
- Engagement Score
- Study Hours

These features become the input variables for the prediction model.

---

## 6. Machine Learning Module

A **Random Forest Classifier** is used to predict student performance.

### Machine Learning Pipeline

- Load processed dataset
- Select features
- Split dataset into training and testing sets
- Train Random Forest model
- Predict student performance
- Save trained model

### Output

```
models/student_model.pkl
```

---

## 7. Model Evaluation Module

The trained model is evaluated using standard classification metrics.

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

These metrics determine how effectively the model predicts student performance.

---

## 8. Recommendation Engine

Based on the prediction results and learning gap analysis, the system generates personalized recommendations.

### Example Recommendations

| Condition | Recommendation |
|------------|---------------|
| Attendance < 75% | Attend more live classes |
| Quiz Score < 60% | Practice additional quizzes |
| Low Assignment Score | Submit assignments regularly |
| Low Engagement | Increase daily study hours |
| Low Mock Test Score | Revise weak concepts before the next test |

---

## 9. Streamlit Dashboard

The Streamlit dashboard provides an interactive interface for exploring data and predictions.

### Dashboard Pages

- Home
- Dataset Overview
- Learning Analytics
- Performance Prediction
- At-Risk Students
- Recommendations
- About Project

The dashboard allows users to interact with visualizations and view model predictions.

---

# Data Flow

```
Student Data
      │
      ▼
Synthetic Dataset Generation
      │
      ▼
CSV Files
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
EDA
      │
      ▼
Machine Learning
      │
      ▼
Predictions
      │
      ▼
Recommendations
      │
      ▼
Dashboard Visualization
```

---

# Directory Architecture

```
Student-Learning-Analytics/

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
│   ├── mock_tests.csv
│   ├── quiz_attempts.csv
│   └── video_logs.csv
│
├── models/
│   └── student_model.pkl
│
├── notebooks/
│   ├── 01_Data_Generation.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Model.ipynb
│   ├── 04_Model_Evaluation.ipynb
│   └── 05_Final_Insights.ipynb
│
├── docs/
├── images/
├── README.md
└── requirements.txt
```

---

# Advantages of the Architecture

- Modular and easy to maintain
- Scalable for larger educational datasets
- Supports end-to-end machine learning workflow
- Interactive dashboard for visualization
- Easy integration with real Learning Management Systems (LMS)
- Suitable for educational institutions and research projects

---

# Future Enhancements

The architecture can be extended with:

- Real-time LMS integration
- Cloud deployment (AWS, Azure, GCP)
- Deep Learning models
- Student authentication
- Faculty analytics dashboard
- Automated email notifications
- Real-time recommendation system
- Mobile application support

---

# Conclusion

The proposed system architecture provides a complete pipeline for educational learning analytics, beginning with synthetic data generation and ending with an interactive dashboard. The modular design ensures that each component operates independently while contributing to the overall workflow. This architecture enables efficient data analysis, accurate student performance prediction, and personalized recommendations, making it suitable for modern educational analytics applications.

---

# Next Document

After understanding the system architecture, proceed to:

**04_Dataset_Documentation.md**

This document explains every dataset, its columns, data types, relationships, and purpose within the project.