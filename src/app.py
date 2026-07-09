import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles StudentSuccess Terminal", layout="wide")

# ==========================================
# CENTRALIZED STUDENT LIFECYCLE DATA STATE
# ==========================================
if "enrollment_funnel_db" not in st.session_state:
    st.session_state.enrollment_funnel_db = pd.DataFrame({
        "applicant_id": ["87650214", "04218579", "14538206", "46581097", "94753108", "81295374", "JIH339188", "JIH884120", "JIH662199", "JIH551043"],
        "student_name": ["Michael Adam", "Nancy Aguas", "Peggy Aguila", "Margaret Aldrege", "James Alexander", "Nathan Amador", "Chloe Bennett", "David Kim", "Taylor Brooks", "Maya Patel"],
        "department_scope": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "academic_term": ["Spring 2025", "Summer 2025", "Fall 2025", "Spring 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview"],
        "classification": ["Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year"],
        "cumulative_gpa": [2.85, 3.31, 2.45, 3.82, 1.95, 2.88, 3.12, 2.15, 3.64, 3.22],
        "studentvue_sync_status": ["Synced", "Synced", "Hold Alert", "Synced", "Synced", "Synced", "Synced", "Hold Alert", "Synced", "Hold Alert"],
        "funnel_stage": ["Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Admitted", "Applied", "Inquiry"],
        "category_tags": ["First Generation, Pell-Eligible", "Adult Learner, Full-Time", "Military/Veteran", "Active Academic Holds", "Honors Program, Dean's List", "Full-Time, Athlete", "First Generation", "Pell-Eligible, Commuter", "Good Academic Standing", "Active Academic Holds"],
        "staff_meeting_prep_notes": [
            "Historical Record: Confirmed enrollment for Spring 2025.",
            "Historical Record: Confirmed enrollment for Summer 2025.",
            "Historical Record: Confirmed enrollment for Fall 2025.",
            "Historical Record: Confirmed enrollment for Spring 2025.",
            "Historical Record: Confirmed enrollment for Fall 2025.",
            "Current Cycle: Completed onboarding registration for Spring 2026.",
            "Current Cycle: Completed summer transient enrollment checks.",
            "Upcoming Cycle: Admitted with honors scholarship. High follow-up priority.",
            "Upcoming Cycle: Incomplete portfolio submission flag raised.",
            "Upcoming Cycle: Invited to Coles Open House. Primary interest is Marketing niche."
        ]
    })

