# User Guide

# Student Learning Analytics System

**Version:** 1.0

**Project Type:** Machine Learning & Learning Analytics

**Technology Stack:** Python, Jupyter Notebook, Scikit-learn, Pandas, Streamlit

---

# Table of Contents

1. Introduction
2. System Requirements
3. Project Structure
4. Running the Project
5. Using the Jupyter Notebooks
6. Using the Streamlit Dashboard
7. Understanding the Results
8. Troubleshooting
9. Frequently Asked Questions
10. Conclusion

---

# 1. Introduction

The **Student Learning Analytics System** is a Machine Learning-based application designed to analyze student academic performance, identify learning gaps, predict performance, and generate personalized recommendations.

The project uses synthetic educational datasets to simulate real-world student learning data and provides meaningful insights through data analysis and an interactive dashboard.

---

# 2. System Requirements

Before running the project, ensure the following software is installed.

### Software Requirements

- Python 3.10 or above
- Jupyter Notebook
- Visual Studio Code (Optional)
- Git (Optional)

### Python Libraries

- pandas
- numpy
- matplotlib
- scikit-learn
- joblib
- streamlit

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

# 3. Project Structure

```
Student-Learning-Analytics/

│
├── data/
│
├── notebooks/
│
├── models/
│
├── dashboard/
│
├── images/
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

Each folder has a specific purpose.

| Folder | Description |
|---------|-------------|
| data | Stores datasets |
| notebooks | Jupyter notebooks |
| models | Trained ML model |
| dashboard | Streamlit application |
| images | Graphs and screenshots |
| docs | Documentation files |

---

# 4. Running the Project

## Step 1

Open the project folder.

```
Student-Learning-Analytics
```

---

## Step 2

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Step 3

Open Jupyter Notebook.

```bash
jupyter notebook
```

---

## Step 4

Navigate to the **notebooks** folder.

Run the notebooks sequentially.

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

## Step 5

After model training, verify that the model file has been created.

```
models/student_model.pkl
```

---

## Step 6

Start the Streamlit dashboard.

```bash
cd dashboard

streamlit run app.py
```

Open your browser.

```
http://localhost:8501
```

---

# 5. Using the Jupyter Notebooks

The notebooks should always be executed in order.

---

## Notebook 1

### Data Generation

Purpose

- Generate synthetic datasets
- Save datasets as CSV files

Output

```
students.csv

attendance.csv

assignments.csv

engagement.csv

quiz_attempts.csv

mock_tests.csv

video_logs.csv
```

---

## Notebook 2

### Data Preprocessing

Purpose

- Clean datasets
- Remove duplicates
- Merge datasets
- Prepare data

Output

```
Processed dataset
```

---

## Notebook 3

### Exploratory Data Analysis

Purpose

- Generate graphs
- Analyze trends
- Identify learning gaps

Output

- Attendance chart
- Assignment chart
- Quiz chart
- Correlation matrix

---

## Notebook 4

### Model Training

Purpose

- Train Random Forest model

Output

```
student_model.pkl
```

---

## Notebook 5

### Model Evaluation

Purpose

Evaluate model performance.

Output

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# 6. Using the Streamlit Dashboard

After launching the dashboard, users can explore different sections.

### Home

Displays project overview.

---

### Dataset Overview

Displays:

- Student records
- Dataset statistics
- Summary information

---

### Learning Analytics

Displays

- Attendance analysis
- Quiz performance
- Assignment analysis
- Engagement analysis

---

### Prediction

Displays

- Student performance prediction
- Performance category

---

### Recommendations

Displays personalized recommendations based on the predicted performance.

Examples

- Improve attendance
- Practice more quizzes
- Increase study hours
- Complete assignments regularly

---

# 7. Understanding the Results

The model classifies students into three categories.

| Prediction | Meaning |
|------------|----------|
| Good | Student is performing well |
| Average | Student requires moderate improvement |
| At Risk | Student requires immediate academic support |

---

# 8. Troubleshooting

## Streamlit Dashboard Not Opening

Run

```bash
streamlit run app.py
```

If the port is occupied.

```bash
streamlit run app.py --server.port 8502
```

---

## Module Not Found

Install missing libraries.

```bash
pip install library_name
```

Example

```bash
pip install streamlit
```

---

## Model File Missing

Run the Model Training notebook again.

Verify

```
models/student_model.pkl
```

exists.

---

## Dataset Missing

Run

```
01_Data_Generation.ipynb
```

again.

---

## Prediction Error

Check that:

- Dataset preprocessing completed successfully.
- Feature names match those used during training.
- The model file is loaded correctly.

---

# 9. Frequently Asked Questions

### Q1. Why is synthetic data used?

Real student data was unavailable, so realistic synthetic data was generated for demonstration purposes.

---

### Q2. Which Machine Learning model is used?

Random Forest Classifier.

---

### Q3. Can I use my own dataset?

Yes.

Replace the generated CSV files with your own dataset while keeping the same column names or updating the preprocessing and training code accordingly.

---

### Q4. How do I retrain the model?

Run:

```
04_Model_Training.ipynb
```

A new model file will be generated.

---

### Q5. How do I update the dashboard?

Retrain the model and restart Streamlit.

---

# 10. Conclusion

The Student Learning Analytics System enables educators and researchers to analyze student performance, detect learning gaps, predict academic outcomes, and generate personalized recommendations using Machine Learning techniques. By following this guide, users can successfully run the complete project, explore the analysis, and interact with the Streamlit dashboard without requiring advanced programming knowledge.

---

# Support

If you encounter issues while using the project:

- Verify all required Python libraries are installed.
- Ensure the notebooks are executed in the correct order.
- Check that all datasets and model files are generated successfully.
- Restart the Streamlit application after making changes.