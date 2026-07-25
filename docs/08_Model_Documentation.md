# Model Documentation

## Overview

The **Model Documentation** describes the complete Machine Learning pipeline used in the **Student Learning Analytics System**. The primary objective of the model is to predict student academic performance based on various learning indicators such as attendance, assignments, quizzes, mock tests, study habits, and engagement.

The trained model helps identify students who may require additional academic support and enables early intervention through data-driven predictions.

---

# Objectives

The Machine Learning model aims to:

- Predict student performance.
- Identify students at academic risk.
- Support learning gap analysis.
- Generate data-driven insights.
- Improve educational decision-making.

---

# Machine Learning Workflow

```
Processed Dataset
        │
        ▼
Feature Selection
        │
        ▼
Train-Test Split
        │
        ▼
Random Forest Model
        │
        ▼
Model Training
        │
        ▼
Prediction
        │
        ▼
Performance Evaluation
        │
        ▼
Model Saving (.pkl)
        │
        ▼
Streamlit Dashboard
```

---

# Dataset Used

The model is trained using the **processed dataset** generated after data preprocessing.

### Input Features

| Feature | Description |
|----------|-------------|
| Attendance_Percentage | Student attendance percentage |
| Assignment_Average | Average assignment score |
| Quiz_Average | Average quiz score |
| Mock_Test_Average | Average mock test score |
| Study_Hours_Per_Week | Weekly study hours |
| Engagement_Score | Student engagement score |

### Target Variable

| Target | Description |
|---------|-------------|
| Performance | Student performance category (Good / Average / At Risk) |

---

# Feature Selection

Only relevant academic indicators are selected for model training.

Selected features:

- Attendance Percentage
- Assignment Average
- Quiz Average
- Mock Test Average
- Study Hours Per Week
- Engagement Score

These features have the greatest influence on student performance prediction.

---

# Data Splitting

The dataset is divided into **training** and **testing** sets.

Typical split:

| Dataset | Percentage |
|----------|------------|
| Training Data | 80% |
| Testing Data | 20% |

Example:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
```

Using separate testing data ensures unbiased model evaluation.

---

# Machine Learning Algorithm

## Random Forest Classifier

The project uses the **Random Forest Classifier**, an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Why Random Forest?

- High prediction accuracy
- Handles numerical features effectively
- Resistant to overfitting
- Suitable for classification tasks
- Works well on structured datasets
- Requires minimal feature scaling

---

# Model Training

The model is trained using the selected features.

Example:

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
```

During training, the model learns the relationship between academic indicators and student performance.

---

# Model Prediction

After training, predictions are generated using the testing dataset.

Example:

```python
y_pred = model.predict(X_test)
```

The model predicts the performance category for each student.

Example output:

| Student | Prediction |
|----------|------------|
| Student 1 | Good |
| Student 2 | Average |
| Student 3 | At Risk |

---

# Model Evaluation

The trained model is evaluated using standard classification metrics.

## Accuracy

Measures the proportion of correct predictions.

```python
accuracy_score(y_test, y_pred)
```

---

## Precision

Measures how many predicted positive cases are actually correct.

```python
precision_score()
```

---

## Recall

Measures how many actual positive cases are correctly identified.

```python
recall_score()
```

---

## F1 Score

The harmonic mean of precision and recall.

```python
f1_score()
```

---

## Classification Report

Provides a detailed summary of model performance.

Example:

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

---

## Confusion Matrix

Shows the number of correct and incorrect predictions.

Example:

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
```

A confusion matrix helps visualize model performance across different classes.

---

# Model Performance

The model is evaluated based on:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Higher values indicate better prediction performance.

---

# Model Saving

After successful training, the model is saved for future use.

Example:

```python
import joblib

joblib.dump(model, "models/student_model.pkl")
```

Saved model:

```
models/
└── student_model.pkl
```

Saving the model avoids retraining each time the application is executed.

---

# Model Loading

The saved model is loaded during dashboard execution.

Example:

```python
import joblib

model = joblib.load("models/student_model.pkl")
```

The loaded model is used to generate predictions in real time.

---

# Prediction Pipeline

```
Student Data
      │
      ▼
Feature Extraction
      │
      ▼
Random Forest Model
      │
      ▼
Performance Prediction
      │
      ▼
Learning Gap Detection
      │
      ▼
Recommendations
```

---

# Integration with Dashboard

The trained model is integrated into the Streamlit dashboard.

Dashboard capabilities:

- Load trained model
- Accept student input
- Predict student performance
- Display prediction results
- Show personalized recommendations

---

# Advantages of the Model

- Fast training and prediction
- High classification accuracy
- Handles multiple academic features
- Robust against overfitting
- Easy integration with Streamlit
- Suitable for educational analytics

---

# Limitations

- Trained on synthetic data rather than real student records.
- Prediction quality depends on data quality.
- Does not consider external factors such as socioeconomic conditions or personal circumstances.
- Future performance may improve with larger real-world datasets.

---

# Future Improvements

Potential enhancements include:

- Training on real educational datasets
- Hyperparameter tuning
- Cross-validation
- Feature importance analysis
- Deep Learning models
- XGBoost or LightGBM comparison
- Real-time prediction using live LMS data

---

# Conclusion

The Random Forest model serves as the core predictive component of the Student Learning Analytics System. By analyzing attendance, assignments, quizzes, mock tests, study habits, and engagement, the model accurately classifies student performance and supports early identification of at-risk learners. Its integration with the Streamlit dashboard enables educators to make informed decisions and provide timely academic interventions.

---

# Next Document

After completing the Model Documentation, proceed to:

**09_Dashboard_Documentation.md**

This document explains the Streamlit dashboard architecture, pages, visualizations, prediction interface, and user interaction workflow.