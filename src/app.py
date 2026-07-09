import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles Navigate360 Workspace", layout="wide")

# ==========================================
# EXPANDED SEMESTER-BASED ENROLLMENT DATA STATE
# ==========================================

if "enrollment_funnel_db" not in st.session_state:
    st.session_state.enrollment_funnel_db = pd.DataFrame({
        "applicant_id": [
            "APP-2501", "APP-2502", "APP-2503", "APP-2504", "APP-2505", 
            "APP-2601", "APP-2602", "APP-2603", "APP-2604", "APP-2605", "APP-2606"
        ],
        "prospect_name": [
            "James Wyatt", "Nancy Aguas", "Peggy Aguila", "Marcus Vance", "Elena Rostova",
            "Michael Adam", "Chloe Bennett", "David Kim", "Taylor Brooks", "Maya Patel", "Ryan Gallagher"
        ],
        "intended_major": [
            "Biology", "Accounting", "Cybersecurity", "Entrepreneurship", "Finance",
            "Biology", "Hospitality Management", "Information Systems", "Management", "Marketing", "Marketing"
        ],
        "academic_term": [
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2025", "Fall 2025",
            "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview"
        ],
        "funnel_stage": [
            "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled",
            "Enrolled", "Enrolled", "Admitted", "Applied", "Inquiry", "Inquiry"
        ],
        "outreach_campaign_group": [
            "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield",
            "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Scholarship Push", "Fall Preview Invite", "General Inquiry Track"
        ],
        "predicted_yield_probability": [
            "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled",
            "Enrolled", "Enrolled", "High", "Medium", "Low", "Low"
        ],
        "last_interaction_date": [
            "2025-01-10", "2025-05-15", "2025-08-20", "2025-01-12", "2025-08-22",
            "2026-01-08", "2026-05-12", "2026-07-05", "2026-06-28", "2026-07-02", "2026-07-09"
        ],
        "to_dos_pending": [0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 2],
        "communication_preference": ["Email", "Email", "Text/SMS", "Email", "Email", "Text/SMS", "Text/SMS", "Text/SMS", "Email", "Text/SMS", "Email"],
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
            "Upcoming Cycle: Invited to Coles Open House. Primary interest is Marketing niche.",
            "Upcoming Cycle: Web inquiry form capture. Assigned to general outreach queue."
        ]
    })

# Master Operational Performance Capacity Framework
if "coles_capacity_db" not in st.session_state:
    st.session_state.coles_capacity_db = pd.DataFrame({
        "major_name": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "undergrad_seat_count": [850, 1250, 680, 410, 350, 980, 240, 890, 1650, 1420],
        "semester_credit_hours": [12400, 18400, 9100, 5200, 4800, 24500, 3100, 9400, 19800, 14200],
        "retention_goal_pct": [84.0, 85.0, 88.0, 80.0, 82.0, 82.0, 80.0, 88.0, 80.0, 85.0],
        "actual_retention_pct": [81.2, 82.4, 86.7, 79.1, 81.5, 76.8, 80.2, 89.5, 74.2, 81.1],
        "department_inventory_count": [45, 120, 85, 30, 25, 110, 15, 60, 140, 130]
    })

ksu_gold_palette = ["#FFC400", "#FFA000", "#FF8F00", "#FF6F00", "#FF5722", "#E65100", "#4E5D6C", "#161B22"]

# ==========================================
# NAVIGATION CONTROL INTERFACE SIDEBAR
# ==========================================
st.sidebar.title("💎 Coles Navigate360")
st.sidebar.markdown("**Operational Hub:** `Center for Student Success`")
st.sidebar.write("---")

st.sidebar.subheader("🔍 Funnel Filters")
# NEW: Term Isolation Dropdown Matrix
term_filter = st.sidebar.selectbox(
    "Target Academic Term:", 
    options=["All Active Terms", "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview"]
)
stage_filter = st.sidebar.selectbox("Filter Recruitment Stage:", options=["All Stages", "Inquiry", "Applied", "Admitted", "Enrolled"])

# Processing Multi-Tenant Filtering Logic
processed_funnel = st.session_state.enrollment_funnel_db.copy()
if term_filter != "All Active Terms":
    processed_funnel = processed_funnel[processed_funnel["academic_term"] == term_filter]
