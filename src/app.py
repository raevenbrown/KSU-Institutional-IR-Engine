import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles CSS Operations Engine", layout="wide")

# ==========================================
# CENTRALIZED EMBEDDED COLES CSS DATA STATE
# ==========================================

# 1. Active Advising Queue (Emulating daily operations for Accounting, Marketing, Finance, Management)
if "advising_db" not in st.session_state:
    st.session_state.advising_db = pd.DataFrame({
        "case_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007],
        "student_major": ["Accounting", "Finance", "Management", "Marketing", "Information Systems", "Finance", "Management"],
        "assigned_advisor": ["Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe", "Michael Gabriele", "Unassigned"],
        "appointment_type": ["Graduation Check", "Transfer Credit Review", "Academic Warning Intervention", "Change of Major Intake", "Internship/Co-op Approval", "Schedule Optimization", "Emergency Drop-In Request"],
        "priority_tier": ["High", "Medium", "Critical", "Low", "Medium", "Low", "High"],
        "case_status": ["Open", "In Progress", "Open", "Resolved", "Open", "In Progress", "Unassigned"],
        "session_duration_mins": [0, 30, 0, 45, 0, 15, 0],
        "action_notes": ["", "Reviewing transfer credits from local state college.", "", "Major officially swapped to Marketing; forms processed.", "", "Adjusted Fall 2026 scheduling constraints.", ""]
    })

# 2. Coles Departmental Load & Faculty-Student Telemetry Matrix
if "coles_metrics_db" not in st.session_state:
    st.session_state.coles_metrics_db = pd.DataFrame({
        "department_name": ["School of Accountancy", "Economics, Finance & EFQA", "Leven School of Management", "Marketing & Professional Sales", "Information Systems & Security"],
        "undergrad_majors_count": [1250, 980, 1650, 1420, 890],
        "full_time_faculty": [28, 42, 35, 18, 22],
        "part_time_instructors": [12, 15, 22, 8, 11],
        "semester_credit_hours": [18400, 24500, 19800, 14200, 9400],
        "retention_goal_pct": [85.0, 82.0, 80.0, 85.0, 88.0],
        "actual_retention_pct": [82.4, 76.8, 74.2, 81.1, 89.5],
        "invoice_clearance": ["Clear", "Clear", "Review Required", "Clear", "Clear"]
    })

# ==========================================
# UNIFIED COLES STUDENT SUCCESS SIDEBAR
# ==========================================
st.sidebar.title("💎 Coles CSS Workbench")
st.sidebar.markdown("**Operational Hub:** `Center for Student Success` ")
st.sidebar.markdown("**Data Strategy Status:** `● Framework Aligned`")
st.sidebar.write("---")

# Target Department Filter Matrix
dept_selection = st.sidebar.selectbox(
    "Active Department Scope:",
    options=["All Coles Business Majors", "Accounting", "Finance", "Management", "Marketing", "Information Systems"]
)

# Apply context isolation based on selection
if dept_selection == "All Coles Business Majors":
    filtered_cases = st.session_state.advising_db
    filtered_metrics = st.session_state.coles_metrics_db
else:
    filtered_cases = st.session_state.advising_db[st.session_state.advising_db["student_major"] == dept_selection]
    # Map raw filter selection to full department naming keys
    dept_map = {
        "Accounting": "School of Accountancy", "Finance": "Economics, Finance & EFQA",
        "Management": "Leven School of Management", "Marketing": "Marketing & Professional Sales",
        "Information Systems": "Information Systems & Security"
    }
    filtered_metrics = st.session_state.coles_metrics_db[st.session_state.coles_metrics_db["department_name"] == dept_map[dept_selection]]

st.sidebar.write("---")

# Navigation Module Layout Selection
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Management Module Panel:",
    [
        "📋 Advising Desk Queue & Operations",
        "📊 Departmental Resource & Faculty Load",
        "🏛️ University Data Strategy Alignment"
    ]
)

