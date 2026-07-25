# Data Preprocessing

## Overview

Data preprocessing is one of the most important phases in the Student Learning Analytics project. The quality of the Machine Learning model depends on the quality of the input data. During this stage, the generated datasets are cleaned, transformed, validated, and prepared for analysis and model training.

The preprocessing pipeline ensures that the data is accurate, consistent, and suitable for machine learning algorithms.

---

# Objectives

The main objectives of data preprocessing are:

- Clean the generated datasets
- Remove duplicate records
- Handle missing values
- Verify data types
- Merge multiple datasets
- Create useful features
- Prepare the final dataset for Machine Learning

---

# Input Datasets

The preprocessing stage uses the following datasets:

- students.csv
- attendance.csv
- assignments.csv
- engagement.csv
- quiz_attempts.csv
- mock_tests.csv
- video_logs.csv

Each dataset contains different information about student learning activities.

---

# Data Preprocessing Workflow

```
Raw CSV Files
      │
      ▼
Load Datasets
      │
      ▼
Data Inspection
      │
      ▼
Missing Value Check
      │
      ▼
Duplicate Removal
      │
      ▼
Data Type Validation
      │
      ▼
Dataset Merging
      │
      ▼
Feature Engineering
      │
      ▼
Processed Dataset
      │
      ▼
Machine Learning
```

---

# Step 1: Load the Datasets

All CSV files are loaded into Pandas DataFrames.

Example:

```python
students = pd.read_csv("students.csv")
attendance = pd.read_csv("attendance.csv")
assignments = pd.read_csv("assignments.csv")
engagement = pd.read_csv("engagement.csv")
quiz = pd.read_csv("quiz_attempts.csv")
mock = pd.read_csv("mock_tests.csv")
videos = pd.read_csv("video_logs.csv")
```

This allows efficient data manipulation and analysis.

---

# Step 2: Data Inspection

Each dataset is inspected to understand its structure.

The following checks are performed:

- Number of rows
- Number of columns
- Data types
- Sample records
- Statistical summary

Common Pandas functions used:

```python
df.head()

df.info()

df.describe()
```

---

# Step 3: Missing Value Detection

The datasets are checked for missing or null values.

Example:

```python
df.isnull().sum()
```

### Handling Strategy

- If no missing values are found, no action is required.
- If missing values exist, they may be:
  - Filled using mean or median (numerical data)
  - Filled using mode (categorical data)
  - Removed if the records are invalid

Maintaining complete data improves model accuracy.

---

# Step 4: Duplicate Record Removal

Duplicate records can negatively affect data analysis and model training.

Duplicates are identified using:

```python
df.duplicated().sum()
```

If duplicates exist, they are removed using:

```python
df.drop_duplicates(inplace=True)
```

This ensures that each student record is unique.

---

# Step 5: Data Type Validation

Each column is checked to ensure it has the correct data type.

Example:

| Column | Expected Type |
|---------|---------------|
| Student_ID | Integer |
| Attendance_Percentage | Float |
| Assignment_Average | Float |
| Quiz_Average | Float |
| Engagement_Score | Float |

Incorrect data types are converted where necessary.

Example:

```python
df["Attendance_Percentage"] = df["Attendance_Percentage"].astype(float)
```

---

# Step 6: Dataset Merging

The individual datasets are merged into a single dataset using the common key:

```
Student_ID
```

Example:

```python
merged_df = students.merge(attendance, on="Student_ID")
```

Additional datasets are merged similarly until a complete dataset is obtained.

Benefits of merging:

- Combines all student information
- Simplifies analysis
- Creates a unified dataset for machine learning

---

# Step 7: Feature Selection

Only relevant features are selected for model training.

Example features:

- Attendance_Percentage
- Assignment_Average
- Quiz_Average
- Mock_Test_Average
- Study_Hours_Per_Week
- Engagement_Score

Removing unnecessary columns improves model performance and reduces computational complexity.

---

# Step 8: Feature Engineering

Feature engineering creates new variables from existing data to improve model performance.

Examples include:

- Average academic score
- Attendance category
- Performance level
- Learning risk category
- Overall engagement score

These engineered features provide additional insights for prediction.

---

# Step 9: Data Validation

The final dataset is validated before training the machine learning model.

Validation checks include:

- Correct number of records
- No duplicate Student_ID values
- No missing values
- Correct data types
- Valid numerical ranges

This ensures the dataset is reliable and ready for analysis.

---

# Processed Dataset

The final processed dataset contains the cleaned and merged information required for machine learning.

Example structure:

| Student_ID | Attendance | Assignment | Quiz | Mock Test | Engagement | Target |
|------------|------------|------------|------|-----------|------------|--------|
| 1001 | 88.5 | 84.2 | 79.6 | 82.7 | 87 | Good |

The processed dataset serves as the primary input for the prediction model.

---

# Benefits of Data Preprocessing

Data preprocessing provides several advantages:

- Improves data quality
- Reduces inconsistencies
- Removes duplicate records
- Ensures correct data types
- Enhances machine learning accuracy
- Produces reliable analytical insights

---

# Preprocessing Tools

The following Python libraries were used:

| Library | Purpose |
|----------|---------|
| Pandas | Data loading and manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning preprocessing |
| Matplotlib | Data visualization |

---

# Output

The preprocessing stage produces:

- Cleaned datasets
- Merged dataset
- Machine learning-ready dataset
- Improved data quality
- Reliable input for analysis and prediction

---

# Summary

The data preprocessing stage transforms raw synthetic educational datasets into a structured and reliable format suitable for machine learning and analytics. By performing data cleaning, validation, merging, and feature engineering, the project ensures that only high-quality data is used for learning gap analysis, student performance prediction, and personalized recommendation generation.

---

# Next Document

After preprocessing, the next step is:

**05_Exploratory_Data_Analysis.md**

This document explains how the cleaned data is analyzed using statistical methods and visualizations to understand student learning behavior and identify important patterns.