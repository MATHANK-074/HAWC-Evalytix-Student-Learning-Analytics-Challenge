import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Student Learning Analytics",
    layout="wide"
)

st.title("📚 Student Learning Analytics Dashboard")

# ---------------------------
# Load Data
# ---------------------------
students = pd.read_csv("../data/students.csv")
attendance = pd.read_csv("../data/attendance.csv")
quiz = pd.read_csv("../data/quiz_attempts.csv")
mock = pd.read_csv("../data/mock_tests.csv")
assignment = pd.read_csv("../data/assignments.csv")
engagement = pd.read_csv("../data/engagement.csv")

# ---------------------------
# Prepare Student Summary
# ---------------------------
attendance_avg = attendance.groupby("Student_ID")["Attendance_Percentage"].mean().reset_index()
quiz_avg = quiz.groupby("Student_ID")["Accuracy"].mean().reset_index()
mock_avg = mock.groupby("Student_ID")["Marks"].mean().reset_index()

summary = attendance_avg.merge(quiz_avg, on="Student_ID")
summary = summary.merge(mock_avg, on="Student_ID")

# Performance Label
def performance(row):
    if row["Marks"] >= 80:
        return "High Performer"
    elif row["Marks"] >= 50:
        return "Average"
    else:
        return "At Risk"

summary["Performance"] = summary.apply(performance, axis=1)

# ---------------------------
# KPI Cards
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(students))

col2.metric(
    "High Performer",
    (summary["Performance"] == "High Performer").sum()
)

col3.metric(
    "Average",
    (summary["Performance"] == "Average").sum()
)

col4.metric(
    "At Risk",
    (summary["Performance"] == "At Risk").sum()
)

st.divider()

# ---------------------------
# Attendance Chart
# ---------------------------
st.subheader("Attendance Distribution")

fig = px.histogram(
    attendance,
    x="Attendance_Percentage",
    nbins=20,
    title="Attendance Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Quiz Accuracy
# ---------------------------
st.subheader("Quiz Accuracy")

fig2 = px.histogram(
    quiz,
    x="Accuracy",
    nbins=20,
    title="Quiz Accuracy"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# Mock Marks
# ---------------------------
st.subheader("Mock Test Marks")

fig3 = px.histogram(
    mock,
    x="Marks",
    nbins=20,
    title="Mock Test Marks"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------
# Student Search
# ---------------------------
st.subheader("Search Student")

student = st.text_input("Enter Student ID (Example: STU0001)")

if student:

    data = summary[summary["Student_ID"] == student]

    if not data.empty:

        st.dataframe(data)

        level = data.iloc[0]["Performance"]

        st.success(f"Performance : {level}")

        if level == "High Performer":
            st.info("Recommendation: Keep up the excellent work!")

        elif level == "Average":
            st.warning("Recommendation: Practice more quizzes and revise regularly.")

        else:
            st.error("Recommendation: Increase attendance, complete assignments, and attend doubt-clearing sessions.")

    else:
        st.error("Student ID Not Found")