# ==========================================
# MAIN WORKSPACE CANVAS INTERFACE
# ==========================================
st.title("🛡️ Coles College — Center for Student Success Operations Engine")
st.markdown(f"Active Department Focus: **{dept_selection}** | Operational View: **{app_panel}**")
st.write("---")

# ------------------------------------------
# MODULE 1: ADVISING DESK QUEUE & OPERATIONS
# ------------------------------------------
if app_panel == "📋 Advising Desk Queue & Operations":
    st.header("📋 Daily Advising Inbound Operations & Case Workbench")
    
    # Live Pipeline Metrics
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Active Case Queue Load", value=len(filtered_cases))
    with c2:
        unassigned_count = len(filtered_cases[filtered_cases["case_status"] == "Unassigned"])
        st.metric("Unassigned Drop-Ins Pending", value=unassigned_count)
    with c3:
        st.metric("Total Advisory Mins Logged", value=int(filtered_cases["session_duration_mins"].sum()))
        
    st.write("")
    st.subheader("📊 Master Student Advising Board (Daily Live Feed)")
    st.dataframe(filtered_cases, use_container_width=True, hide_index=True)
    st.write("---")
    
    # Interactive Advisor Workbench Hook
    st.subheader("🛠️ Active Advisor Workbench Engine")
    if len(filtered_cases) > 0:
        target_id = st.selectbox("Mount Student Case to Action Center ID:", options=filtered_cases["case_id"].unique())
        idx = st.session_state.advising_db[st.session_state.advising_db["case_id"] == target_id].index[0]
        row = st.session_state.advising_db.loc[idx]
        
        with st.container(border=True):
            w_col1, w_col2 = st.columns(2)
            with w_col1:
                st.markdown(f"**🏢 Student Major Niche:** `{row['student_major']}` | **📁 Appointment Type:** `{row['appointment_type']}`")
                st.markdown(f"**👤 Assigned Coles Staff Advisor:** `{row['assigned_advisor']}`")
            with w_col2:
                st.markdown(f"**⚙️ Case State Status:** `{row['case_status']}` | **⏳ Duration Sourced:** `{row['session_duration_mins']} Mins`")
                
        w_in1, w_in2, w_in3, w_in4 = st.columns([1, 1, 2, 1])
        with w_in1:
            time_add = st.selectbox("Log Session Time Slot:", options=[0, 15, 30, 45, 60], format_func=lambda x: f"{x} Mins")
        with w_in2:
            advisor_update = st.selectbox("Reassign Staff Role:", options=["Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe", "Unassigned"])
        with w_in3:
            note_add = st.text_input("Append Advisor Session Resolution Notes:")
        with w_in4:
            state_update = st.selectbox("Flag Status Tier:", options=["Open", "In Progress", "Resolved", "Unassigned"])
            
        if st.button("🚀 Push Update to Coles Production Framework", use_container_width=True):
            st.session_state.advising_db.at[idx, "session_duration_mins"] += time_add
            st.session_state.advising_db.at[idx, "case_status"] = state_update
            st.session_state.advising_db.at[idx, "assigned_advisor"] = advisor_update
            if note_add:
                st.session_state.advising_db.at[idx, "action_notes"] = f"{row['action_notes']} | {note_add}".strip(" | ")
            st.success("Authorized operational modification logged successfully!")
            st.rerun()
    else:
        st.warning("No tracking assets match the filtered focus matrix.")

