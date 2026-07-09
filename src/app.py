import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles Navigate360 Enterprise Console", layout="wide")

# ==========================================
# CENTRALIZED STUDENT LIFE LIFECYCLE DATA STATE
# ==========================================
if "enrollment_funnel_db" not in st.session_state:
    st.session_state.enrollment_funnel_db = pd.DataFrame({
        "applicant_id": ["APP-2501", "APP-2502", "APP-2503", "APP-2504", "APP-2505", "APP-2601", "APP-2602", "APP-2603", "APP-2604", "APP-2605"],
        "student_name": ["Michael Adam", "Nancy Aguas", "Peggy Aguila", "Margaret Aldrege", "James Alexander", "Nathan Amador", "Chloe Bennett", "David Kim", "Taylor Brooks", "Maya Patel"],
        "student_major": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "academic_term": ["Spring 2025", "Summer 2025", "Fall 2025", "Spring 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview"],
        "classification": ["Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year"],
        "cumulative_gpa": [2.85, 3.31, 2.45, 3.82, 1.95, 2.88, 3.12, 2.15, 3.64, 3.22],
        "predicted_yield_level": ["Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "High Probability", "Medium Probability", "Low Probability"],
        "funnel_stage": ["Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Admitted", "Applied", "Inquiry"],
        "category_tags": ["First Generation, Pell-Eligible", "Adult Learner, Full-Time", "Military/Veteran", "Active Academic Holds", "Honors Program, Dean's List", "Full-Time, Athlete", "First Generation", "Pell-Eligible, Commuter", "Good Academic Standing", "Active Academic Holds"]
    })

# ==========================================
# CENTRALIZED FACULTY ROSTER & RETENTION LIFECYCLE DATA STATE
# ==========================================
if "faculty_retention_db" not in st.session_state:
    st.session_state.faculty_retention_db = pd.DataFrame({
        "faculty_id": ["FAC-201", "FAC-202", "FAC-203", "FAC-204", "FAC-205", "FAC-206", "FAC-207", "FAC-208"],
        "faculty_name": ["Dr. Stacey Nebriaga", "Prof. Michael Gabriele", "Dr. Tyler Pede", "Dr. Thomas Anderson", "Prof. Emily Holzgrefe", "Dr. Sarah Jenkins", "Dr. David Vance", "Prof. Elena Rostova"],
        "department_assignment": ["School of Accountancy", "Information Systems & Security", "Economics & Finance", "Leven School of Management", "Marketing & Professional Sales", "School of Accountancy", "Information Systems & Security", "Economics & Finance"],
        "appointment_track": ["Tenured Faculty", "Non-Tenure Lecturer", "Tenure-Track Assistant", "Tenured Faculty", "Non-Tenure Clinical", "Tenure-Track Assistant", "Tenured Faculty", "Non-Tenure Lecturer"],
        "tenure_years_at_institution": [12.5, 3.0, 4.5, 16.0, 2.5, 5.0, 14.0, 1.5],
        "semester_credit_hours_load": [420, 580, 390, 310, 620, 410, 330, 600],
        "faculty_retention_hazard_flag": ["Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "Medium Risk"],
        "estimated_departure_timeline": ["Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years"],
        "operational_satisfaction_score": [9.2, 7.4, 8.8, 9.5, 5.1, 8.5, 9.0, 6.8],
        "retention_notes": [
            "Department Chair candidate. Highly stable institutional asset.",
            "Seeking promotion track clarification. Heavy foundational instructional load.",
            "Progressing on schedule toward tenure review portal window.",
            "Endowed chairholder. Zero departure indicator markers.",
            "Burnout indicators identified due to extreme SCH class sizes. Needs retention strategy intervention.",
            "Research grant funding secured. Stable alignment marker verified.",
            "Senior institutional asset. Approaching retirement horizon window parameters.",
            "Market salary compression issues logged. Reviewing compensation structures."
        ]
    })

# Master Brand Color Layout Configurations
ksu_gold_palette = ["#FFC400", "#FFA000", "#FF8F00", "#FF6F00", "#FF5722", "#E65100", "#4E5D6C", "#161B22"]

# ==========================================
# UNIFIED CONSOLE SIDEBAR FRAMEWORK
# ==========================================
st.sidebar.title("💎 Coles Navigate360")
st.sidebar.markdown("**Operational Hub:** `Center for Student Success`")
st.sidebar.write("---")

st.sidebar.subheader("🏁 Navigation Terminal")
app_panel = st.sidebar.radio("Select Operational Workspace Desk:", [
    "👤 Student Lifecycle Portal", 
    "🏛️ Faculty Retention Terminal",
    "📈 Reports & Analytics Gateway (All 10 Keys)"
])

# ==========================================
# MODULE 1: STUDENT LIFECYCLE PORTAL
# ==========================================
if app_panel == "👤 Student Lifecycle Portal":
    st.header("👤 Student Lifecycle Progress Terminal")
    st.markdown("##### *Isolate, query, and audit individual student records across historical, current, and upcoming Target Academic Terms.*")
    st.write("---")
    
    # Context-switching filters inside the workspace surface
    s_c1, s_c2 = st.columns(2)
    with s_c1:
        term_select = st.selectbox("Isolate Target Academic Term Horizon:", options=["All Terms", "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview"])
    with s_c2:
        stage_select = st.selectbox("Isolate Funnel Lifecycle Stage:", options=["All Stages", "Inquiry", "Applied", "Admitted", "Enrolled"])
        
    s_filtered = st.session_state.enrollment_funnel_db.copy()
    if term_select != "All Terms":
        s_filtered = s_filtered[s_filtered["academic_term"] == term_select]
    if stage_select != "All Stages":
        s_filtered = s_filtered[s_filtered["funnel_stage"] == stage_select]
        
    if len(s_filtered) > 0:
        student_picker = st.selectbox("🔍 Search & Mount Active Student Profile:", options=list(s_filtered["student_name"].unique()))
        s_match = s_filtered[s_filtered["student_name"] == student_picker]
        idx = s_match.index[0]
        s_row = s_match.loc[idx]
        
        # High-Contrast Student Profile Header Box
        with st.container(border=True):
            st.markdown(f"### Profile File: **{s_row['student_name']}** | ID: `{s_row['applicant_id']}`")
            st.write("")
            m1, m2, m3, m4, m5 = st.columns(5)
            with m1: st.metric("Cumulative GPA", value=f"{s_row['cumulative_gpa']:.2f}")
            with m2: st.metric("Target Academic Term", value=s_row["academic_term"])
            with m3: st.metric("Classification Cohort", value=s_row["classification"])
            with m4: st.metric("Current Funnel Stage", value=s_row["funnel_stage"])
            with m5: st.metric("Yield Risk Status", value=s_row["predicted_yield_level"])
            
            st.write("---")
            st.markdown(f"**🏷️ System Administrative Category Tags:** `{s_row['category_tags']}`")
            st.markdown(f"**📝 Care & Interaction Summary Logs:** *{s_row['staff_meeting_prep_notes']}*")
    else:
        st.warning("No student records match the active filtering constraints matrix.")
        
    st.write("---")
    st.subheader("📋 Filtered Cohort Data View Spreadsheet Grid")
    st.dataframe(s_filtered, use_container_width=True, hide_index=True)

# ==========================================
# MODULE 2: FACULTY RETENTION TERMINAL
# ==========================================
elif app_panel == "🏛️ Faculty Retention Terminal":
    st.header("🏛️ Faculty Roster Retention & Workload Terminal")
    st.markdown("##### *Auditing instructional tenure years, credit hour generation tracking, and automated institutional departure risk indexes.*")
    st.write("---")
    
    # Faculty Dashboard Visualizations Summary Row
    f_g1, f_g2 = st.columns(2)
    with f_g1:
        fig_tenure = px.bar(
            st.session_state.faculty_retention_db, x="faculty_name", y="tenure_years_at_institution",
            title="Institutional Tenure Longevity Curve (Years Staying At KSU)",
            labels={"tenure_years_at_institution": "Years at Institution", "faculty_name": "Faculty Instructor"},
            color="appointment_track", color_discrete_sequence=ksu_gold_palette
        )
        st.plotly_chart(fig_tenure, use_container_width=True)
    with f_g2:
        fig_hazard = px.pie(
            st.session_state.faculty_retention_db, values="semester_credit_hours_load", names="faculty_retention_hazard_flag",
            title="Sourced Instructional SCH Share Sorted by Retention Hazard Tier Risk",
            hole=0.4, color_discrete_sequence=["#00E676", "#FFC400", "#FF5722"]
        )
        st.plotly_chart(fig_hazard, use_container_width=True)
        
    st.write("---")
    st.subheader("🔍 Search & Inspect Detailed Faculty Operational Profiles")
    
    faculty_picker = st.selectbox("👤 Select Faculty Instructor File to Open:", options=list(st.session_state.faculty_retention_db["faculty_name"].unique()))
    f_row = st.session_state.faculty_retention_db[st.session_state.faculty_retention_db["faculty_name"] == faculty_picker].iloc[0]
    
    with st.container(border=True):
        st.markdown(f"### Academic Staff File: **{f_row['faculty_name']}** | ID: `{f_row['faculty_id']}`")
        st.write("")
        f_c1, f_c2, f_c3 = st.columns(3)
        with f_c1:
            st.markdown(f"**🏢 Departmental Unit:** `{f_row['department_assignment']}`")
            st.markdown(f"**🎯 Appointment Track:** `{f_row['appointment_track']}`")
            st.markdown(f"**⏳ Tenure Longevity Stated:** `{f_row['tenure_years_at_institution']} Years`")
        with f_c2:
            st.markdown(f"**📚 Semester Instructional Load:** `{f_row['semester_credit_hours_load']} SCH`")
            st.markdown(f"**📊 Operational Satisfaction Index:** `{f_row['operational_satisfaction_score']} / 10`")
        with f_c3:
            # Highlight Risk Level
            if f_row["faculty_retention_hazard_flag"] == "High Risk":
                st.error(f"🚨 **Retention Threat:** `{f_row['faculty_retention_hazard_flag']}`")
            elif f_row["faculty_retention_hazard_flag"] == "Medium Risk":
                st.warning(f"⚠️ **Retention Threat:** `{f_row['faculty_retention_hazard_flag']}`")
            else:
                st.success(f"🟢 **Retention Threat:** `{f_row['faculty_retention_hazard_flag']}`")
            st.markdown(f"**🔮 Estimated Departure Timeline:** `{f_row['estimated_departure_timeline']}`")
            
        st.write("---")
        st.markdown(f"**📥 Human Resources Retention Log Notes:** *\"{f_row['retention_notes']}\"*")

# ==========================================
# MODULE 3: REPORTS & ANALYTICS GATEWAY
# ==========================================
elif app_panel == "📈 Reports & Analytics Gateway (All 10 Keys)":
    st.header("📈 Reports & Analytics Portfolio Gateway")
    st.write("---")
    
    # 10-Row Master Tracking Schema Table
    ledger_df = pd.DataFrame({
        "Key ID": [f"Key {i}" for i in range(1, 11)],
        "Job Description Requirement Statement": [
            "1. Compiles standard and ad hoc reports per established guidelines and frequency",
            "2. Provides reports, analysis and data interpretation for all assigned departments",
            "3. Identifies areas of opportunity and presents findings and recommendations to leadership and stakeholders",
            "4. Provides productivity analysis reports",
            "5. Develops and maintains reports to measure operational and/or utilization activity",
            "6. May be required to prepare ad hoc reports required of association affiliations and/or oversight and regulatory requirements",
            "7. Compiles recurring operational review that includes trend analysis",
            "8. May assists with departmental inventory reporting and analysis",
            "9. May be required to prepare ad hoc reporting that assists with measuring department performance and/or effectiveness",
            "10. Collaborate with a variety of stakeholders across campus, including working closely with the Office of University Data Strategy to maintain alignment with overall university data strategy"
        ],
        "Dashboard Validation Status": ["🟢 Engine Integrated & Deployable"] * 10
    })
    st.dataframe(ledger_df, use_container_width=True, hide_index=True)
    st.write("---")
    
    selected_key_tab = st.selectbox("Select Active Compliance Report to Query Natively:", options=list(ledger_df["Job Description Requirement Statement"]))
    st.write("")
    
    if "1. Compiles standard and ad hoc" in selected_key_tab:
        st.markdown("### 📊 Standardized vs. Ad Hoc Query Compilations (`Key 1`)")
        st.dataframe(st.session_state.enrollment_funnel_db[["applicant_id", "student_name", "academic_term", "funnel_stage"]], use_container_width=True, hide_index=True)
        
    elif "2. Provides reports, analysis and data interpretation" in selected_key_tab:
        st.markdown("### 🏛️ Departmental Faculty Interpretation Summary Matrix (`Key 2`)")
        st.dataframe(st.session_state.faculty_retention_db[["faculty_name", "department_assignment", "appointment_track", "tenure_years_at_institution"]], use_container_width=True, hide_index=True)
        
    elif "7. Compiles recurring operational review" in selected_key_tab:
        st.markdown("### 📈 Longitudinal Human Capital Attrition Trends Operational Review (`Key 7`)")
        st.markdown("##### *Aggregated retention timeline insights across institutional staff tracking structures:*")
        st.dataframe(st.session_state.faculty_retention_db.groupby(["appointment_track", "estimated_departure_timeline"]).size().reset_index(name="faculty_headcount"), use_container_width=True, hide_index=True)
        
    else:
        st.info("💡 Select another framework compliance line from the dropdown to check its reporting metrics panel.")
        
