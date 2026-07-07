import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles Navigate360 Terminal", layout="wide")

# ==========================================
# EAB NAVIGATE CORE DATA SCHEMA COMPLIANCE
# ==========================================

# Persistent Session State 1: Central Navigate360 Student Caseload & Activity Feed
if "navigate_caseload_db" not in st.session_state:
    st.session_state.navigate_caseload_db = pd.DataFrame({
        "case_id": [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
        "student_record": ["Student Alpha", "Student Beta", "Student Gamma", "Student Delta", "Student Epsilon", "Student Zeta", "Student Eta", "Student Theta", "Student Iota", "Student Kappa"],
        "student_major": ["Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems & Information Security", "Management", "Marketing", "Marketing"],
        "appointment_care_unit": ["Academic Advising", "Academic Advising", "Career Coaching", "Internship & Co-op Advising", "Academic Advising", "Student Engagement", "Academic Advising", "Career Coaching", "Academic Advising", "Professional Sales Track"],
        "assigned_staff_owner": ["Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe", "Sarah Jenkins", "Stacey Nebriaga", "Tyler Pede", "Michael Gabriele", "Thomas Anderson"],
        "reason_category": [
            "Graduation Check & Degree Auditing",
            "MFA Token Issue & Registration Authorization",
            "Resume Polish & Executive Mock Interview",
            "Corporate Internship Credit Sign-off",
            "Schedule Optimization & Prerequisite Check",
            "Business Student Association Leadership Intake",
            "Upper-Division Security Course Override Request",
            "Fall Career Fair Strategic Prep Session",
            "Change of Major Intake: Swapping to Marketing",
            "National Collegiate Sales Competition Prep & Vetting"
        ],
        "predicted_support_level": ["High Risk", "Medium Risk", "High Risk", "Critical Risk", "Low Risk", "Low Risk", "Critical Risk", "High Risk", "Medium Risk", "High Risk"],
        "case_status": ["Open", "In Progress", "Open", "Open", "Resolved", "Open", "In Progress", "Open", "Resolved", "In Progress"],
        "touchpoint_duration_mins": [0, 15, 0, 0, 45, 0, 30, 0, 30, 15],
        "appointment_summary_report": ["", "Reviewing transfer credits from state college.", "", "", "Cleared registration holds and prerequisites.", "", "Processing system registration override permission codes.", "", "Change of major paperwork securely archived.", ""]
    })

# Persistent Session State 2: Progress Report Campaigns (Navigate's Midterm/Early Alert Engine)
if "progress_reports_db" not in st.session_state:
    st.session_state.progress_reports_db = pd.DataFrame({
        "campaign_course": ["BUSA 2150", "BUSA 3150", "BUSA 4150", "BUSA 2150", "BUSA 3150"],
        "business_major": ["Accounting", "Finance", "Management", "Marketing", "Cybersecurity"],
        "students_targeted": [340, 290, 410, 380, 195],
        "faculty_response_rate_pct": [94.2, 88.5, 91.1, 86.4, 92.7],
        "positive_case_outcomes": [315, 240, 395, 310, 180],
        "intervention_alert_status": ["Compliant", "Needs Review", "Compliant", "Needs Attention", "Compliant"]
    })

# Master Coles Capacity & Outcome Metrics
coles_capacity_data = pd.DataFrame({
    "major_name": ["Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems & Information Security", "Management", "Marketing", "Professional Sales"],
    "undergrad_seat_count": [1250, 680, 410, 350, 980, 240, 890, 1650, 1420, 310],
    "semester_credit_hours": [18400, 9100, 5200, 4800, 24500, 3100, 9400, 19800, 14200, 3900],
    "retention_goal_pct": [85.0, 88.0, 80.0, 82.0, 82.0, 80.0, 88.0, 80.0, 85.0, 85.0],
    "actual_retention_pct": [82.4, 86.7, 79.1, 81.5, 76.8, 80.2, 89.5, 74.2, 81.1, 84.8]
})

# ==========================================
# SIDEBAR CONTROL PANEL
# ==========================================
st.sidebar.title("💎 Coles Navigate360 Terminal")
st.sidebar.markdown("**Operational Hub:** `Center for Student Success` ")
st.sidebar.markdown("**System Class:** `Navigate V3 Data Engine`")
st.sidebar.write("---")

# Direct Major-by-Major Context Switch Matrix
st.sidebar.subheader("🏢 Caseload Scope Filter")
major_selection = st.sidebar.selectbox(
    "Select Student Cohort Focus:",
    options=["All Coles Business Majors"] + list(coles_capacity_data["major_name"].unique())
)

# Apply Context Isolation Filters
if major_selection == "All Coles Business Majors":
    filtered_cases = st.session_state.navigate_caseload_db
    filtered_progress = st.session_state.progress_reports_db
    filtered_metrics = coles_capacity_data
else:
    filtered_cases = st.session_state.navigate_caseload_db[st.session_state.navigate_caseload_db["student_major"] == major_selection]
    filtered_progress = st.session_state.progress_reports_db[st.session_state.progress_reports_db["business_major"] == major_selection]
    filtered_metrics = coles_capacity_data[coles_capacity_data["major_name"] == major_selection]

st.sidebar.write("---")

# Navigation Panel Choice Structure Loops
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Dashboard View:",
    [
        "📋 Staff Home: Caseload & Activity Feed", 
        "📢 Progress Report Campaigns",
        "📊 Population Health & Capacity Metrics", 
        "🏛️ University Data Strategy Alignment"
    ]
)

