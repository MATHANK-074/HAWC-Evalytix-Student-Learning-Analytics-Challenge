# Project Overview

## Introduction

The **HAWC Evalytix – Student Learning Analytics Challenge** is an AI and Data Science internship assignment focused on designing an intelligent learning analytics system for educational institutions. The objective is to analyze student learning behavior, identify students who require academic intervention, predict student performance using machine learning, and provide actionable recommendations through an interactive dashboard.

Since no real-world educational dataset was available, this project begins by generating realistic synthetic datasets that simulate the activities of students preparing for competitive examinations such as **JEE, NEET, CBSE, ICSE, and Foundation**.

The project demonstrates the complete Data Science lifecycle, including data generation, preprocessing, exploratory data analysis (EDA), machine learning, recommendation generation, and dashboard development.

---

# Problem Statement

Educational institutions generate large volumes of learning data, including attendance, assignment submissions, quiz attempts, mock test scores, and online engagement. However, this data often remains underutilized, making it difficult to identify students who may need additional academic support.

The challenge is to build a system that can:

- Analyze student learning behavior.
- Detect learning gaps at an early stage.
- Predict student performance.
- Provide personalized recommendations for improvement.
- Present insights through an interactive dashboard.

---

# Project Objectives

The primary objectives of this project are:

- Design a realistic educational data model.
- Generate synthetic datasets for more than 2,000 students.
- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Identify learning gaps among students.
- Train a Machine Learning model to predict student performance.
- Evaluate the performance of the trained model.
- Generate personalized learning recommendations.
- Develop an interactive Streamlit dashboard for visualization.

---

# Project Scope

This project covers the complete workflow of an educational learning analytics system.

The implementation includes:

- Synthetic educational dataset generation
- Data preprocessing
- Exploratory Data Analysis
- Learning gap identification
- Student performance prediction
- Recommendation engine
- Interactive analytics dashboard

The project is intended for educational purposes and demonstrates how Artificial Intelligence and Data Science techniques can be applied to improve student learning outcomes.

---

# Dataset Overview

The project uses multiple synthetic datasets representing different aspects of student learning.

The generated datasets include:

- students.csv
- attendance.csv
- assignments.csv
- engagement.csv
- quiz_attempts.csv
- mock_tests.csv
- video_logs.csv

These datasets are merged and processed to create a unified dataset for analysis and machine learning.

---

# Project Workflow

The project follows a structured Data Science workflow.

```
Synthetic Data Generation
          │
          ▼
Data Cleaning
          │
          ▼
Feature Engineering
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Learning Gap Analysis
          │
          ▼
Machine Learning Model
          │
          ▼
Model Evaluation
          │
          ▼
Recommendation Engine
          │
          ▼
Interactive Streamlit Dashboard
```

---

# Machine Learning Approach

A supervised Machine Learning model is trained to classify student performance based on learning behavior and academic indicators.

The workflow includes:

- Feature Selection
- Data Splitting
- Model Training
- Prediction
- Model Evaluation
- Model Saving
- Dashboard Integration

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

# Recommendation Engine

The recommendation engine provides personalized suggestions based on student learning behavior.

Examples include:

- Increase lecture attendance.
- Improve assignment completion.
- Spend more time watching educational videos.
- Practice chapter-wise quizzes.
- Increase weekly study hours.
- Revise weak subjects identified from mock tests.

These recommendations help students improve their academic performance and reduce learning gaps.

---

# Dashboard Overview

The project includes an interactive dashboard developed using **Streamlit**.

The dashboard contains the following sections:

- Home
- Dataset Overview
- Learning Analytics
- Student Performance Prediction
- At-Risk Students
- Personalized Recommendations
- About Project

The dashboard enables users to explore educational data and visualize student performance through interactive charts and metrics.

---

# Technology Stack

The following technologies were used during development:

## Programming Language

- Python

## Development Environment

- Jupyter Notebook
- Visual Studio Code

## Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

---

# Expected Outcomes

The completed system is capable of:

- Generating realistic educational datasets.
- Analyzing student learning behavior.
- Detecting learning gaps.
- Predicting student performance.
- Identifying students requiring academic support.
- Providing personalized recommendations.
- Presenting results through an interactive dashboard.

---

# Future Enhancements

The project can be further enhanced by:

- Integrating real Learning Management System (LMS) data.
- Implementing deep learning models for prediction.
- Deploying the application on cloud platforms.
- Sending automated alerts to students and faculty.
- Building faculty performance analytics.
- Providing AI-powered personalized learning plans.

---

# Conclusion

The **Student Learning Analytics System** demonstrates the practical application of Artificial Intelligence and Data Science in education. By combining synthetic data generation, exploratory analysis, machine learning, and interactive visualization, the project provides a comprehensive solution for understanding student learning behavior and identifying students who require timely academic intervention.

The project establishes a strong foundation for future educational analytics systems that can support teachers, institutions, and students in making informed, data-driven decisions.