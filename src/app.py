import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles Navigate360 Workspace", layout="wide")

# ==========================================
# CENTRALIZED NAVIGATE360 ALIGNED DATA BASE
# ==========================================

# Persistent Session State: Central Student Profile Logs
if "navigate_students_db" not in st.session_state:
    st.session_state.navigate_students_db = pd.DataFrame({
        "student_id": ["KSU-9321", "KSU-4412", "KSU-5591", "KSU-2204", "KSU-7781", "KSU-1104", "KSU-3391", "KSU-8841", "KSU-6621", "KSU-5510"],
        "student_record": ["Student Alpha", "Student Beta", "Student Gamma", "Student Delta", "Student Epsilon", "Student Zeta", "Student Eta", "Student Theta", "Student Iota", "Student Kappa"],
        "student_major": ["Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems & Information Security", "Management", "Marketing", "Marketing"],
        "classification": ["Sophomore", "Freshman", "Senior", "Junior", "Sophomore", "Freshman", "Senior", "Junior", "Sophomore", "Senior"],
        "transfer_student": ["No", "Yes", "No", "No", "Yes", "No", "No", "No", "No", "Yes"],
        "gpa_df_count": [0, 1, 0, 2, 0, 0, 1, 0, 0, 0],
        "withdrawn_courses": [0, 0, 1, 3, 0, 0, 0, 1, 0, 0],
        "cumulative_gpa": [3.31, 2.45, 3.82, 1.95, 2.88, 3.12, 2.15, 3.64, 3.22, 2.95],
        "total_credits_earned": [51.0, 18.0, 94.0, 72.0, 45.0, 14.0, 112.0, 88.0, 62.0, 105.0],
        "credit_completion_pct": [100, 85, 96, 64, 100, 100, 78, 92, 100, 88],
        "predicted_support_level": ["Low Risk", "Medium Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "Medium Risk"],
        "appointment_care_unit": ["Academic Advising", "Academic Advising", "Career Coaching", "Internship & Co-op Advising", "Academic Advising", "Student Engagement", "Academic Advising", "Career Coaching", "Academic Advising", "Professional Sales Track"],
        "assigned_staff_owner": ["Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe", "Sarah Jenkins", "Stacey Nebriaga", "Tyler Pede", "Michael Gabriele", "Thomas Anderson"],
        "reason_category": ["Graduation Check", "Registration Auth", "Resume Polish", "Co-op Sign-off", "Prerequisite Check", "Leadership Intake", "Course Override", "Career Fair Prep", "Change of Major", "Sales Team Vetting"],
        "case_status": ["Open", "In Progress", "Open", "Open", "Resolved", "Open", "In Progress", "Open", "Resolved", "In Progress"],
        "appointment_summary_report": ["", "Reviewing transfer credits from state college.", "", "", "Cleared registration holds and prerequisites.", "", "Processing system registration override permission codes.", "", "Change of major paperwork securely archived.", ""]
    })

# Master Coles Capacity Analytics Reference Frame
coles_capacity_data = pd.DataFrame({
    "major_name": ["Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems & Information Security", "Management", "Marketing", "Professional Sales"],
    "undergrad_seat_count": [1250, 680, 410, 350, 980, 240, 890, 1650, 1420, 310],
    "semester_credit_hours": [18400, 9100, 5200, 4800, 24500, 3100, 9400, 19800, 14200, 3900],
    "retention_goal_pct": [85.0, 88.0, 80.0, 82.0, 82.0, 80.0, 88.0, 80.0, 85.0, 85.0],
    "actual_retention_pct": [82.4, 86.7, 79.1, 81.5, 76.8, 80.2, 89.5, 74.2, 81.1, 84.8]
})

# ==========================================
# NAVIGATE360 NATIVE FILTER SIDEBAR SYSTEM
# ==========================================
st.sidebar.title("🛡️ Navigate360 Context")
st.sidebar.markdown("**Operational Suite:** `Student Success Workstation`")
st.sidebar.write("---")

st.sidebar.subheader("🔍 Filter Parameters")

# 1. Enrollment Major Filter Loop Focus
major_filter = st.sidebar.selectbox(
    "Enrollment History (Major Focus):",
    options=["All Coles Business Majors"] + list(coles_capacity_data["major_name"].unique())
)

# 2. Student Current Classification Filters
class_filter = st.sidebar.selectbox(
    "Current Classification:",
    options=["All Classifications", "Freshman", "Sophomore", "Junior", "Senior"]
)

# 3. Transfer Student Isolation Filter
transfer_filter = st.sidebar.selectbox(
    "Transfer Student Status:",
    options=["All Students", "Yes", "No"]
)

# Processing Selection Matrix
processed_df = st.session_state.navigate_students_db

if major_filter != "All Coles Business Majors":
    processed_df = processed_df[processed_df["student_major"] == major_filter]
if class_filter != "All Classifications":
    processed_df = processed_df[processed_df["classification"] == class_filter]
if transfer_filter != "All Students":
    processed_df = processed_df[processed_df["transfer_student"] == transfer_filter]

st.sidebar.write("---")

# Dashboard Tab Controller Matrix
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Interface Terminal View:",
    ["📋 Staff Home: Caseload Workspace", "📊 Population Health Analytics", "🏛️ University Data Strategy Alignment"]
)

