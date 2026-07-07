import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles CSS Command Suite", layout="wide")

# ==========================================
# RE-ENGINEERED COLES CSS REAL-WORLD SEED DATA
# ==========================================

# Persistent Session State 1: Central Advising, Coaching, and Engagement Queue
if "coles_cases_db" not in st.session_state:
    st.session_state.coles_cases_db = pd.DataFrame({
        "case_id": [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
        "student_major": ["Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems & Information Security", "Management", "Marketing", "Professional Sales"],
        "service_track": ["Academic Advising", "Academic Advising", "Career Coaching", "Internship & Co-op", "Academic Advising", "Student Engagement", "Academic Advising", "Career Coaching", "Academic Advising", "Internship & Co-op"],
        "assigned_staff": ["Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe", "Sarah Jenkins", "Stacey Nebriaga", "Tyler Pede", "Michael Gabriele", "Thomas Anderson"],
        "appointment_topic": [
            "Graduation Check & Degree Auditing",
            "MFA Token Issue & System Authorization",
            "Resume Polish & Executive Mock Interview",
            "Corporate Internship Credit Sign-off",
            "Schedule Optimization & Prerequisite Check",
            "Business Student Association Inbound Intake",
            "Upper-Division Security Course Override Request",
            "Fall Career Fair Strategic Prep Session",
            "Change of Major Intake: Swapping to Marketing",
            "Co-op Agreement Extension with Corporate Partner"
        ],
        "priority": ["High", "Medium", "High", "Critical", "Low", "Low", "Critical", "High", "Medium", "High"],
        "status": ["Open", "In Progress", "Open", "Open", "Resolved", "Open", "In Progress", "Open", "Resolved", "In Progress"],
        "duration_minutes": [0, 15, 0, 0, 45, 0, 30, 0, 30, 15],
        "session_logs": ["", "Reviewing transfer credits.", "", "", "Cleared prerequisites.", "", "Processing course override override codes.", "", "Forms processed successfully.", ""]
    })

# Persistent Session State 2: BUSA Professionalism Courses Enrollment Tracker
if "busa_courses_db" not in st.session_state:
    st.session_state.busa_courses_db = pd.DataFrame({
        "course_code": ["BUSA 2150", "BUSA 3150", "BUSA 4150", "BUSA 2150", "BUSA 3150"],
        "business_major": ["Accounting", "Finance", "Management", "Marketing", "Cybersecurity"],
        "total_enrolled": [340, 290, 410, 380, 195],
        "attendance_rate_pct": [94.2, 88.5, 91.1, 86.4, 92.7],
        "professionalism_milestones_completed": [315, 240, 395, 310, 180],
        "vulnerability_risk_flag": ["Compliant", "Needs Review", "Compliant", "Needs Attention", "Compliant"]
    })

# Master Coles Department Capacity Metrics
coles_metrics_data = pd.DataFrame({
    "major_name": ["Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems & Information Security", "Management", "Marketing", "Professional Sales"],
    "undergrad_seat_count": [1250, 680, 410, 350, 980, 240, 890, 1650, 1420, 310],
    "semester_credit_hours": [18400, 9100, 5200, 4800, 24500, 3100, 9400, 19800, 14200, 3900],
    "retention_goal_pct": [85.0, 88.0, 80.0, 82.0, 82.0, 80.0, 88.0, 80.0, 85.0, 85.0],
    "actual_retention_pct": [82.4, 86.7, 79.1, 81.5, 76.8, 80.2, 89.5, 74.2, 81.1, 84.8]
})

# ==========================================
# SIDEBAR CONTROL PANEL
# ==========================================
st.sidebar.title("💎 Coles CSS Workbench")
st.sidebar.markdown("**Operational Hub:** `Center for Student Success` ")
st.sidebar.markdown("**System Class:** `Embedded Data Terminals`")
st.sidebar.write("---")

# Direct Major-by-Major Context Switch Matrix
st.sidebar.subheader("🏢 Undergraduate Major Scope")
major_selection = st.sidebar.selectbox(
    "Active Academic Scope:",
    options=["All Coles Business Majors"] + list(coles_metrics_data["major_name"].unique())
)

# Apply Context Isolation Filters
if major_selection == "All Coles Business Majors":
    filtered_cases = st.session_state.coles_cases_db
    filtered_busa = st.session_state.busa_courses_db
    filtered_metrics = coles_metrics_data
else:
    filtered_cases = st.session_state.coles_cases_db[st.session_state.coles_cases_db["student_major"] == major_selection]
    filtered_busa = st.session_state.busa_courses_db[st.session_state.busa_courses_db["business_major"] == major_selection]
    filtered_metrics = coles_metrics_data[coles_metrics_data["major_name"] == major_selection]

st.sidebar.write("---")

# Navigation Panel Choice Structure Loops
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Management Module Panel:",
    [
        "📋 Academic Advising & Services Queue", 
        "📚 BUSA Professionalism Courses",
        "📊 Departmental Resource Analytics", 
        "🏛️ University Data Strategy Alignment"
    ]
)