if stage_filter != "All Stages":
    processed_funnel = processed_funnel[processed_funnel["funnel_stage"] == stage_filter]

st.sidebar.write("---")
st.sidebar.subheader("🏁 Navigation Terminal")
app_panel = st.sidebar.radio("Select View Desk Mode:", [
    "📋 Enrollment Funnel & Staff Home", 
    "📢 EAB Targeted Campaign Manager", 
    "📈 Reports & Analytics Gateway (All 10 Keys)"
])

# ==========================================
# MODULE 1: ENROLLMENT FUNNEL & STAFF HOME
# ==========================================
if app_panel == "📋 Enrollment Funnel & Staff Home":
    main_workspace, ai_assistant_col = st.columns([3, 1])
    
    with main_workspace:
        st.markdown("## 📋 Staff Home: Funnel Progress & Prospect Management")
        st.write("---")
        
        # Upper KPI Analytical Overview Strip
        fc1, fc2, fc3, fc4 = st.columns(4)
        with fc1: st.metric("Filtered Cohort Records", value=len(processed_funnel))
        with fc2: st.metric("Admitted Student Pipeline", value=len(processed_funnel[processed_funnel["funnel_stage"] == "Admitted"]))
        with fc3: st.metric("Enrolled Conversion Count", value=len(processed_funnel[processed_funnel["funnel_stage"] == "Enrolled"]))
        with fc4: st.metric("Open Reminders/To-Dos", value=int(processed_funnel["to_dos_pending"].sum()))
        
        st.write("")
        if len(processed_funnel) > 0:
            selected_prospect = st.selectbox("🔍 Select Active Student File to Audit:", options=list(processed_funnel["prospect_name"].unique()))
            
            master_match = st.session_state.enrollment_funnel_db[st.session_state.enrollment_funnel_db["prospect_name"] == selected_prospect]
            idx = master_match.index[0]
            p_row = master_match.loc[idx]
            
            with st.container(border=True):
                st.markdown(f"### Applicant Portal: **{p_row['prospect_name']}** | ID: `{p_row['applicant_id']}`")
                st.write("")
                det_col1, det_col2 = st.columns(2)
                with det_col1:
                    st.markdown(f"**📚 Intended Academic Major:** `{p_row['intended_major']}`")
                    st.markdown(f"**🗓️ Academic Term Registration:** `{p_row['academic_term']}`")
                    st.markdown(f"**🎯 Current Funnel Stage:** `{p_row['funnel_stage']}`")
                with det_col2:
                    st.markdown(f"**🔮 Predicted Yield Probability:** `{p_row['predicted_yield_probability']}`")
                    st.markdown(f"**📅 Last Interaction Timestamp:** `{p_row['last_interaction_date']}`")
                    st.markdown(f"**✉️ Outreach Preference Mode:** `{p_row['communication_preference']}`")
            
            st.write("")
            st.subheader("🤖 AI Assistant: Automated Meeting Prep Insights")
            with st.container(border=True):
                st.markdown(f"*🧠 Institutional Digest Material:* **\"{p_row['staff_meeting_prep_notes']}\"**")
                
            st.write("---")
            st.subheader("🛠         Streamline Applicant Progress Queue Tasks")
            w1, w2, w3 = st.columns([1, 1, 2])
            with w1:
                stage_update = st.selectbox("Advance Funnel Stage:", options=["Inquiry", "Applied", "Admitted", "Enrolled"])
            with w2:
                camp_update = st.selectbox("Reassign Outreach Campaign:", options=["Completed Yield", "General Inquiry Track", "Fall Preview Invite", "Scholarship Push", "Housing Deposit Nudge"])
            with w3:
                append_note = st.text_input("Append Diagnostic Communication Log Entry:")
                
            if st.button("🚀 Commit Adjustments to Centralized Funnel View", use_container_width=True):
                st.session_state.enrollment_funnel_db.at[idx, "funnel_stage"] = stage_update
                st.session_state.enrollment_funnel_db.at[idx, "outreach_campaign_group"] = camp_update
                if append_note:
                    st.session_state.enrollment_funnel_db.at[idx, "staff_meeting_prep_notes"] = f"{p_row['staff_meeting_prep_notes']} | Update: {append_note}"
                st.success("Funnel attributes modified successfully.")
                st.rerun()
        else:
            st.warning("No tracking files match filtered conditions.")
            
        st.write("---")
        st.subheader("📋 Centralized View: Filtered Recruitment Pipeline Ledger")
        st.dataframe(processed_funnel[["applicant_id", "prospect_name", "intended_major", "academic_term", "funnel_stage", "predicted_yield_probability"]], use_container_width=True, hide_index=True)

    with ai_assistant_col:
        st.markdown("### 🤖 Staff AI Assistant")
        st.caption("EAB Higher-Ed Engine Connected")
        st.write("---")
        if len(processed_funnel) > 0 and 'p_row' in locals():
            st.markdown("##### 📥 **Digest Insight Cards:**")
            with st.container(border=True):
                st.markdown(f"**Target:** `{p_row['prospect_name']}`")
                st.write(f"* **Term Scope:** {p_row['academic_term']}")
                st.write(f"* **Yield Probability:** {p_row['predicted_yield_probability']}")
                
        st.write("")
        st.markdown("##### ⚙️ **Automated Task Actions:**")
        st.button("✉️ Deploy Automated Nudge Reminder", use_container_width=True)
        st.button("📅 Invite to Connect with Staff/Events", use_container_width=True)
        st.write("---")
        ai_query = st.text_input("💬 Ask AI Agent for Funnel Metrics:")
        if ai_query:
            q_lower = ai_query.lower()
            with st.container(border=True):
                if "preview" in q_lower or "2026" in q_lower:
                    st.info("AI Finder: Flagged 4 student profiles currently pipeline-routed for the Fall 2026 Preview cycle campaign framework.")
                elif "2025" in q_lower:
                    st.success("AI Finder: Sourced 5 historical records completely integrated for the 2025 academic cycles sequence.")
                else:
                    st.success(f"System Check: Active sub-view contains {len(processed_funnel)} records matching baseline criteria.")

