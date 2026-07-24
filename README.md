# HAWC-Evalytix-Student-Learning-Analytics-Challenge



# 📚 Student Learning Analytics System

> **An AI-powered Student Learning Analytics and Performance Prediction System** that generates synthetic educational datasets, analyzes student learning behavior, predicts academic performance using Machine Learning, and visualizes insights through an interactive Streamlit dashboard.

---

## 📖 Table of Contents

- Overview
- Problem Statement
- Objectives
- Features
- Technology Stack
- Project Architecture
- Folder Structure
- Installation
- Project Workflow
- Dataset Description
- Data Preprocessing
- Exploratory Data Analysis
- Machine Learning Model
- Dashboard
- Results
- Future Enhancements
- Author

---

# 📌 Overview

The **Student Learning Analytics System** is a data-driven educational analytics platform developed using **Python, Jupyter Notebook, Machine Learning, and Streamlit**.

The system simulates educational data, analyzes student learning patterns, predicts student performance, and provides meaningful insights that help educators identify students requiring academic support.

The project demonstrates a complete Machine Learning pipeline, starting from synthetic dataset generation to deployment through an interactive dashboard.

---

# ❓ Problem Statement

Educational institutions collect large amounts of student data such as attendance, quiz scores, mock tests, assignments, and learning engagement.

However, this information is usually scattered across multiple sources, making it difficult to:

- Monitor student progress
- Identify academically weak students
- Analyze learning behavior
- Predict future performance
- Provide personalized recommendations

This project solves these challenges by integrating all learning data into one intelligent analytics system.

---

# 🎯 Objectives

- Generate realistic educational datasets.
- Analyze student learning behavior.
- Perform exploratory data analysis.
- Build a Machine Learning prediction model.
- Predict student academic performance.
- Identify at-risk students.
- Display insights using an interactive dashboard.

---

# ✨ Features

- Synthetic student data generation
- Attendance analytics
- Quiz performance analysis
- Mock test analysis
- Assignment performance tracking
- Student engagement analytics
- Performance prediction using Machine Learning
- Interactive Streamlit dashboard
- Personalized recommendations

---

# 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Development Environment | Jupyter Notebook |
| Data Analysis | Pandas |
| Numerical Computing | NumPy |
| Data Generation | Faker |
| Visualization | Matplotlib, Plotly |
| Machine Learning | Scikit-learn |
| Model | Random Forest Classifier |
| Dashboard | Streamlit |
| Model Storage | Joblib |

---

# 🏗 Project Architecture

```

Synthetic Data Generation
│
▼
CSV Dataset Creation
│
▼
Data Preprocessing
│
▼
Exploratory Data Analysis
│
▼
Feature Engineering
│
▼
Machine Learning Model
│
▼
Performance Prediction
│
▼
Streamlit Dashboard
│
▼
Student Recommendations

```

---

# 📂 Project Structure

```

Student-Learning-Analytics/
│
├── data/
│   ├── students.csv
│   ├── attendance.csv
│   ├── video_logs.csv
│   ├── quiz_attempts.csv
│   ├── mock_tests.csv
│   ├── assignments.csv
│   └── engagement.csv
│
├── notebooks/
│   ├── 01_Data_Generation.ipynb
│   ├── 02_EDA.ipynb
│   └── 03_Model.ipynb
│
├── dashboard/
│   └── app.py
│
├── models/
│   └── student_model.pkl
│
├── README.md
└── requirements.txt

```

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/Student-Learning-Analytics.git
```

## 2. Navigate to Project

```bash
cd Student-Learning-Analytics
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Project Workflow

## Step 1 – Data Generation

The project starts by generating realistic educational datasets using the **Faker** library.

The notebook:

```

01_Data_Generation.ipynb

```

creates multiple CSV files containing student learning information.

Generated datasets include:

- students.csv
- attendance.csv
- video_logs.csv
- quiz_attempts.csv
- mock_tests.csv
- assignments.csv
- engagement.csv

---

## Step 2 – Data Preprocessing

All datasets are loaded using **Pandas**.

The preprocessing stage includes:

- Loading CSV files
- Checking data types
- Handling missing values
- Removing duplicate records
- Data validation
- Preparing data for analysis

---

## Step 3 – Exploratory Data Analysis (EDA)

EDA is performed using **Matplotlib** and **Plotly** to understand student learning behavior.

Visualizations include:

- Attendance Distribution
- Quiz Accuracy Distribution
- Mock Test Marks Distribution
- Assignment Scores
- Weekly Study Hours
- Login Frequency
- Student Engagement