# ==========================================
# MAIN DASHBOARD MOUNTING
# ==========================================
st.title("🏛️ Coles College — Navigate360 Student Success Workspace")
st.markdown(f"Active Filtering Cohort: **{major_selection}** | Workspace Module: **{app_panel}**")
st.write("---")

# ------------------------------------------
# MODULE 1: STAFF HOME: CASELOAD & ACTIVITY FEED
# ------------------------------------------
if app_panel == "📋 Staff Home: Caseload & Activity Feed":
    st.header("📋 Staff Home: Real-Time Caseload Activity Feed")
    st.markdown("##### *Monitoring live queues across Academic Advising Care Units, Career Coaching, and Appointment Summary Reports.*")
    
    # Process Process Metrics
    tc1, tc2, tc3 = st.columns(3)
    with tc1: st.metric("Total Assigned Caseload Count", value=len(filtered_cases))
    with tc2: st.metric("Critical Support Levels Flagged", value=len(filtered_cases[filtered_cases["predicted_support_level"] == "Critical Risk"]))
    with tc3: st.metric("Accumulated Touchpoint Duration", value=f"{filtered_cases['touchpoint_duration_mins'].sum()} Mins")
    
    st.write("")
    st.subheader("📊 Live Activity Feed (V3 Reporting Format)")
    st.dataframe(filtered_cases, use_container_width=True, hide_index=True)
    st.write("---")
    
    # Dynamic Advisor Input Desk Hook
    st.subheader("🛠️ Navigate360 Case Management Engine")
    if len(filtered_cases) > 0:
        target_id = st.selectbox("Mount Student Record to Case Management Center ID:", options=filtered_cases["case_id"].unique())
        idx = st.session_state.navigate_caseload_db[st.session_state.navigate_caseload_db["case_id"] == target_id].index[0]
        row = st.session_state.navigate_caseload_db.loc[idx]
        
        with st.container(border=True):
            w_col1, w_col2 = st.columns(2)
            with w_col1:
                st.markdown(f"**🏢 Student Major:** `{row['student_major']}` | **🎯 Appointment Care Unit:** `{row['appointment_care_unit']}`")
                st.markdown(f"**👤 Owner (User List):** `{row['assigned_staff_owner']}`")
                st.markdown(f"**📝 Care Reason Category:** *{row['reason_category']}*")
            with w_col2:
                st.markdown(f"**📈 Predicted Support Level:** `{row['predicted_support_level']}`")
                st.markdown(f"**⚙️ Current Case Status:** `{row['case_status']}` | **⏳ Touchpoint Duration:** `{row['touchpoint_duration_mins']} Mins`")
                
        w_in1, w_in2, w_in3, w_in4 = st.columns([1, 1, 2, 1])
        with w_in1:
            time_add = st.selectbox("Log Touchpoint Duration:", options=[0, 15, 30, 45, 60], format_func=lambda x: f"{x} Mins")
        with w_in2:
            staff_update = st.selectbox("Modify Case Owner:", options=["Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe", "Sarah Jenkins", "Unassigned"])
        with w_in3:
            note_add = st.text_input("Append Appointment Summary Report Entry:")
        with w_in4:
            state_update = st.selectbox("Update Case Status Field:", options=["Open", "In Progress", "Resolved"])
            
        if st.button("🚀 Commit Changes to Navigate360 Database Pipeline", use_container_width=True):
            st.session_state.navigate_caseload_db.at[idx, "touchpoint_duration_mins"] += time_add
            st.session_state.navigate_caseload_db.at[idx, "case_status"] = state_update
            st.session_state.navigate_caseload_db.at[idx, "assigned_staff_owner"] = staff_update
            if note_add:
                st.session_state.navigate_caseload_db.at[idx, "appointment_summary_report"] = f"{row['appointment_summary_report']} | {note_add}".strip(" | ")
            st.success("Authorized modification saved to Navigate core schema database tables.")
            st.rerun()
    else:
        st.warning("No dynamic caseload targets match the filtered focus matrix.")