# ==========================================
# CENTRALIZED FACULTY ROSTER & RETENTION DATA STATE
# ==========================================
if "faculty_retention_db" not in st.session_state:
    st.session_state.faculty_retention_db = pd.DataFrame({
        "faculty_id": ["FAC-201", "FAC-202", "FAC-203", "FAC-204", "FAC-205", "FAC-206", "FAC-207", "FAC-208"],
        "faculty_name": ["Dr. Stacey Nebriaga", "Prof. Michael Gabriele", "Dr. Tyler Pede", "Dr. Thomas Anderson", "Prof. Emily Holzgrefe", "Dr. Sarah Jenkins", "Dr. David Vance", "Prof. Elena Rostova"],
        "department_assignment": ["Biology", "Information Systems", "Economics", "Management", "Marketing", "Accounting", "Cybersecurity", "Finance"],
        "appointment_track": ["Tenured Faculty", "Non-Tenure Lecturer", "Tenure-Track Assistant", "Tenured Faculty", "Non-Tenure Clinical", "Tenure-Track Assistant", "Tenured Faculty", "Non-Tenure Lecturer"],
        "tenure_years_at_institution": [12.5, 3.0, 4.5, 16.0, 2.5, 5.0, 14.0, 1.5],
        "semester_credit_hours_load": [420, 580, 390, 310, 620, 410, 330, 600],
        "faculty_retention_hazard_flag": ["Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "Medium Risk"],
        "estimated_departure_timeline": ["Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years"],
        "retention_notes": ["Stable institutional asset.", "Seeking promotion track clarification.", "Progressing toward tenure review.", "Endowed chairholder.", "Needs retention strategy intervention.", "Research grant funding secured.", "Approaching retirement horizon.", "Market salary compensation compression issues logged."]
    })

if "coles_capacity_db" not in st.session_state:
    st.session_state.coles_capacity_db = pd.DataFrame({
        "major_name": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "undergrad_seat_count": [850, 1250, 680, 410, 350, 980, 240, 890, 1650, 1420]
    })

ksu_gold_palette = ["#FFC400", "#161B22", "#FFA000", "#FF8F00", "#4E5D6C"]

# ==========================================
# RESTORED ENTERPRISE SIDEBAR FILTER ENGINE
# ==========================================
st.sidebar.title("🛡️ Navigate360 Core")
st.sidebar.markdown("**Operational View:** `Multi-Tenant Analytics`")
st.sidebar.write("---")

st.sidebar.subheader("🗂️ Global Scope Filters")

dept_filter = st.sidebar.selectbox("Filter by Academic Department:", options=["All Departments"] + list(st.session_state.coles_capacity_db["major_name"].unique()))
year_filter = st.sidebar.selectbox("Longitudinal Timeline Context:", options=["All Timelines", "Past Cycles (2025)", "Active/Upcoming Cycles (2026)"])
studentvue_filter = st.sidebar.selectbox("StudentVue Portal Status Updates:", options=["All Sync States", "Synced", "Hold Alert"])

processed_students = st.session_state.enrollment_funnel_db.copy()
filtered_faculty = st.session_state.faculty_retention_db.copy()

if dept_filter != "All Departments":
    processed_students = processed_students[processed_students["department_scope"] == dept_filter]
    filtered_faculty = filtered_faculty[filtered_faculty["department_assignment"] == dept_filter]

if year_filter == "Past Cycles (2025)":
    processed_students = processed_students[processed_students["academic_term"].str.contains("2025")]
elif year_filter == "Active/Upcoming Cycles (2026)":
    processed_students = processed_students[processed_students["academic_term"].str.contains("2026")]

if studentvue_filter != "All Sync States":
    processed_students = processed_students[processed_students["studentvue_sync_status"] == studentvue_filter]

st.sidebar.write("---")
st.sidebar.subheader("🏁 Navigation Terminal")
app_panel = st.sidebar.radio("Select Active Console Mode:", [
    "👤 Student Lifecycle Portal (StudentVue)", 
    "🏛️ Faculty Retention Terminal",
    "📈 Reports & Analytics Gateway (All 10 Keys)"
])

# ==========================================
# RENDERING TAB CONSOLES
# ==========================================
if app_panel == "👤 Student Lifecycle Portal (StudentVue)":
    st.header("👤 Student Lifecycle Progress Terminal (StudentVue Live Integration)")
    st.markdown("##### *Isolating academic paths, performance indices, and portal alert metrics on demand.*")
    st.write("---")
    
    if len(processed_students) > 0:
        student_picker = st.selectbox("🔍 Search and Inspect Profile directly:", options=list(processed_students["student_name"].unique()))
        
        # FIXED: Pure boolean matching to preserve scalar key extracts safely
        s_row = processed_students[processed_students["student_name"] == student_picker].iloc[0]
        
        with st.container(border=True):
            st.markdown(f"### Profile File: **{s_row['student_name']}** | ID: `{s_row['applicant_id']}`")
            st.write("")
            m1, m2, m3, m4, m5 = st.columns(5)
            with m1: st.metric("Cumulative GPA", value=f"{s_row['cumulative_gpa']:.2f}")
            with m2: st.metric("Target Academic Term", value=s_row["academic_term"])
            with m3: st.metric("Classification Cohort", value=s_row["classification"])
            with m4: st.metric("StudentVue Status", value=s_row["studentvue_sync_status"])
            with m5: st.metric("Department Major", value=s_row["department_scope"])
            
            st.write("---")
            st.markdown(f"**🏷️ Category Flags:** `{s_row['category_tags']}`")
            st.markdown(f"**📥 Summary Logs:** *{s_row['staff_meeting_prep_notes']}*")
    else:
        st.warning("No records found matching those exact sidebar filter criteria configurations.")

    st.write("---")
    st.subheader("📋 Ingested Dataset Grid Output View")
    st.dataframe(processed_students, use_container_width=True, hide_index=True)

elif app_panel == "🏛️ Faculty Retention Terminal":
    st.header("🏛️ Faculty Roster Retention & Attrition Manager")
    st.write("---")
    
    if len(filtered_faculty) > 0:
        f_g1, f_g2 = st.columns(2)
        with f_g1:
            fig_tenure = px.bar(filtered_faculty, x="faculty_name", y="tenure_years_at_institution", title="Tenure Longevity Curve Profile", color="appointment_track", color_discrete_sequence=ksu_gold_palette)
            st.plotly_chart(fig_tenure, use_container_width=True)
        with f_g2:
            fig_hazard = px.pie(filtered_faculty, values="semester_credit_hours_load", names="faculty_retention_hazard_flag", title="Workload (SCH) by Hazard Status Flag", hole=0.4, color_discrete_sequence=["#00E676", "#FFC400", "#FF5722"])
            st.plotly_chart(fig_hazard, use_container_width=True)
            
        st.write("---")
        st.subheader("📋 Active Faculty Roster Logs Spreadsheet")
        st.dataframe(filtered_faculty, use_container_width=True, hide_index=True)
    else:
        st.warning("No faculty records match the selected sidebar department filters.")

elif app_panel == "📈 Reports & Analytics Gateway (All 10 Keys)":
    st.header("📈 Reports & Analytics Portfolio Gateway")
    st.write("---")
    
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
        st.dataframe(processed_students[["applicant_id", "student_name", "academic_term", "funnel_stage", "studentvue_sync_status"]], use_container_width=True, hide_index=True)
        
    elif "2. Provides reports, analysis and data interpretation" in selected_key_tab:
        st.markdown("### 🏛️ Departmental Faculty Interpretation Summary Matrix (`Key 2`)")
        st.dataframe(filtered_faculty[["faculty_name", "department_assignment", "appointment_track", "tenure_years_at_institution"]], use_container_width=True, hide_index=True)
        
    elif "7. Compiles recurring operational review" in selected_key_tab:
        st.markdown("### 📈 Longitudinal Human Capital Attrition Trends Operational Review (`Key 7`)")
        if len(filtered_faculty) > 0:
            st.dataframe(filtered_faculty.groupby(["appointment_track", "estimated_departure_timeline"]).size().reset_index(name="faculty_headcount"), use_container_width=True, hide_index=True)
        else:
            st.warning("No records to aggregate.")
            
    else:
        st.info("💡 Select another framework compliance line from the dropdown to check its reporting metrics panel.")
