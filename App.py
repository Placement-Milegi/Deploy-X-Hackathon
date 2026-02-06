import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Student Performance Predictor", layout="centered")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
h1 {
    text-align: center;
    color: white;
}
label {
    color: white !important;
}
.stButton>button {
    width: 100%;
    height: 45px;
    font-size: 18px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎓 Student Performance Predictor</h1>", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
with open("df_model.pkl", "rb") as f:
    model = pickle.load(f)

st.markdown("### 📋 Enter Student Details")

# ---------------- INPUT FIELDS ----------------
Hours_Studied = st.number_input("Hours Studied per Day", 0.0, 24.0, step=0.5)
Attendance = st.number_input("Attendance (%)", 0.0, 100.0, step=1.0)

Parental_Involvement = st.selectbox(
    "Parental Involvement",
    [0, 1, 2],
    format_func=lambda x: ["Low", "Medium", "High"][x]
)

Access_to_Resources = st.selectbox(
    "Access to Resources",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

Extracurricular_Activities = st.selectbox(
    "Extracurricular Activities",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

Sleep_Hours = st.number_input("Sleep Hours per Day", 0.0, 24.0, step=0.5)

Previous_Scores = st.number_input("Previous Exam Score", 0.0, 100.0, step=1.0)

Motivation_Level = st.selectbox(
    "Motivation Level",
    [0, 1, 2],
    format_func=lambda x: ["Low", "Medium", "High"][x]
)

Internet_Access = st.selectbox(
    "Internet Access",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

Tutoring_Sessions = st.number_input("Tutoring Sessions (per month)", 0, 50, step=1)

Family_Income = st.selectbox(
    "Family Income",
    [0, 1, 2],
    format_func=lambda x: ["Low", "Medium", "High"][x]
)

Teacher_Quality = st.selectbox(
    "Teacher Quality",
    [0, 1, 2],
    format_func=lambda x: ["Low", "Medium", "High"][x]
)

School_Type = st.selectbox(
    "School Type",
    [0, 1],
    format_func=lambda x: "Private" if x == 1 else "Public"
)

Peer_Influence = st.selectbox(
    "Peer Influence",
    [0, 1, 2],
    format_func=lambda x: ["Low", "Medium", "High"][x]
)

Physical_Activity = st.number_input(
    "Physical Activity (hours per week)", 0.0, 30.0, step=0.5
)

Learning_Disabilities = st.selectbox(
    "Learning Disabilities",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

# ---------------- PREDICTION ----------------
if st.button("Predict Result"):
    input_df = pd.DataFrame([{
        "Hours_Studied": Hours_Studied,
        "Attendance": Attendance,
        "Parental_Involvement": Parental_Involvement,
        "Access_to_Resources": Access_to_Resources,
        "Extracurricular_Activities": Extracurricular_Activities,
        "Sleep_Hours": Sleep_Hours,
        "Previous_Scores": Previous_Scores,
        "Motivation_Level": Motivation_Level,
        "Internet_Access": Internet_Access,
        "Tutoring_Sessions": Tutoring_Sessions,
        "Family_Income": Family_Income,
        "Teacher_Quality": Teacher_Quality,
        "School_Type": School_Type,
        "Peer_Influence": Peer_Influence,
        "Physical_Activity": Physical_Activity,
        "Learning_Disabilities": Learning_Disabilities
    }])

    prediction = model.predict(input_df)[0]

    st.success("Prediction Completed ✅")
    st.markdown(f"## 📊 **Predicted Output: {prediction}**")
