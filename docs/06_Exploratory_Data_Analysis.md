# Exploratory Data Analysis (EDA)

## Overview

Exploratory Data Analysis (EDA) is a crucial step in the Student Learning Analytics project. It involves examining and visualizing the cleaned dataset to understand student learning patterns, identify trends, detect anomalies, and discover relationships between different academic factors.

The insights obtained during EDA help in selecting important features for the Machine Learning model and identifying students who may require academic intervention.

---

# Objectives

The main objectives of EDA are:

- Understand the structure of the dataset.
- Analyze student academic performance.
- Study attendance patterns.
- Examine assignment and quiz performance.
- Analyze student engagement.
- Identify learning gaps.
- Discover relationships between variables.
- Prepare data for Machine Learning.

---

# Dataset Used

The EDA process uses the cleaned and merged dataset created during the preprocessing stage.

The dataset includes information such as:

- Student ID
- Attendance Percentage
- Assignment Average
- Quiz Average
- Mock Test Average
- Study Hours Per Week
- Engagement Score
- Target Performance Category

---

# EDA Workflow

```
Processed Dataset
        │
        ▼
Dataset Inspection
        │
        ▼
Descriptive Statistics
        │
        ▼
Missing Value Check
        │
        ▼
Distribution Analysis
        │
        ▼
Relationship Analysis
        │
        ▼
Correlation Analysis
        │
        ▼
Learning Gap Identification
        │
        ▼
Insights for Machine Learning
```

---

# Step 1: Dataset Inspection

The first step is to understand the dataset.

The following functions are used:

```python
df.head()
```

Displays the first five records.

```python
df.info()
```

Displays:

- Number of rows
- Number of columns
- Data types
- Missing values

```python
df.describe()
```

Displays statistical information such as:

- Mean
- Median
- Standard deviation
- Minimum
- Maximum
- Quartiles

---

# Step 2: Attendance Analysis

Attendance plays an important role in academic performance.

### Visualization

Histogram

```python
plt.figure(figsize=(8,5))
df["Attendance_Percentage"].hist(bins=10)
plt.title("Attendance Distribution")
plt.xlabel("Attendance Percentage")
plt.ylabel("Number of Students")
plt.show()
```

### Analysis

This visualization helps identify:

- Average attendance
- Students with poor attendance
- Overall attendance distribution

### Interpretation

Students with attendance below **75%** may require academic attention.

---

# Step 3: Assignment Performance Analysis

Assignment scores indicate student consistency.

### Visualization

Bar Chart

```python
plt.figure(figsize=(8,5))
df["Assignment_Average"].plot(kind="hist")
plt.title("Assignment Score Distribution")
plt.show()
```

### Analysis

This graph helps identify:

- High-performing students
- Low-performing students
- Assignment completion trends

---

# Step 4: Quiz Performance Analysis

Quiz scores measure concept understanding.

### Visualization

Histogram

```python
plt.figure(figsize=(8,5))
df["Quiz_Average"].hist(bins=10)
plt.title("Quiz Score Distribution")
plt.show()
```

### Interpretation

Students with consistently low quiz scores may require additional practice.

---

# Step 5: Mock Test Analysis

Mock tests simulate real examinations.

### Visualization

Histogram

```python
plt.figure(figsize=(8,5))
df["Mock_Test_Average"].hist(bins=10)
plt.title("Mock Test Score Distribution")
plt.show()
```

### Insights

The analysis shows:

- Overall exam readiness
- Performance consistency
- Students requiring revision

---

# Step 6: Study Hours Analysis

Weekly study hours significantly influence academic performance.

### Visualization

Histogram

```python
plt.figure(figsize=(8,5))
df["Study_Hours_Per_Week"].hist(bins=10)
plt.title("Weekly Study Hours")
plt.show()
```

### Analysis

This visualization identifies:

- Students spending sufficient study time
- Students with low study commitment

---

# Step 7: Student Engagement Analysis

Engagement reflects the student's interaction with learning resources.

### Visualization

Histogram

```python
plt.figure(figsize=(8,5))
df["Engagement_Score"].hist(bins=10)
plt.title("Student Engagement Score")
plt.show()
```

### Analysis

Higher engagement generally indicates:

- Better learning behavior
- Improved academic performance
- Higher participation

---

# Step 8: Correlation Analysis

Correlation analysis helps understand relationships between different variables.

### Visualization

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))
plt.imshow(df.corr(numeric_only=True), cmap="coolwarm")
plt.colorbar()
plt.title("Correlation Matrix")
plt.show()
```

### Analysis

The correlation matrix helps identify:

- Strong positive relationships
- Negative relationships
- Independent variables

Example:

- Attendance vs Performance
- Study Hours vs Quiz Score
- Engagement vs Assignment Score

---

# Step 9: Learning Gap Identification

EDA helps identify students who require academic support.

Indicators include:

- Low attendance
- Low assignment scores
- Low quiz performance
- Low engagement
- Low mock test scores

These students are classified as **At-Risk Students**.

---

# Key Insights

The exploratory analysis provides the following insights:

- Attendance has a significant impact on academic performance.
- Students with higher engagement generally perform better.
- Assignment completion is positively related to quiz scores.
- Study hours influence mock test performance.
- Low-performing students can be identified before final examinations.

These findings support effective academic interventions.

---

# Visualizations Generated

The EDA notebook generates the following charts:

- Attendance Distribution
- Assignment Score Distribution
- Quiz Score Distribution
- Mock Test Distribution
- Study Hours Distribution
- Engagement Score Distribution
- Correlation Matrix

These visualizations are stored in the **images/** directory for documentation and dashboard integration.

---

# Tools Used

| Tool | Purpose |
|------|---------|
| Pandas | Data analysis |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Scikit-learn | Feature preparation |

---

# Importance of EDA

Exploratory Data Analysis helps in:

- Understanding student learning behavior
- Detecting hidden patterns
- Selecting important features
- Improving machine learning performance
- Supporting data-driven educational decisions

---

# Output

The EDA process produces:

- Statistical summaries
- Data visualizations
- Learning behavior insights
- Correlation analysis
- At-risk student identification
- Feature selection for machine learning

---

# Conclusion

Exploratory Data Analysis transforms raw educational data into meaningful insights. By analyzing attendance, assignments, quizzes, mock tests, study hours, and engagement, the project identifies important learning patterns that guide the Machine Learning model and recommendation engine. The findings from EDA provide a strong foundation for predicting student performance and supporting personalized learning interventions.

---

# Next Document

After completing the Exploratory Data Analysis, proceed to:

**06_Model_Documentation.md**

This document explains the complete Machine Learning pipeline, including feature selection, model training, evaluation, prediction, and model deployment.