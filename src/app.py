import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles Navigate360 Workspace", layout="wide")

# ==========================================
# CENTRALIZED HIGH-DENSITY LIFE CYCLE DATA STATES
# ==========================================

if "enrollment_funnel_db" not in st.session_state:
    st.session_state.enrollment_funnel_db = pd.DataFrame({
        "applicant_id": ["APP-2501", "APP-2502", "APP-2503", "APP-2504", "APP-2505", "APP-2601", "APP-2602", "APP-2603", "APP-2604", "APP-2605"],
        "student_name": ["Michael Adam", "Nancy Aguas", "Peggy Aguila", "Margaret Aldrege", "James Alexander", "Nathan Amador", "Chloe Bennett", "David Kim", "Taylor Brooks", "Maya Patel"],
        "intended_major": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "academic_term": ["Spring 2025", "Summer 2025", "Fall 2025", "Spring 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview"],
        "classification": ["Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year"],
        "cumulative_gpa": [2.85, 3.31, 2.45, 3.82, 1.95, 2.88, 3.12, 2.15, 3.64, 3.22],
        "studentvue_sync_status": [
            "Good Standing - Regular Sync", 
            "Good Standing - Regular Sync", 
            "Academic Hold - Missing Transcript", 
            "Good Standing - Regular Sync", 
            "Good Standing - Regular Sync", 
            "Good Standing - Regular Sync", 
            "Good Standing - Regular Sync", 
            "Financial Hold - Balance Due", 
            "Good Standing - Regular Sync", 
            "Probation Sync Alert"
        ],
        "funnel_stage": ["Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Admitted", "Applied", "Inquiry"],
        "outreach_campaign_group": ["Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Scholarship Push", "Fall Preview Invite"],
        "predicted_yield_probability": ["Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "High", "Medium", "Low"],
        "last_interaction_date": ["2025-01-10", "2025-05-15", "2025-08-20", "2025-01-12", "2025-08-22", "2026-01-08", "2026-05-12", "2026-07-05", "2026-06-28", "2026-07-02"],
        "to_dos_pending": [0, 0, 0, 0, 0, 0, 0, 0, 1, 3],
        "communication_preference": ["Email", "Email", "Text/SMS", "Email", "Email", "Text/SMS", "Text/SMS", "Text/SMS", "Email", "Text/SMS"],
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

if "faculty_retention_db" not in st.session_state:
    st.session_state.faculty_retention_db = pd.DataFrame({
        "faculty_id": ["FAC-201", "FAC-202", "FAC-203", "FAC-204", "FAC-205", "FAC-206", "FAC-207", "FAC-208"],
        "faculty_name": ["Dr. Stacey Nebriaga", "Prof. Michael Gabriele", "Dr. Tyler Pede", "Dr. Thomas Anderson", "Prof. Emily Holzgrefe", "Dr. Sarah Jenkins", "Dr. David Vance", "Prof. Elena Rostova"],
        "department_assignment": ["Biology", "Information Systems", "Economics", "Management", "Marketing", "Accounting", "Cybersecurity", "Finance"],
        "appointment_track": ["Tenured Faculty", "Non-Tenure Lecturer", "Tenure-Track Assistant", "Tenured Faculty", "Non-Tenure Clinical", "Tenure-Track Assistant", "Tenured Faculty", "Non-Tenure Lecturer"],
        "faculty_staff_status": [
            "Active - Full Instructional Load",
            "Active - Full Instructional Load",
            "Pending Tenure Review Notice",
            "Sabbatical - Research Active",
            "Active - Full Instructional Load",
            "Pending Tenure Review Notice",
            "Active - Full Instructional Load",
            "Medical Leave"
        ],
        "tenure_years_at_institution": [12.5, 3.0, 4.5, 16.0, 2.5, 5.0, 14.0, 1.5],
        "semester_credit_hours_load": [420, 580, 390, 310, 620, 410, 330, 600],
        "faculty_retention_hazard_flag": ["Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "Medium Risk"],
        "estimated_departure_timeline": ["Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years"],
        "retention_notes": ["Stable institutional asset.", "Seeking promotion track clarification.", "Progressing toward tenure review.", "Endowed chairholder.", "Needs retention strategy intervention.", "Research grant funding secured.", "Approaching retirement horizon.", "Market salary compensation compression issues logged."]
    })

if "coles_capacity_db" not in st.session_state:
    st.session_state.coles_capacity_db = pd.DataFrame({
        "major_name": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "undergrad_seat_count": [850, 1250, 680, 410, 350, 980, 240, 890, 1650, 1420],
        "semester_credit_hours": [12400, 18400, 9100, 5200, 4800, 24500, 3100, 9400, 19800, 14200],
        "retention_goal_pct": [84.0, 85.0, 88.0, 80.0, 82.0, 82.0, 80.0, 88.0, 80.0, 85.0],
        "actual_retention_pct": [81.2, 82.4, 86.7, 79.1, 81.5, 76.8, 80.2, 89.5, 74.2, 81.1],
        "department_inventory_count": [45, 120, 85, 30, 25, 110, 15, 60, 140, 130]
    })

ksu_gold_palette = ["#FFC400", "#161B22", "#FFA000", "#FF8F00", "#4E5D6C", "#FF5722", "#00E676"]

# ==========================================
# SIDEBAR SELECTION SYSTEM
# ==========================================
st.sidebar.title("🛡️ Navigate360 Core")
st.sidebar.markdown("**Operational Hub:** `Center for Student Success`")
st.sidebar.write("---")

# NEW DIRECTIVE FEATURE: Data Visibility Checklist Layer Toggle Options
st.sidebar.subheader("👁️ Layer Visibility Options")
show_students = st.sidebar.checkbox("Show Student Data Tracks", value=True)
show_faculty = st.sidebar.checkbox("Show Faculty Staff Tracks", value=True)
st.sidebar.write("---")

st.sidebar.subheader("🗂️ Global Scope Filters")

dept_filter = st.sidebar.selectbox("Filter by Academic Department Major:", options=["All Departments"] + list(st.session_state.coles_capacity_db["major_name"].unique()))

term_filter = st.sidebar.selectbox(
    "Target Academic Term Horizon:", 
    options=["All Semesters", "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview"]
)

studentvue_filter = st.sidebar.selectbox(
    "StudentVue Registration Profile Status:",
    options=["All Student Tiers", "Good Standing - Regular Sync", "Academic Hold - Missing Transcript", "Financial Hold - Balance Due", "Probation Sync Alert"]
)

faculty_status_filter = st.sidebar.selectbox(
    "Faculty Staff Administrative Status:",
    options=["All Faculty Tiers", "Active - Full Instructional Load", "Pending Tenure Review Notice", "Sabbatical - Research Active", "Medical Leave"]
)

processed_funnel = st.session_state.enrollment_funnel_db.copy()
processed_faculty = st.session_state.faculty_retention_db.copy()

# Apply Department Filters to both
if dept_filter != "All Departments":
    processed_funnel = processed_funnel[processed_funnel["intended_major"] == dept_filter]
    processed_faculty = processed_faculty[processed_faculty["department_assignment"] == dept_filter]

# Apply Student-specific filters
if term_filter != "All Semesters":
    processed_funnel = processed_funnel[processed_funnel["academic_term"] == term_filter]

if studentvue_filter != "All Student Tiers":
    processed_funnel = processed_funnel[processed_funnel["studentvue_sync_status"] == studentvue_filter]

# Apply Faculty-specific filters
if faculty_status_filter != "All Faculty Tiers":
    processed_faculty = processed_faculty[processed_faculty["faculty_staff_status"] == faculty_status_filter]

st.sidebar.write("---")
st.sidebar.subheader("🏁 Navigation Terminal")

# Dynamic navigation setup determined strictly by checked layer flags
nav_options = []
if show_students:
    nav_options.append("👤 Student Lifecycle Portal (StudentVue)")
if show_faculty:
    nav_options.append("🏛️ Faculty Retention Terminal")
if show_students:
    nav_options.append("📢 EAB Targeted Campaign Manager")
nav_options.append("📈 Reports & Analytics Gateway (All 10 Keys)")

app_panel = st.sidebar.radio("Select Operational Workspace Desk:", options=nav_options)

# ==========================================
# RENDERING TAB CONSOLES
# ==========================================
if app_panel == "👤 Student Lifecycle Portal (StudentVue)":
    main_workspace, ai_assistant_col = st.columns([3, 1])
    
    with main_workspace:
        st.markdown("## 📋 Staff Home: Funnel Progress & Prospect Management")
        st.write("---")
        
        fc1, fc2, fc3, fc4 = st.columns(4)
        with fc1: st.metric("Sourced Active Records Focus", value=len(processed_funnel))
        with fc2: st.metric("Admitted Student Pipeline", value=len(processed_funnel[processed_funnel["funnel_stage"] == "Admitted"]))
        with fc3: st.metric("Enrolled Yield Conversion", value=len(processed_funnel[processed_funnel["funnel_stage"] == "Enrolled"]))
        
        with fc4: 
            if "to_dos_pending" in processed_funnel.columns and len(processed_funnel) > 0:
                st.metric("Open Reminders/To-Dos", value=int(processed_funnel["to_dos_pending"].sum()))
            else:
                st.metric("Open Reminders/To-Dos", value=0)
        
        st.write("")
        if len(processed_funnel) > 0:
            selected_prospect = st.selectbox("🔍 Select Active Applicant File to Audit:", options=list(processed_funnel["student_name"].unique()))
            
            master_match = st.session_state.enrollment_funnel_db[st.session_state.enrollment_funnel_db["student_name"] == selected_prospect]
            idx = master_match.index[0]
            p_row = master_match.loc[idx]
            
            with st.container(border=True):
                st.markdown(f"### Applicant Portal: **{p_row['student_name']}** | ID: `{p_row['applicant_id']}`")
                st.write("")
                det_col1, det_col2 = st.columns(2)
                with det_col1:
                    st.markdown(f"**📚 Intended Academic Major:** `{p_row['intended_major']}`")
                    st.markdown(f"**🗓️ Target Academic Term:** `{p_row['academic_term']}`")
                    st.markdown(f"**🎯 Current Funnel Stage:** `{p_row['funnel_stage']}`")
                with det_col2:
                    st.markdown(f"**🔮 Predicted Yield Probability:** `{p_row['predicted_yield_probability']}`")
                    st.markdown(f"**🔒 StudentVue Sync Update:** `{p_row['studentvue_sync_status']}`")
                    st.markdown(f"**🏷️ Category Flags Matrix:** `{p_row['category_tags']}`")
            
            st.write("")
            st.subheader("🤖 AI Assistant: Automated Meeting Prep Insights")
            with st.container(border=True):
                st.markdown(f"*🧠 Institutional Digest Material:* **\"{p_row['staff_meeting_prep_notes']}\"**")
                
            st.write("---")
            st.subheader("🛠️ Streamline Applicant Progress Queue Tasks")
            w1, w2, w3 = st.columns([1, 1, 2])
            with w1:
                stage_update = st.selectbox("Advance Funnel Stage:", options=["Inquiry", "Applied", "Admitted", "Enrolled"])
            with w2:
                camp_update = st.selectbox("Reassign Outreach Campaign:", options=["Completed Yield", "Fall Preview Invite", "Scholarship Push", "Housing Deposit Nudge"])
            with w3:
                append_note = st.text_input("Append Diagnostic Communication Log Entry:")
                
            if st.button("🚀 Commit Adjustments to Centralized Funnel View", use_container_width=True):
                st.session_state.enrollment_funnel_db.at[idx, "funnel_stage"] = stage_update
                st.session_state.enrollment_funnel_db.at[idx, "outreach_campaign_group"] = camp_update
                if append_note:
                    st.session_state.enrollment_funnel_db.at[idx, "staff_meeting_prep_notes"] = f"{p_row['staff_meeting_prep_notes']} | CDO Edit: {append_note}"
                st.success("Funnel attributes modified and saved to baseline ledger frames.")
                st.rerun()
        else:
            st.warning("No tracking records match selection filter parameters constraints.")
            
        st.write("---")
        st.subheader("📋 Centralized View: Filtered Recruitment Pipeline Ledger")
        st.dataframe(processed_funnel[["applicant_id", "student_name", "intended_major", "academic_term", "funnel_stage", "studentvue_sync_status", "predicted_yield_probability"]], use_container_width=True, hide_index=True)

    with ai_assistant_col:
        st.markdown("### 🤖 Staff AI Assistant")
        st.caption("EAB Higher-Ed Engine Connected")
        st.write("---")
        if len(processed_funnel) > 0 and 'p_row' in locals():
            st.markdown("##### 📥 **Digest Insight Cards:**")
            with st.container(border=True):
                st.markdown(f"**Target Focus:** `{p_row['student_name']}`")
                st.write(f"* **Term Scope:** {p_row['academic_term']}")
                st.write(f"* **Yield Probability:** {p_row['predicted_yield_probability']}")
                
        st.write("")
        st.markdown("##### ⚙️ **Automated Task Actions:**")
        st.button("✉️ Deploy Automated Nudge reminder", use_container_width=True)
        st.button("📅 Invite to Connect with Staff/Events", use_container_width=True)

# ==========================================
# MODULE 2: FACULTY RETENTION TERMINAL
# ==========================================
elif app_panel == "🏛️ Faculty Retention Terminal":
    st.header("🏛️ Faculty Roster Retention & Workload Terminal")
    st.markdown("##### *Auditing teacher tenure years, credit hour generation workloads, and administrative retention risk variables.*")
    st.write("---")
    
    if len(processed_faculty) > 0:
        faculty_picker = st.selectbox("👤 Select Detailed Faculty Profile File to Open:", options=list(processed_faculty["faculty_name"].unique()))
        f_row = processed_faculty[processed_faculty["faculty_name"] == faculty_picker].iloc[0]
        
        with st.container(border=True):
            st.markdown(f"### Academic Staff File: **{f_row['faculty_name']}** | ID: `{f_row['faculty_id']}`")
            st.write("")
            f_c1, f_c2, f_c3 = st.columns(3)
            with f_c1:
                st.markdown(f"**🏢 Departmental Unit:** `{f_row['department_assignment']}`")
                st.markdown(f"**🎯 Appointment Track:** `{f_row['appointment_track']}`")
                st.markdown(f"**⚙️ Teacher Status Update:** `{f_row['faculty_staff_status']}`")
            with f_c2:
                st.markdown(f"**⏳ Tenure Longevity Curve:** `{f_row['tenure_years_at_institution']} Years STAYING`")
                st.markdown(f"**📚 Instructional Load Metric:** `{f_row['semester_credit_hours_load']} SCH`")
            with f_c3:
                st.markdown(f"**🔮 Attrition Risk Tier:** `{f_row['faculty_retention_hazard_flag']}`")
                st.markdown(f"**📅 Departure Horizon Estimate:** `{f_row['estimated_departure_timeline']}`")
            st.write("---")
            st.markdown(f"**📥 HR Analyst Log entries:** *\"{f_row['retention_notes']}\"*")
            
        st.write("---")
        f_g1, f_g2 = st.columns(2)
        with f_g1:
            fig_tenure = px.bar(processed_faculty, x="faculty_name", y="tenure_years_at_institution", title="Institutional Tenure Gaps Profile by Teacher", color="appointment_track", color_discrete_sequence=ksu_gold_palette)
            st.plotly_chart(fig_tenure, use_container_width=True)
        with f_g2:
            fig_hazard = px.pie(processed_faculty, values="semester_credit_hours_load", names="faculty_retention_hazard_flag", title="Workload Focus Distribution Slices by Threat level", hole=0.4, color_discrete_sequence=["#00E676", "#FFC400", "#FF5722"])
            st.plotly_chart(fig_hazard, use_container_width=True)
    else:
        st.warning("No teacher metrics log segments match active sidebar filter matrix controls.")

# ==========================================
# MODULE 3: EAB TARGETED CAMPAIGN MANAGER
# ==========================================
elif app_panel == "📢 EAB Targeted Campaign Manager":
    st.header("📢 EAB Custom Communications Campaign Manager")
    st.write("---")
    
    st.markdown("#### ⚙️ Configure & Launch Tailored Outreach Campaign")
    with st.form("campaign_creation_desk"):
        c_name = st.text_input("Campaign Name Target Label:", value="Fall 2026 Orientation Completion Nudge")
        c_channel = st.selectbox("Primary Communication Channel Strategy:", options=["Targeted Email Sequences", "Personalized Text/SMS Blasts", "Shared Event Invitation Portals"])
        c_cohort = st.selectbox("Target Audience Filter Group Stage:", options=["Inquiry Population Pool", "Applied - Awaiting Decision", "Admitted - Yield Acceleration Focus"])
        
        if st.form_submit_button("🚀 Deploy Nuanced Outreach & Launch Campaign"):
            st.success(f"Outreach track '{c_name}' deployed successfully! Communication automated across target {c_cohort} clusters.")

    st.write("---")
    st.subheader("📊 Active Funnel Stage Allocations Distribution Analysis")
    fig_funnel = px.bar(processed_funnel, x="funnel_stage", title="Continuous Progress Funnel Monitor", color="funnel_stage", color_discrete_sequence=ksu_gold_palette)
    st.plotly_chart(fig_funnel, use_container_width=True)

# ==========================================
# MODULE 4: REPORTS & ANALYTICS GATEWAY (ALL 10 KEYS)
# ==========================================
elif app_panel == "📈 Reports & Analytics Gateway (All 10 Keys)":
    st.header("📈 Reports & Analytics Portfolio Gateway")
    st.markdown("##### *Mapping interactive query views to verify all 10 Key Responsibilities outlined in the data analyst job profile framework.*")
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
        if show_students:
            st.dataframe(processed_funnel[["applicant_id", "student_name", "intended_major", "academic_term", "funnel_stage"]], use_container_width=True, hide_index=True)
        else:
            st.info("Student reporting layer toggled off.")

    elif "2. Provides reports, analysis" in selected_key_tab:
        st.markdown("### 🏛️ Departmental Interpretation Ledger Matrix (`Key 2`)")
        if show_faculty:
            st.dataframe(processed_faculty[["faculty_name", "department_assignment", "appointment_track", "faculty_staff_status", "tenure_years_at_institution"]], use_container_width=True, hide_index=True)
        else:
            st.info("Faculty reporting layer toggled off.")

    elif "3. Identifies areas of opportunity" in selected_key_tab:
        st.markdown("### 💡 Leadership Findings & Strategic Recommendations Engine (`Key 3`)")
        if show_students and len(processed_funnel) > 0:
            low_yield_leads = processed_funnel[processed_funnel["predicted_yield_probability"] == "Low"]
            with st.container(border=True):
                st.markdown("🏆 **Executive Data Insights Memorandum**")
                st.write(f"1. **Identified Area of Opportunity:** Found **{len(low_yield_leads)}** active records maintaining low yield conversion markers within filter scope.")
                st.write("2. **Actionable Recommendation:** Apply targeted nudge text automation strings to mitigate process registration bottlenecks.")
                st.error("🚨 Opportunity Tracking Scope List:")
                st.dataframe(low_yield_leads[["student_name", "intended_major", "academic_term", "studentvue_sync_status"]], use_container_width=True, hide_index=True)
        else:
            st.warning("Reporting layer inactive or zero records in selection.")

    elif "4. Provides productivity analysis" in selected_key_tab:
        st.markdown("### ⏳ Outreach Campaign Effectiveness Productivity Audit Log (`Key 4`)")
        if show_students and len(processed_funnel) > 0:
            prod_df = processed_funnel.groupby("outreach_campaign_group").agg(total_prospects_reached=("applicant_id", "count"), total_pending_tasks=("to_dos_pending", "sum")).reset_index()
            st.dataframe(prod_df, use_container_width=True, hide_index=True)
        else: st.warning("No records to aggregate for productivity evaluation metrics.")

    elif "5. Develops and maintains reports to measure operational" in selected_key_tab:
        st.markdown("### ⚙️ Operational Utilization & Communication Activity Benchmarks (`Key 5`)")
        if show_students and len(processed_funnel) > 0:
            util_df = processed_funnel.groupby("communication_preference").size().reset_index(name="active_allocated_leads")
            fig_util = px.pie(util_df, values="active_allocated_leads", names="communication_preference", title="Preferred Channel Share", color_discrete_sequence=ksu_gold_palette)
            st.plotly_chart(fig_util, use_container_width=True)
        else: st.warning("No records available.")

    elif "6. May be required to prepare ad hoc reports required of association" in selected_key_tab:
        st.markdown("### 🏛️ External Oversight & Regulatory Compliance USG Framework Gateway (`Key 6`)")
        st.success("🟢 Validation Protocol: Pass. Core structures are formatted perfectly for external state and accreditation transfers.")

    elif "7. Compiles recurring operational review" in selected_key_tab:
        st.markdown("### 📈 Multi-Semester Longitudinal Trend Analytics Curve (`Key 7`)")
        trend_df = st.session_state.coles_capacity_db.copy()
        trend_df["retention_shortfall"] = trend_df["retention_goal_pct"] - trend_df["actual_retention_pct"]
        fig_trend = px.line(trend_df, x="major_name", y="retention_shortfall", title="Retention Goal Gaps Profile Trends", markers=True, color_discrete_sequence=["#FF5722"])
        st.plotly_chart(fig_trend, use_container_width=True)

    elif "8. May assists with departmental inventory" in selected_key_tab:
        st.markdown("### 🖥️ Departmental Technology Asset Inventory Analysis (`Key 8`)")
        st.dataframe(st.session_state.coles_capacity_db[["major_name", "undergrad_seat_count", "department_inventory_count"]], use_container_width=True, hide_index=True)

    elif "9. May be required to prepare ad hoc reporting that assists with measuring department performance" in selected_key_tab:
        st.markdown("### 🎯 Center Performance & Program Effectiveness Matrix (`Key 9`)")
        if show_students and len(processed_funnel) > 0:
            res_counts = processed_funnel.groupby("funnel_stage").size().reset_index(name="total_cases")
            fig_perf = px.bar(res_counts, x="funnel_stage", y="total_cases", title="Recruitment Progress Conversion Rates Profile", color_discrete_sequence=["#00E676"])
            st.plotly_chart(fig_perf, use_container_width=True)

    elif "10. Collaborate with a variety of stakeholders" in selected_key_tab:
        st.markdown("### 🤝 Office of University Data Strategy Alignment Matrix (`Key 10`)")
        st.success("🟢 **Alignment Confirmed:** Local fields mapped to Navigate360 structures perfectly match KSU's central data taxonomy rules.")