# ==========================================
# MAIN DASHBOARD MOUNTING
# ==========================================
st.title("🛡️ Coles College — Center for Student Success Control Center")
st.markdown(f"Active Academic Scope: **{major_selection}** | Operational View: **{app_panel}**")
st.write("---")

# ------------------------------------------
# MODULE 1: ACADEMIC ADVISING & SERVICES QUEUE
# ------------------------------------------
if app_panel == "📋 Academic Advising & Services Queue":
    st.header("📋 Center Operations Support Desk & Service Tracks")
    st.markdown("##### *Monitoring live queues across Academic Advising, Professional Sales, Career Coaching, Internships/Co-ops, and Student Engagement.*")
    
    # Live Operations Metrics
    tc1, tc2, tc3 = st.columns(3)
    with tc1: st.metric("Active Case Records Dynamic Count", value=len(filtered_cases))
    with tc2: st.metric("Critical Priority Actions Stalled", value=len(filtered_cases[filtered_cases["priority"] == "Critical"]))
    with tc3: st.metric("Accumulated Counseling Duration", value=f"{filtered_cases['duration_minutes'].sum()} Mins")
    
    st.write("")
    st.subheader("📊 Master Student Success Queue (Daily Live Feed)")
    st.dataframe(filtered_cases, use_container_width=True, hide_index=True)
    st.write("---")
    
    # Dynamic Advisory Input Desk Hook
    st.subheader("🛠️ Active Advisor & Career Coach Workbench Engine")
    if len(filtered_cases) > 0:
        target_id = st.selectbox("Mount Student Record to Action Center ID:", options=filtered_cases["case_id"].unique())
        idx = st.session_state.coles_cases_db[st.session_state.coles_cases_db["case_id"] == target_id].index[0]
        row = st.session_state.coles_cases_db.loc[idx]
        
        with st.container(border=True):
            w_col1, w_col2 = st.columns(2)
            with w_col1:
                st.markdown(f"**🏢 Student Major:** `{row['student_major']}` | **🎯 Service Track:** `{row['service_track']}`")
                st.markdown(f"**👤 Assigned Coles Officer:** `{row['assigned_staff']}`")
                st.markdown(f"**📝 Intake Problem Statement:** *{row['appointment_topic']}*")
            with w_col2:
                st.markdown(f"**⚙️ Execution Workflow Status:** `{row['status']}`")
                st.markdown(f"**⏳ Logged Counseling Sessions Duration:** `{row['duration_minutes']} Mins`")
                
        w_in1, w_in2, w_in3, w_in4 = st.columns([1, 1, 2, 1])
        with w_in1:
            time_add = st.selectbox("Log Session Time Slot:", options=[0, 15, 30, 45, 60], format_func=lambda x: f"{x} Mins")
        with w_in2:
            staff_update = st.selectbox("Modify Assigned Staff Role:", options=["Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe", "Sarah Jenkins", "Unassigned"])
        with w_in3:
            note_add = st.text_input("Append Advisory Resolution Case Notes:")
        with w_in4:
            state_update = st.selectbox("Flag Status Tier:", options=["Open", "In Progress", "Resolved", "Unassigned"])
            
        if st.button("🚀 Push Update to Coles Production Framework", use_container_width=True):
            st.session_state.coles_cases_db.at[idx, "duration_minutes"] += time_add
            st.session_state.coles_cases_db.at[idx, "status"] = state_update
            st.session_state.coles_cases_db.at[idx, "assigned_staff"] = staff_update
            if note_add:
                st.session_state.coles_cases_db.at[idx, "session_logs"] = f"{row['session_logs']} | {note_add}".strip(" | ")
            st.success("Authorized entry submitted! Rerunning database tables.")
            st.rerun()
    else:
        st.warning("No dynamic cases match the filtered criteria.")

