# Dataset Documentation

## Overview

The **Student Learning Analytics System** uses multiple synthetic datasets to simulate the academic activities and learning behavior of students. Since real educational data was not available, these datasets were generated programmatically to resemble realistic student records.

Each dataset represents a specific aspect of student learning, such as attendance, assignments, quizzes, mock tests, engagement, and video learning activity. Together, these datasets provide a comprehensive foundation for learning analytics and machine learning.

---

# Dataset Collection

The project contains the following datasets:

| Dataset | Description |
|----------|-------------|
| students.csv | Basic student information |
| attendance.csv | Student attendance records |
| assignments.csv | Assignment scores and submission details |
| engagement.csv | Student engagement metrics |
| quiz_attempts.csv | Quiz performance records |
| mock_tests.csv | Mock examination results |
| video_logs.csv | Video learning activity |

---

# Dataset Relationships

All datasets are connected using the **Student_ID** field.

```
                  Student_ID
                      │
     ┌────────────────┼────────────────┐
     │                │                │
     ▼                ▼                ▼
students.csv    attendance.csv   assignments.csv
     │                │                │
     ├────────────┬───┴───────┬────────┤
     │            │           │
     ▼            ▼           ▼
quiz_attempts.csv engagement.csv mock_tests.csv
     │
     ▼
video_logs.csv
```

---

# 1. students.csv

## Purpose

This dataset stores the demographic and academic profile of each student.

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| Student_ID | Integer | Unique identifier for each student |
| Student_Name | String | Full name of the student |
| Gender | String | Male or Female |
| Age | Integer | Student age |
| Grade | String | Academic level or class |
| Course | String | Program enrolled (JEE, NEET, CBSE, ICSE, Foundation) |

### Sample Record

| Student_ID | Student_Name | Gender | Age | Grade | Course |
|------------|--------------|--------|-----|--------|---------|
| 1001 | Rahul Sharma | Male | 17 | Grade 12 | JEE |

---

# 2. attendance.csv

## Purpose

Stores attendance information for each student.

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| Student_ID | Integer | Student identifier |
| Attendance_Percentage | Float | Overall attendance percentage |
| Present_Days | Integer | Number of days attended |
| Total_Days | Integer | Total working days |

### Sample Record

| Student_ID | Attendance_Percentage | Present_Days | Total_Days |
|------------|----------------------|--------------|------------|
| 1001 | 88.50 | 177 | 200 |

---

# 3. assignments.csv

## Purpose

Stores assignment submission and performance details.

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| Student_ID | Integer | Student identifier |
| Assignment_Average | Float | Average assignment score |
| Assignments_Submitted | Integer | Number of assignments submitted |
| Total_Assignments | Integer | Total assignments assigned |

### Sample Record

| Student_ID | Assignment_Average | Assignments_Submitted | Total_Assignments |
|------------|-------------------|-----------------------|-------------------|
| 1001 | 84.20 | 18 | 20 |

---

# 4. engagement.csv

## Purpose

Measures student engagement with learning activities.

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| Student_ID | Integer | Student identifier |
| Study_Hours_Per_Week | Float | Weekly study hours |
| Engagement_Score | Float | Overall engagement score |
| Login_Frequency | Integer | Weekly platform logins |
| Consecutive_Study_Days | Integer | Continuous study streak |

### Sample Record

| Student_ID | Study_Hours_Per_Week | Engagement_Score | Login_Frequency | Consecutive_Study_Days |
|------------|----------------------|------------------|-----------------|------------------------|
| 1001 | 22.5 | 87 | 15 | 8 |

---

# 5. quiz_attempts.csv

## Purpose

Stores quiz performance records.

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| Student_ID | Integer | Student identifier |
| Quiz_Average | Float | Average quiz score |
| Quizzes_Attempted | Integer | Number of quizzes attempted |

### Sample Record

| Student_ID | Quiz_Average | Quizzes_Attempted |
|------------|--------------|-------------------|
| 1001 | 79.60 | 24 |

---

# 6. mock_tests.csv

## Purpose

Stores mock examination performance.

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| Student_ID | Integer | Student identifier |
| Mock_Test_Average | Float | Average mock test score |
| Mock_Tests_Attended | Integer | Number of mock tests attended |

### Sample Record

| Student_ID | Mock_Test_Average | Mock_Tests_Attended |
|------------|-------------------|---------------------|
| 1001 | 82.70 | 10 |

---

# 7. video_logs.csv

## Purpose

Stores student video learning activity.

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| Student_ID | Integer | Student identifier |
| Videos_Watched | Integer | Total videos watched |
| Video_Watch_Time_Hours | Float | Total watch time in hours |

### Sample Record

| Student_ID | Videos_Watched | Video_Watch_Time_Hours |
|------------|----------------|------------------------|
| 1001 | 145 | 96.50 |

---

# Data Generation Process

The datasets were generated using Python with randomization techniques to simulate realistic educational records.

The following libraries were used:

- pandas
- numpy
- random
- faker

Each dataset was exported as a CSV file and stored in the `data/` directory.

---

# Data Preprocessing

Before analysis, the datasets undergo preprocessing steps including:

- Checking for missing values
- Removing duplicate records
- Verifying data types
- Merging datasets using `Student_ID`
- Feature engineering
- Creating the final processed dataset

---

# Feature Summary

The following features are used for machine learning:

| Feature | Description |
|----------|-------------|
| Attendance_Percentage | Student attendance rate |
| Assignment_Average | Average assignment score |
| Quiz_Average | Average quiz score |
| Mock_Test_Average | Average mock test score |
| Study_Hours_Per_Week | Weekly study hours |
| Engagement_Score | Student engagement level |

These features help predict student performance and identify learning gaps.

---

# Data Quality Measures

To ensure dataset quality, the following checks were performed:

- No duplicate Student_ID values
- Valid numeric ranges
- Consistent data types
- Realistic score distributions
- Proper foreign key relationship using `Student_ID`

---

# Dataset Usage

The datasets are used throughout different stages of the project.

| Stage | Dataset Usage |
|--------|---------------|
| Data Generation | Create synthetic student records |
| Preprocessing | Clean and merge datasets |
| EDA | Analyze learning patterns |
| Machine Learning | Train prediction model |
| Dashboard | Display visualizations and predictions |

---

# Storage Location

All generated datasets are stored in the following directory:

```
Student-Learning-Analytics/
│
├── data/
│   ├── students.csv
│   ├── attendance.csv
│   ├── assignments.csv
│   ├── engagement.csv
│   ├── quiz_attempts.csv
│   ├── mock_tests.csv
│   └── video_logs.csv
```

---

# Conclusion

The synthetic datasets provide a realistic representation of student academic performance and learning behavior. By combining information from multiple sources through the `Student_ID` field, the project enables comprehensive learning analytics, machine learning-based performance prediction, and personalized recommendations. These datasets form the foundation of the Student Learning Analytics System and support all subsequent stages of the project.