# ------------------------------------------
# MODULE 2: DEPARTMENTAL RESOURCE & FACULTY LOAD
# ------------------------------------------
elif app_panel == "📊 Departmental Resource & Faculty Load":
    st.header("📊 Educational Infrastructure Load & Evaluation Desk")
    
    # Financial/Resource Analytics Cards
    rc1, rc2, rc3 = st.columns(3)
    with rc1:
        st.metric("Total Coles Business Undergrad Load", value=f"{filtered_metrics['undergrad_majors_count'].sum():,}")
    with rc2:
        st.metric("Aggregated Semester Credit Hours (SCH)", value=f"{filtered_metrics['semester_credit_hours'].sum():,}")
    with rc3:
        review_needed = len(filtered_metrics[filtered_metrics["invoice_clearance"] == "Review Required"])
        st.metric("Departmental Budgets Pending Review", value=review_needed)
        
    st.write("---")
    st.subheader("🏢 Departmental Capacity & Performance Tracking Matrix")
    st.dataframe(filtered_metrics, use_container_width=True, hide_index=True)
    st.write("---")
    
    # Comparative Retention Analytics Graphs
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        fig_retention = px.bar(
            filtered_metrics, x="department_name", y=["retention_goal_pct", "actual_retention_pct"],
            title="Retention Matrix Analysis: Institutional Goals vs. Actual Ratios",
            labels={"value": "Percentage (%)", "department_name": "Coles Academic Unit", "variable": "Retention Class"},
            color_discrete_sequence=["#FFC400", "#161B22"], barmode="group"
        )
        st.plotly_chart(fig_retention, use_container_width=True)
    with g_col2:
        fig_faculty = px.pie(
            filtered_metrics, values="full_time_faculty", names="department_name", hole=0.4,
            title="Full-Time Faculty Core Resource Footprint Allocation",
            color_discrete_sequence=px.colors.sequential.Golds
        )
        st.plotly_chart(fig_faculty, use_container_width=True)

# ------------------------------------------
# MODULE 3: UNIVERSITY DATA STRATEGY ALIGNMENT
# ------------------------------------------
elif app_panel == "🏛️ University Data Strategy Alignment":
    st.header("🏛️ Office of University Data Strategy Integration Framework")
    st.markdown("##### *Aligning local student success metrics with external reporting structures (USG System, Federal IPEDS, and National Publication surveys).*")
    st.write("")
    
    compliance_target = st.selectbox(
        "Select Regulatory Compliance Export Gateway:",
        ["1. University System of Georgia (USG) - Term Census Headcount Packets",
         "2. Federal IPEDS Matrix Gateway - Annual Institutional Completion Matrix",
         "3. National Rankings Survey (U.S. News & World Report Profiling)"]
    )
    
    with st.container(border=True):
        if "USG" in compliance_target:
            st.markdown("### 🏛️ Alignment Validation: **USG Fall Term Census Data**")
            st.markdown("**Local Coles CSS Validation Signature:** `● Authenticated by Assessment Coordinator`")
            st.markdown(f"*   **Target Data Scope:** Finalized credit hours and student counts for **{dept_selection}**.")
            st.info("💡 **USG Core Values Check:** Local data maps pass institutional cross-check baseline validation testing. Ready for automated state-wide data pipeline synchronization.")
            
        elif "IPEDS" in compliance_target:
            st.markdown("### 🦅 Alignment Validation: **Federal IPEDS Higher-Ed Compliance**")
            st.markdown("**Local Coles CSS Validation Signature:** `● Audit Complete`")
            st.markdown(f"*   **Target Data Scope:** Program completion indicators matching **{dept_selection}** parameters.")
            st.warning("🔒 **FERPA Safety Shield Reminder:** Small student sample clusters (cell counts under threshold values) must maintain automated baseline suppression rules before public publishing.")
            
        else:
            st.markdown("### 🏆 Alignment Validation: **National Publications Survey Ingestion**")
            st.markdown("**Local Coles CSS Validation Signature:** `● Verified Pipeline Clear`")
            st.markdown(f"*   **Target Data Scope:** Undergraduate retention shifts mapped to **{dept_selection}** timeline curves.")
            st.success("🟢 **Operational Directive:** Performance indicators comply precisely with structural survey ranking indices.")