EDA helps identify trends and learning gaps.

---

## Step 4 – Feature Engineering

Relevant features from different datasets are merged into one dataset.

Features used for prediction include:

- Attendance Percentage
- Quiz Accuracy
- Mock Test Marks
- Assignment Score
- Weekly Study Hours
- Login Frequency
- Average Session Duration
- Sessions Per Week

The target variable is student performance categorized as:

- High Performer
- Average
- At Risk

---

## Step 5 – Machine Learning Model

The project uses the **Random Forest Classifier**.

The model training process consists of:

1. Loading processed data.
2. Splitting data into training and testing sets.
3. Training the Random Forest model.
4. Evaluating prediction accuracy.
5. Saving the trained model using Joblib.

The trained model is stored as:

```

models/student_model.pkl

```

---

## Step 6 – Interactive Dashboard

The dashboard is developed using **Streamlit**.

It provides an interactive interface to visualize student analytics.

Dashboard features include:

- Total Students
- High Performers
- Average Students
- At-Risk Students
- Attendance Distribution
- Quiz Accuracy
- Mock Test Analysis
- Student Search
- Performance Prediction
- Personalized Recommendations

---

# 📊 Dataset Description

## students.csv

Contains basic student information.

Columns:

- Student_ID
- Student_Name
- Class
- Board
- Target_Exam
- Medium
- Admission_Date
- Study_Mode

---

## attendance.csv

Stores attendance information.

Columns:

- Student_ID
- Subject
- Attendance_Percentage

---

## video_logs.csv

Stores online learning activity.

Columns:

- Student_ID
- Video_Length
- Watch_Time
- Completion_Percentage

---

## quiz_attempts.csv

Contains quiz results.

Columns:

- Student_ID
- Accuracy
- Correct
- Incorrect

---

## mock_tests.csv

Contains mock examination performance.

Columns:

- Student_ID
- Marks
- Rank
- Time_Utilization

---

## assignments.csv

Stores assignment information.

Columns:

- Student_ID
- Submitted
- Submission_Delay
- Score

---

## engagement.csv

Contains learning engagement statistics.

Columns:

- Student_ID
- Weekly_Study_Hours
- Login_Frequency
- Average_Session_Duration
- Sessions_Per_Week

---

# 📈 Exploratory Data Analysis

The following analyses are performed:

- Attendance Distribution
- Quiz Accuracy Distribution
- Mock Test Score Distribution
- Assignment Score Distribution
- Weekly Study Hours Analysis
- Student Engagement Analysis
- Performance Category Distribution

---

# 🤖 Machine Learning

Algorithm Used:

**Random Forest Classifier**

Input Features:

- Attendance Percentage
- Quiz Accuracy
- Mock Test Marks
- Assignment Score
- Weekly Study Hours
- Login Frequency
- Average Session Duration
- Sessions Per Week

Target Classes:

- High Performer
- Average
- At Risk

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

# 📱 Dashboard

The Streamlit dashboard displays:

- Student Performance Summary
- Attendance Analytics
- Quiz Analytics
- Mock Test Analytics
- Student Search
- Performance Prediction
- Personalized Recommendations

Run the dashboard using:

```bash
cd dashboard
streamlit run app.py
```

---

# 📊 Results

The system successfully:

- Generated realistic educational datasets.
- Performed comprehensive exploratory data analysis.
- Trained a Machine Learning model for performance prediction.
- Classified students into performance categories.
- Built an interactive dashboard for visualization.
- Provided personalized academic recommendations.

---

# 🚀 Future Enhancements

- Real student database integration
- Deep Learning models
- XGBoost implementation
- Student login authentication
- Parent dashboard
- Faculty dashboard
- Cloud deployment
- Mobile application
- Real-time analytics
- Automatic report generation

---

# 👨‍💻 Author

**Mathankumar**

**B.Tech – Artificial Intelligence and Data Science**

**Kongu Engineering College**

---

# 📄 License

This project is developed for educational and learning purposes. It may be freely used for academic demonstrations, research, and skill development.

---

# ⭐ Conclusion

The **Student Learning Analytics System** demonstrates a complete end-to-end Machine Learning workflow, including synthetic data generation, preprocessing, exploratory data analysis, predictive modeling, and dashboard development. By combining data analytics with machine learning, the system helps educators monitor student performance, identify at-risk learners, and make informed academic decisions through an intuitive and interactive interface.