# ==========================================
# MODULE 2: EAB TARGETED CAMPAIGN MANAGER
# ==========================================
elif app_panel == "📢 EAB Targeted Campaign Manager":
    st.header("📢 EAB Custom Communications Campaign Manager")
    st.write("---")
    
    st.markdown("#### ⚙️ Configure & Launch Tailored Outreach Campaign")
    with st.form("campaign_creation_desk"):
        c_name = st.text_input("Campaign Name Target Label:", value="Fall 2026 Orientation Completion Nudge")
        c_channel = st.selectbox("Primary Communication Channel Strategy:", options=["Targeted Email Sequences", "Personalized Text/SMS Blasts", "Shared Event Invitation Portals"])
        c_cohort = st.selectbox("Target Audience Filter Group Term:", options=["Fall 2026 Preview Pool", "Historical Active Inquiries Pipeline"])
        
        if st.form_submit_button("🚀 Deploy Nuanced Outreach & Launch Campaign"):
            st.success(f"Outreach track '{c_name}' deployed successfully!")

    st.write("---")
    st.subheader("📊 Historical Longitudinal Pipeline Growth: Term-by-Term Submissions")
    # Group and map counts across standard timelines cleanly
    term_counts = st.session_state.enrollment_funnel_db.groupby("academic_term").size().reset_index(name="total_applicants")
    fig_term = px.bar(term_counts, x="academic_term", y="total_applicants", title="Longitudinal Intake Distribution", color="academic_term", color_discrete_sequence=ksu_gold_palette)
    st.plotly_chart(fig_term, use_container_width=True)

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
        st.info(f"Extracting cohort statistics isolated by current scope context parameters:")
        st.dataframe(processed_funnel[["applicant_id", "prospect_name", "academic_term", "funnel_stage"]], use_container_width=True, hide_index=True)
        
    elif "7. Compiles recurring operational review" in selected_key_tab:
        st.markdown("### 📈 Multi-Semester Longitudinal Trend Analytics Curve (`Key 7`)")
        st.markdown("##### *Reviewing tracking allocations across historical and upcoming enrollment pipelines:*")
        st.dataframe(st.session_state.enrollment_funnel_db.groupby(["academic_term", "funnel_stage"]).size().reset_index(name="student_count"), use_container_width=True, hide_index=True)
        
    else:
        st.info("💡 Select another Key requirement line to evaluate localized data interpretation panels.")
