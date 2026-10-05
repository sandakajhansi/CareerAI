
import streamlit as st
import requests
import pandas as pd

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="CareerAI",
    page_icon="🎯",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"


# =========================
# SIDEBAR
# =========================

st.sidebar.title("🎯 CareerAI")
st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Go to",
    ["🏠 Dashboard", "👨‍🎓 Student Analysis"]
)

st.sidebar.divider()

st.sidebar.info(
    "AI-powered career and skill recommendation system"
)


# =========================
# DASHBOARD PAGE
# =========================

if page == "🏠 Dashboard":

    st.title("🎯 CareerAI")

    st.subheader(
        "AI-Powered Student Career & Skill Recommendation System"
    )

    st.divider()

    st.header("🚀 Welcome to CareerAI")

    st.write(
        """
        CareerAI is an AI-powered student career guidance system.
        It analyzes student skills and provides career recommendations,
        machine learning predictions, skill gap analysis and course
        recommendations.
        """
    )

    st.divider()

    # Dashboard Metrics

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🎓 Student Analysis",
            "Ready"
        )

    with col2:
        st.metric(
            "🤖 ML Prediction",
            "Active"
        )

    with col3:
        st.metric(
            "📊 Skill Analysis",
            "Active"
        )

    with col4:
        st.metric(
            "📚 Courses",
            "Available"
        )

    st.divider()

    # How it works

    st.header("⚙️ How CareerAI Works")

    st.write(
        "1️⃣ Enter your student details"
    )

    st.write(
        "2️⃣ Rate your technical skills"
    )

    st.write(
        "3️⃣ Click **Analyze My Career**"
    )

    st.write(
        "4️⃣ View your career recommendations"
    )

    st.write(
        "5️⃣ Identify skill gaps and recommended courses"
    )

    st.divider()

    # Features

    st.header("✨ CareerAI Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            """
            🎯 **Career Recommendation**

            Get a career recommendation based on
            your technical skills.
            """
        )

        st.info(
            """
            🤖 **Machine Learning Prediction**

            Predict a suitable career using the
            trained ML model.
            """
        )

    with col2:

        st.info(
            """
            ⚠️ **Skill Gap Analysis**

            Identify the skills that need improvement.
            """
        )

        st.info(
            """
            📚 **Course Recommendations**

            Get recommended courses based on your
            current skill gaps.
            """
        )

    st.divider()

    st.success(
        "👉 Go to **Student Analysis** from the sidebar to start."
    )


# =========================
# STUDENT ANALYSIS PAGE
# =========================

else:

    st.title("👨‍🎓 Student Career Analysis")

    st.subheader(
        "Enter your details and analyze your career path"
    )

    st.divider()

    # =========================
    # STUDENT PROFILE
    # =========================

    st.header("👨‍🎓 Student Profile")

    col1, col2, col3 = st.columns(3)

    with col1:

        name = st.text_input(
            "Name",
            value="Jhansi"
        )

        age = st.number_input(
            "Age",
            min_value=15,
            max_value=50,
            value=21
        )

        gender = st.selectbox(
            "Gender",
            ["Female", "Male", "Other"]
        )

    with col2:

        branch = st.text_input(
            "Branch",
            value="CSE"
        )

        cgpa = st.number_input(
            "CGPA",
            min_value=0.0,
            max_value=10.0,
            value=8.5,
            step=0.1
        )

    with col3:

        career_goal = st.text_input(
            "Career Goal",
            value="Data Analyst"
        )

    st.divider()

    # =========================
    # SKILL ASSESSMENT
    # =========================

    st.header("📊 Skill Assessment")

    st.write(
        "Rate your current skill level from 0 to 10."
    )

    col1, col2 = st.columns(2)

    with col1:

        python_score = st.slider(
            "🐍 Python",
            min_value=0,
            max_value=10,
            value=8
        )

        sql_score = st.slider(
            "🗄️ SQL",
            min_value=0,
            max_value=10,
            value=7
        )

    with col2:

        ml_score = st.slider(
            "🤖 Machine Learning",
            min_value=0,
            max_value=10,
            value=6
        )

        power_bi_score = st.slider(
            "📊 Power BI",
            min_value=0,
            max_value=10,
            value=8
        )

    st.divider()

    # =========================
    # ANALYZE BUTTON
    # =========================

    if st.button(
        "🚀 Analyze My Career",
        use_container_width=True
    ):

        student = {

            "name": name,
            "age": age,
            "gender": gender,
            "branch": branch,
            "cgpa": cgpa,

            "python": python_score,
            "sql": sql_score,
            "machine_learning": ml_score,
            "power_bi": power_bi_score,

            "career_goal": career_goal
        }

        try:

            # =========================
            # CREATE STUDENT
            # =========================

            response = requests.post(
                f"{API_URL}/students",
                json=student
            )

            if response.status_code == 200:

                student_data = response.json()

                student_id = student_data["id"]

                # =========================
                # GET RECOMMENDATION
                # =========================

                recommendation_response = requests.get(
                    f"{API_URL}/students/{student_id}/recommendation"
                )

                recommendation = (
                    recommendation_response.json()
                )

                # =========================
                # GET SKILL GAP
                # =========================

                skill_gap_response = requests.get(
                    f"{API_URL}/students/{student_id}/skill-gap"
                )

                skill_gap = (
                    skill_gap_response.json()
                )

                # =========================
                # GET COURSES
                # =========================

                courses_response = requests.get(
                    f"{API_URL}/students/{student_id}/courses"
                )

                courses = (
                    courses_response.json()
                )

                # =========================
                # GET ML PREDICTION
                # =========================

                ml_response = requests.get(
                    f"{API_URL}/students/{student_id}/ml-prediction"
                )

                ml_prediction = (
                    ml_response.json()
                )

                st.success(
                    "✅ Career analysis completed successfully!"
                )

                st.divider()

                # =========================
                # CAREER RESULTS
                # =========================

                st.header("🎯 Career Results")

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Rule-Based Recommendation",
                        recommendation[
                            "recommended_career"
                        ]
                    )

                with col2:

                    st.metric(
                        "🤖 ML Prediction",
                        ml_prediction[
                            "predicted_career"
                        ]
                    )

                st.divider()

                # =========================
                # STUDENT SUMMARY
                # =========================

                st.header("📋 Student Summary")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "Name",
                        name
                    )

                with col2:
                    st.metric(
                        "Branch",
                        branch
                    )

                with col3:
                    st.metric(
                        "CGPA",
                        cgpa
                    )

                with col4:
                    st.metric(
                        "Career Goal",
                        career_goal
                    )

                st.divider()

                # =========================
                # SKILL SCORES
                # =========================

                st.header("📈 Your Skill Scores")

                skill_data = pd.DataFrame(
                    {
                        "Skill": [
                            "Python",
                            "SQL",
                            "Machine Learning",
                            "Power BI"
                        ],

                        "Score": [
                            python_score,
                            sql_score,
                            ml_score,
                            power_bi_score
                        ]
                    }
                )

                st.bar_chart(
                    skill_data.set_index("Skill")
                )

                st.divider()

                # =========================
                # SKILL GAP ANALYSIS
                # =========================

                st.header("⚠️ Skill Gap Analysis")

                if skill_gap["skill_gap"]:

                    for skill, details in (
                        skill_gap["skill_gap"].items()
                    ):

                        st.warning(
                            f"**{skill}** — "
                            f"Current: {details['current']} | "
                            f"Required: {details['required']} | "
                            f"Gap: {details['gap']}"
                        )

                else:

                    st.success(
                        "🎉 No skill gaps found!"
                    )

                st.divider()

                # =========================
                # RECOMMENDED COURSES
                # =========================

                st.header("📚 Recommended Courses")

                recommended_courses = (
                    courses["recommended_courses"]
                )

                if recommended_courses:

                    for course in recommended_courses:

                        st.info(
                            f"📘 {course}"
                        )

                else:

                    st.success(
                        "🎉 No additional courses required."
                    )

                st.divider()

                # =========================
                # PROJECT STATUS
                # =========================

                st.header("✅ Analysis Completed")

                st.success(
                    "Your career analysis includes "
                    "career recommendation, ML prediction, "
                    "skill gap analysis and course recommendations."
                )

            else:

                st.error(
                    "❌ Unable to add student to the backend."
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Backend is not running. "
                "Please start FastAPI first."
            )

        except Exception as e:

            st.error(
                f"❌ Error: {e}"
            )