# ------------------------------------------
# MODULE 2: PROGRESS REPORT CAMPAIGNS
# ------------------------------------------
elif app_panel == "📢 Progress Report Campaigns":
    st.header("📢 Early Alert & Progress Report Campaigns")
    st.markdown("##### *Tracking faculty engagement, midterm risk alerts, and positive case outcomes across BUSA core blocks.*")
    
    bc1, bc2, bc3 = st.columns(3)
    with bc1: st.metric("Total Campaign Targeted Population", value=f"{filtered_progress['students_targeted'].sum():,}")
    with bc2: st.metric("Mean Faculty Response Rate", value=f"{filtered_progress['faculty_response_rate_pct'].mean():.1f}%" if len(filtered_progress) > 0 else "N/A")
    with bc3: st.metric("Total Positive Case Outcomes", value=f"{filtered_progress['positive_case_outcomes'].sum():,}")
    
    st.write("---")
    st.subheader("📋 Progress Report Campaigns Tracking Grid")
    
    def color_progress_rows(row):
        if row["intervention_alert_status"] == "Needs Attention": return ['background-color: #3E2723; color: #FFCC80'] * len(row)
        elif row["intervention_alert_status"] == "Needs Review": return ['background-color: #4A3B00; color: #FFE082'] * len(row)
        return [''] * len(row)
    st.dataframe(filtered_progress.style.apply(color_progress_rows, axis=1), use_container_width=True, hide_index=True)
    
    st.write("---")
    st.subheader("📊 Successful Positive Outcomes Sliced by Cohort Major")
    if len(filtered_progress) > 0:
        fig_prog = px.bar(filtered_progress, x="campaign_course", y="positive_case_outcomes", color="business_major",
                          title="Intervention Milestone Resolution Rates", barmode="group",
                          color_discrete_sequence=px.colors.sequential.Golds)
        st.plotly_chart(fig_prog, use_container_width=True)

# ------------------------------------------
# MODULE 3: POPULATION HEALTH & CAPACITY METRICS
# ------------------------------------------
elif app_panel == "📊 Population Health & Capacity Metrics":
    st.header("📊 Population Health Dashboard & Capacity Metrics")
    st.markdown("##### *Auditing institutional outcome metrics: undergraduate enrollment caps vs. multi-semester retention goals.*")
    
    mc1, mc2 = st.columns(2)
    with mc1: st.metric("Undergraduate Enrollment Size Focus", value=f"{filtered_metrics['undergrad_seat_count'].sum():,}")
    with mc2: st.metric("Total Semester Credit Hours (SCH) Sourced", value=f"{filtered_metrics['semester_credit_hours'].sum():,}")
    
    st.write("---")
    st.subheader("🏢 Capacity Load & Retention Metric Audit Grid")
    st.dataframe(filtered_metrics, use_container_width=True, hide_index=True)
    st.write("---")
    
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        fig_ret = px.bar(filtered_metrics, x="major_name", y=["retention_goal_pct", "actual_retention_pct"],
                         title="Retention Matrix: Ultimate Goals vs. Actual Process Outcome Rates", barmode="group",
                         color_discrete_sequence=["#FFC400", "#161B22"])
        st.plotly_chart(fig_ret, use_container_width=True)
    with g_col2:
        fig_seats = px.pie(filtered_metrics, values="undergrad_seat_count", names="major_name", hole=0.4,
                           title="Enrollment Metric Distribution Shares", color_discrete_sequence=px.colors.sequential.Golds)
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
            st.markdown("### 🏆 Alignment Validation: **National Rankings Survey Ingestion**")
            st.markdown("**Local Coles CSS Validation Signature:** `● Verified Pipeline Clear`")
            st.markdown(f"*   **Target Data Scope:** Retained undergraduate curves mapped to **{major_selection}** benchmarks.")
            st.success("🟢 **Operational Directive:** Sourced performance indicators comply precisely with structural ranking survey parameters.")