# ==========================================
# MAIN INTERFACE RENDER ENGINE
# ==========================================
st.title("🏛️ Navigate360 — Center for Student Success Control Center")
st.write("---")

# ------------------------------------------
# TERMINAL MODULE 1: STAFF HOME LOGS CASELOAD
# ------------------------------------------
if app_panel == "📋 Staff Home: Caseload Workspace":
    st.header("📋 Staff Home Workspace & Active Appointment Queues")
    
    # 1. Interactive Selection Box to Mount a Specific Profile Target
    if len(processed_df) > 0:
        target_student_id = st.selectbox("Mount Active Student File to Worksurface Workspace ID:", options=processed_df["student_id"].unique())
        
        # Isolate selected record reference data row parameters
        idx = st.session_state.navigate_students_db[st.session_state.navigate_students_db["student_id"] == target_student_id].index[0]
        s_row = st.session_state.navigate_students_db.loc[idx]
        
        # 2. HIGH-DENSITY PROFILE INFRASTRUCTURE SCOREBOARD (Mimicking the System Header Grid Layout)
        with st.container(border=True):
            st.markdown(f"### 👤 Profile Terminal: `{s_row['student_record']}` | ID: `{s_row['student_id']}`")
            st.write("")
            
            # Split Top Metrics Row Bar Interface
            kpi_c1, kpi_c2, kpi_c3, kpi_c4, kpi_c5, kpi_c6, kpi_c7 = st.columns(7)
            with kpi_c1: st.metric("Course Grade D/F", value=int(s_row["gpa_df_count"]))
            with kpi_c2: st.metric("Repeated Courses", value="0")
            with kpi_c3: st.metric("Withdrawn Courses", value=int(s_row["withdrawn_courses"]))
            with kpi_c4: st.metric("Missed Markers", value="0")
            with kpi_c5: st.metric("Cumulative GPA", value=f"{s_row['cumulative_gpa']:.2f}")
            with kpi_c6: st.metric("Total Credits Earned", value=f"{s_row['total_credits_earned']:.1f}")
            with kpi_c7: st.metric("Credit Completion %", value=f"{s_row['credit_completion_pct']}%")
            
        st.write("")
        
        # 3. SPLIT CONSOLE INTERFACE WORK BENCH LAYOUT
        left_profile_col, right_options_col = st.columns([3, 1])
        
        with left_profile_col:
            st.subheader("📝 Institutional Profile Overview")
            with st.container(border=True):
                p_c1, p_c2 = st.columns(2)
                with p_c1:
                    st.markdown(f"**📚 Academic Concentration Major:** `{s_row['student_major']}`")
                    st.markdown(f"**🎯 Classification Level:** `{s_row['classification']}`")
                    st.markdown(f"**🤝 Transfer Route Status:** `{s_row['transfer_student']}`")
                with p_c2:
                    st.markdown(f"**🔮 Predicted Support Level:** `{s_row['predicted_support_level']}`")
                    st.markdown(f"**📂 Active Appointment Care Unit:** `{s_row['appointment_care_unit']}`")
                    st.markdown(f"**👤 Assigned Care Owner Staff:** `{s_row['assigned_staff_owner']}`")
            
            st.write("")
            st.subheader("📥 Active Summary Report Log & Current Appointment Case Details")
            with st.container(border=True):
                st.markdown(f"**Care Reason Category:** `{s_row['reason_category']}` | **Case Status Field:** `{s_row['case_status']}`")
                st.markdown(f"**Appointment Summary Report Log:** *{s_row['appointment_summary_report'] if s_row['appointment_summary_report'] else 'No summary reports recorded for current session touchpoint milestone.'}*")
                
        with right_options_col:
            st.subheader("⚡ Options Workflow")
            # Mimicking Right Sidebar Actions Command Elements Link Panel directly
            with st.container(border=True):
                st.markdown("##### *I want to...*")
                st.button("✉️ Message Student", use_container_width=True)
                st.button("📝 Add a Note on this Student", use_container_width=True)
                st.button("📅 Schedule an Appointment", use_container_width=True)
                
                st.write("---")
                st.markdown("**Modify Database Fields:**")
                state_update = st.selectbox("Update Case Status:", options=["Open", "In Progress", "Resolved"])
                staff_update = st.selectbox("Reassign Staff Owner:", options=["Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe", "Sarah Jenkins"])
                note_add = st.text_input("Append Summary Report Text:")
                
                if st.button("🚀 Commit Changes to Core System Database", use_container_width=True):
                    st.session_state.navigate_students_db.at[idx, "case_status"] = state_update
                    st.session_state.navigate_students_db.at[idx, "assigned_staff_owner"] = staff_update
                    if note_add:
                        st.session_state.navigate_students_db.at[idx, "appointment_summary_report"] = f"{s_row['appointment_summary_report']} | {note_add}".strip(" | ")
                    st.success("Changes successfully tracked!")
                    st.rerun()

    else:
        st.warning("No tracking student files match the active left-hand query parameters filters.")
        
    st.write("---")
    st.subheader("📋 Active Filtered Results Datatable View")
    st.dataframe(processed_df, use_container_width=True, hide_index=True)