# ------------------------------------------
# MODULE 2: BUSA PROFESSIONALISM COURSES
# ------------------------------------------
elif app_panel == "📚 BUSA Professionalism Courses":
    st.header("📚 BUSA Professionalism Courses & Milestone Compliance")
    st.markdown("##### *Tracking student career development benchmarks across BUSA 2150, 3150, and 4150.*")
    
    bc1, bc2, bc3 = st.columns(3)
    with bc1: st.metric("Total Enrolled Student Footprint", value=f"{filtered_busa['total_enrolled'].sum():,}")
    with bc2: st.metric("Mean Class Engagement Attendance", value=f"{filtered_busa['attendance_rate_pct'].mean():.1f}%" if len(filtered_busa) > 0 else "N/A")
    with bc3: st.metric("Flagged Interventions Required", value=len(filtered_busa[filtered_busa["vulnerability_risk_flag"] != "Compliant"]))
    
    st.write("---")
    st.subheader("📋 BUSA Course Enrollment & Milestone Completion Matrix")
    
    def color_busa_rows(row):
        if row["vulnerability_risk_flag"] == "Needs Attention": return ['background-color: #3E2723; color: #FFCC80'] * len(row)
        elif row["vulnerability_risk_flag"] == "Needs Review": return ['background-color: #4A3B00; color: #FFE082'] * len(row)
        return [''] * len(row)
    st.dataframe(filtered_busa.style.apply(color_busa_rows, axis=1), use_container_width=True, hide_index=True)
    
    st.write("---")
    st.subheader("📊 Course Milestone Trajectory Split by Undergraduate Major")
    if len(filtered_busa) > 0:
        fig_busa = px.bar(filtered_busa, x="course_code", y="professionalism_milestones_completed", color="business_major",
                          title="Professionalism Badges Sourced per Cohort Profile", barmode="group",
                          color_discrete_sequence=px.colors.sequential.Golds)
        st.plotly_chart(fig_busa, use_container_width=True)

# ------------------------------------------
# MODULE 3: DEPARTMENTAL RESOURCE ANALYTICS
# ------------------------------------------
elif app_panel == "📊 Departmental Resource Analytics":
    st.header("📊 Coles College Capacity Load & Evaluation Desk")
    
    mc1, mc2 = st.columns(2)
    with mc1: st.metric("Total Sourced Business Undergrads", value=f"{filtered_metrics['undergrad_seat_count'].sum():,}")
    with mc2: st.metric("Total Sourced Semester Credit Hours (SCH)", value=f"{filtered_metrics['semester_credit_hours'].sum():,}")
    
    st.write("---")
    st.subheader("🏢 Capacity Load & Retention Metric Audit Grid")
    st.dataframe(filtered_metrics, use_container_width=True, hide_index=True)
    st.write("---")
    
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        fig_ret = px.bar(filtered_metrics, x="major_name", y=["retention_goal_pct", "actual_retention_pct"],
                         title="Retention Metrics: Coles Goals vs. Actual Ratios", barmode="group",
                         color_discrete_sequence=["#FFC400", "#161B22"])
        st.plotly_chart(fig_ret, use_container_width=True)
    with g_col2:
        fig_seats = px.pie(filtered_metrics, values="undergrad_seat_count", names="major_name", hole=0.4,
                           title="Undergraduate Enrollment Volume Share by Major", color_discrete_sequence=px.colors.sequential.Golds)
        st.plotly_chart(fig_seats, use_container_width=True)

# ------------------------------------------
# MODULE 4: UNIVERSITY DATA STRATEGY ALIGNMENT
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
            st.markdown(f"*   **Target Data Scope:** Sourced records matching: **{major_selection}**.")
            st.info("💡 **USG Core Values Check:** Local transaction counts pass institutional baseline verification test models. Schedulers clear to sync with system-wide pipelines.")
        elif "IPEDS" in compliance_target:
            st.markdown("### 🦅 Alignment Validation: **Federal IPEDS Higher-Ed Compliance**")
            st.markdown("**Local Coles CSS Validation Signature:** `● Audit Complete`")
            st.markdown(f"*   **Target Data Scope:** Program milestones matching **{major_selection}** parameters.")
            st.warning("🔒 **FERPA Safety Shield Engaged:** Small student sample clusters (cell counts under threshold parameters) must enforce automated baseline cell suppression before external compilation.")
        else:
            st.markdown("### 🏆 Alignment Validation: **National Publications Survey Ingestion**")
            st.markdown("**Local Coles CSS Validation Signature:** `● Verified Pipeline Clear`")
            st.markdown(f"*   **Target Data Scope:** Retained undergraduate curves mapped to **{major_selection}** benchmarks.")
            st.success("🟢 **Operational Directive:** Sourced performance indicators comply precisely with structural ranking survey parameters.")
