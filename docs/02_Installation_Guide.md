# Installation Guide

## Overview

This guide explains how to set up and run the **HAWC Evalytix – Student Learning Analytics Challenge** project on your local machine.

The project consists of:

- Jupyter Notebooks for data generation, preprocessing, exploratory data analysis, and machine learning.
- A Streamlit dashboard for visualizing student analytics and predictions.
- Documentation describing each stage of the project.

The guide is intended for beginners and assumes no prior experience with the project.

---

# System Requirements

Before starting, ensure your system meets the following requirements.

## Operating System

- Windows 10/11
- Ubuntu 22.04 LTS
- macOS (Optional)

---

## Software Requirements

- Python 3.10 or later
- Git
- Jupyter Notebook
- Visual Studio Code (Recommended)
- Streamlit

---

## Required Python Libraries

The project uses the following libraries:

- pandas
- numpy
- matplotlib
- scikit-learn
- joblib
- streamlit

These dependencies are listed in the **requirements.txt** file.

---

# Project Structure

```
Student-Learning-Analytics/

│── dashboard/
│── data/
│── docs/
│── images/
│── models/
│── notebooks/

│── README.md
│── requirements.txt
│── LICENSE
```

---

# Step 1: Clone the Repository

Open a terminal or command prompt and execute:

```bash
git clone https://github.com/YOUR_USERNAME/HAWC-Evalytix-Student-Learning-Analytics-Challenge.git
```

Replace **YOUR_USERNAME** with your GitHub username.

---

# Step 2: Navigate to the Project Directory

```bash
cd HAWC-Evalytix-Student-Learning-Analytics-Challenge
```

---

# Step 3: Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# Step 4: Install Required Packages

Install all project dependencies using:

```bash
pip install -r requirements.txt
```

If installation is successful, all required libraries will be available for use.

---

# Step 5: Verify Installation

Check the installed versions.

```bash
python --version
```

```bash
pip --version
```

```bash
jupyter --version
```

```bash
streamlit --version
```

---

# Step 6: Launch Jupyter Notebook

Start Jupyter Notebook.

```bash
jupyter notebook
```

A browser window will open automatically.

Open the **notebooks** folder.

Run the notebooks in the following order:

1. 01_Data_Generation.ipynb
2. 02_EDA.ipynb
3. 03_Model.ipynb
4. 04_Model_Evaluation.ipynb
5. 05_Final_Insights.ipynb

Running them in sequence ensures that all datasets, processed files, and trained models are generated correctly.

---

# Step 7: Generate Synthetic Dataset

Run:

```
01_Data_Generation.ipynb
```

This notebook creates realistic educational datasets such as:

- students.csv
- attendance.csv
- assignments.csv
- engagement.csv
- quiz_attempts.csv
- mock_tests.csv
- video_logs.csv

The generated datasets are stored in the **data** folder.

---

# Step 8: Perform Exploratory Data Analysis

Run:

```
02_EDA.ipynb
```

This notebook performs:

- Data Cleaning
- Missing Value Handling
- Statistical Analysis
- Data Visualization
- Correlation Analysis
- Learning Behaviour Analysis

---

# Step 9: Train the Machine Learning Model

Run:

```
03_Model.ipynb
```

This notebook performs:

- Feature Selection
- Train-Test Split
- Model Training
- Prediction
- Model Saving

The trained model is saved in the **models** folder.

---

# Step 10: Evaluate the Model

Run:

```
04_Model_Evaluation.ipynb
```

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

This notebook validates the performance of the trained model.

---

# Step 11: View Final Insights

Run:

```
05_Final_Insights.ipynb
```

This notebook summarizes:

- Student performance
- Learning gaps
- Recommendations
- Overall project findings

---

# Step 12: Launch the Streamlit Dashboard

Navigate to the dashboard directory.

```bash
cd dashboard
```

Run:

```bash
streamlit run app.py
```

The application starts locally.

Open the browser at:

```
http://localhost:8501
```

If port **8501** is already in use:

```bash
streamlit run app.py --server.port 8502
```

or

```bash
streamlit run app.py --server.port 8505
```

---

# Dashboard Features

The dashboard provides the following pages:

- Home
- Dataset Overview
- Learning Analytics
- Student Performance Prediction
- At-Risk Students
- Personalized Recommendations
- About Project

---

# Output Files

After successfully running the project, the following outputs are generated.

### Generated Datasets

```
data/
```

### Trained Model

```
models/student_model.pkl
```

### Visualizations

```
images/
```

### Dashboard

```
dashboard/
```

---

# Troubleshooting

## ModuleNotFoundError

Install missing packages.

```bash
pip install -r requirements.txt
```

---

## Jupyter Notebook Not Opening

Verify installation.

```bash
jupyter --version
```

Reinstall if necessary.

```bash
pip install notebook
```

---

## Streamlit Not Starting

Check the installed version.

```bash
streamlit --version
```

Reinstall Streamlit if required.

```bash
pip install streamlit
```

---

## Port Already in Use

Run Streamlit on a different port.

```bash
streamlit run app.py --server.port 8502
```

---

## Model File Not Found

Ensure that **03_Model.ipynb** has been executed successfully.

Verify that:

```
models/student_model.pkl
```

exists.

---

# Project Execution Flow

```
Clone Repository
        │
        ▼
Install Dependencies
        │
        ▼
Run Jupyter Notebook
        │
        ▼
Generate Dataset
        │
        ▼
Perform EDA
        │
        ▼
Train Model
        │
        ▼
Evaluate Model
        │
        ▼
Generate Insights
        │
        ▼
Launch Streamlit Dashboard
```

---

# Installation Completed

If all steps are completed successfully, the Student Learning Analytics System is ready to use.

You can now:

- Explore the generated datasets.
- Analyze student learning behavior.
- Predict student performance.
- Identify at-risk students.
- View interactive dashboards.
- Generate personalized learning recommendations.

---

# Next Document

After completing the installation, the next document to read is:

**03_System_Architecture.md**

This document explains the overall architecture, workflow, and data flow of the project.