# ------------------------------------------
# TERMINAL MODULE 2: POPULATION HEALTH METRICS
# ------------------------------------------
elif app_panel == "📊 Population Health Analytics":
    st.header("📊 Population Health Dashboard & Resource Analytics")
    st.markdown("##### *Monitoring macro-level performance indicators: cumulative GPA trends, credit hours, and target retention gaps.*")
    
    # Filtering Metrics View calculations
    display_metrics = coles_capacity_data if major_filter == "All Coles Business Majors" else coles_capacity_data[coles_capacity_data["major_name"] == major_filter]
    
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        fig_ret = px.bar(display_metrics, x="major_name", y=["retention_goal_pct", "actual_retention_pct"],
                         title="Retention Matrix Analysis: Coles Goals vs. Actual Proportions", barmode="group",
                         color_discrete_sequence=["#FFC400", "#161B22"])
        st.plotly_chart(fig_ret, use_container_width=True)
    with g_col2:
        fig_seats = px.pie(display_metrics, values="undergrad_seat_count", names="major_name", hole=0.4,
                           title="Undergraduate Enrollment Volume Allocations Share", color_discrete_sequence=px.colors.sequential.Golds)
        st.plotly_chart(fig_seats, use_container_width=True)

# ------------------------------------------
# TERMINAL MODULE 3: DATA STRATEGY ALIGNMENT
# ------------------------------------------
elif app_panel == "🏛️ University Data Strategy Alignment":
    st.header("🏛️ Office of University Data Strategy Integration Framework")
    st.markdown("##### *Aligning localized Center for Student Success (CSS) operations with macro-level reporting constraints.*")
    
    compliance_target = st.selectbox(
        "Select Regulatory Compliance Export Gateway Component Loop:",
        ["1. University System of Georgia (USG) - Term Census Headcount Packets",
         "2. Federal IPEDS Matrix Gateway - Annual Institutional Completion Matrix",
         "3. National Rankings Survey (U.S. News & World Report Profiling)"]
    )
    
    with st.container(border=True):
        if "USG" in compliance_target:
            st.markdown("### 🏛️ Alignment Validation: **USG Fall Term Census Data**")
            st.markdown("**Local Coles CSS Validation Signature:** `● Authenticated by Assessment Coordinator`")
            st.info("💡 **USG Core Values Check:** Local transaction counts pass institutional baseline verification test models. Schedulers clear to sync with system-wide pipelines.")
        elif "IPEDS" in compliance_target:
            st.markdown("### 🦅 Alignment Validation: **Federal IPEDS Higher-Ed Compliance**")
            st.markdown("**Local Coles CSS Validation Signature:** `● Audit Complete`")
            st.warning("🔒 **FERPA Safety Shield Engaged:** Small student sample clusters (cell counts under threshold parameters) must enforce automated baseline cell suppression before external compilation.")
        else:
            st.markdown("### 🏆 Alignment Validation: **National Rankings Survey Ingestion**")
            st.markdown("**Local Coles CSS Validation Signature:** `● Verified Pipeline Clear`")
            st.success("🟢 **Operational Directive:** Sourced performance indicators comply precisely with structural ranking survey parameters.")
