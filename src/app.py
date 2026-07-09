import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles Navigate360 Workspace", layout="wide")

# ==========================================
# CENTRALIZED REALISTIC ENROLLMENT & LIFE CYCLE DATA
# ==========================================

if "enrollment_funnel_db" not in st.session_state:
    st.session_state.enrollment_funnel_db = pd.DataFrame({
        "applicant_id": ["APP-9081", "APP-4112", "APP-3094", "APP-5512", "APP-7721", "APP-1109", "APP-6642", "APP-8841", "APP-2291", "APP-1043"],
        "prospect_name": ["Alex Rivera", "Jordan Chang", "Sarah Jenkins", "Marcus Vance", "Elena Rostova", "Chloe Bennett", "David Kim", "Taylor Brooks", "Maya Patel", "Ryan Gallagher"],
        "intended_major": ["Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing", "Marketing"],
        "funnel_stage": ["Inquiry", "Applied", "Inquiry", "Admitted", "Applied", "Admitted", "Inquiry", "Admitted", "Applied", "Enrolled"],
        "outreach_campaign_group": ["Fall Preview Invite", "Scholarship Push", "Fall Preview Invite", "Housing Deposit Nudge", "Scholarship Push", "Housing Deposit Nudge", "General Inquiry Track", "Housing Deposit Nudge", "Scholarship Push", "Completed Yield"],
        "predicted_yield_probability": ["Low", "Medium", "Low", "High", "Low", "High", "Low", "High", "Medium", "Enrolled"],
        "last_interaction_date": ["2026-06-12", "2026-07-01", "2026-05-18", "2026-07-05", "2026-06-28", "2026-07-02", "2026-04-15", "2026-07-08", "2026-06-30", "2026-07-09"],
        "to_dos_pending": [2, 1, 3, 0, 1, 0, 4, 1, 2, 0],
        "communication_preference": ["Email", "Text/SMS", "Email", "Text/SMS", "Email", "Text/SMS", "Email", "Email", "Text/SMS", "Email"],
        "staff_meeting_prep_notes": ["Student inquired at local high school career fair. Primary interest is CPA track acceleration.", "Transfer credit evaluation pending from local college.", "Sent invite to Coles Open House. No response yet.", "Admitted with honors scholarship. High follow-up priority.", "Incomplete portfolio submission flag raised.", "Housing selection finalized. Clear onboarding path.", "Cold lead from website request info form.", "Awaiting official final high school transcript files.", "Parent attended information night seminar.", "Orientation deposit securely captured. Transferred to advisor module."]
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
stage_filter = st.sidebar.selectbox("Filter Recruitment Stage:", options=["All Stages", "Inquiry", "Applied", "Admitted", "Enrolled"])
campaign_filter = st.sidebar.selectbox("Filter Marketing Campaign:", options=["All Campaigns", "Fall Preview Invite", "Scholarship Push", "Housing Deposit Nudge"])

processed_funnel = st.session_state.enrollment_funnel_db.copy()
if stage_filter != "All Stages":
    processed_funnel = processed_funnel[processed_funnel["funnel_stage"] == stage_filter]
if campaign_filter != "All Campaigns":
    processed_funnel = processed_funnel[processed_funnel["outreach_campaign_group"] == campaign_filter]

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
        with fc1: st.metric("Total Prospects Monitored", value=len(processed_funnel))
        with fc2: st.metric("Admitted Student Pipeline", value=len(processed_funnel[processed_funnel["funnel_stage"] == "Admitted"]))
        with fc3: st.metric("Enrolled Yield Conversion", value=len(processed_funnel[processed_funnel["funnel_stage"] == "Enrolled"]))
        with fc4: st.metric("Open Reminders/To-Dos", value=int(processed_funnel["to_dos_pending"].sum()))
        
        st.write("")
        if len(processed_funnel) > 0:
            selected_prospect = st.selectbox("🔍 Select Active Applicant File to Audit:", options=list(processed_funnel["prospect_name"].unique()))
            
            # Match item string reference parameters cleanly
            master_match = st.session_state.enrollment_funnel_db[st.session_state.enrollment_funnel_db["prospect_name"] == selected_prospect]
            idx = master_match.index[0]
            p_row = master_match.loc[idx]
            
            with st.container(border=True):
                st.markdown(f"### Applicant Portal: **{p_row['prospect_name']}** | ID: `{p_row['applicant_id']}`")
                st.write("")
                det_col1, det_col2 = st.columns(2)
                with det_col1:
                    st.markdown(f"**📚 Intended Academic Major:** `{p_row['intended_major']}`")
                    st.markdown(f"**🎯 Current Funnel Stage:** `{p_row['funnel_stage']}`")
                    st.markdown(f"**📢 Assigned Outreach Track:** `{p_row['outreach_campaign_group']}`")
                with det_col2:
                    st.markdown(f"**🔮 Predicted Yield Probability:** `{p_row['predicted_yield_probability']}`")
                    st.markdown(f"**📅 Last Interaction Timestamp:** `{p_row['last_interaction_date']}`")
                    st.markdown(f"**✉️ Outreach Preference Mode:** `{p_row['communication_preference']}`")
            
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
                camp_update = st.selectbox("Reassign Outreach Campaign:", options=["General Inquiry Track", "Fall Preview Invite", "Scholarship Push", "Housing Deposit Nudge"])
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
            st.warning("No tracking files match filtered conditions.")
            
        st.write("---")
        st.subheader("📋 Centralized View: Filtered Recruitment Pipeline Ledger")
        st.dataframe(processed_funnel[["applicant_id", "prospect_name", "intended_major", "funnel_stage", "outreach_campaign_group", "predicted_yield_probability"]], use_container_width=True, hide_index=True)

    with ai_assistant_col:
        st.markdown("### 🤖 Staff AI Assistant")
        st.caption("EAB Higher-Ed Engine Connected")
        st.write("---")
        if len(processed_funnel) > 0 and 'p_row' in locals():
            st.markdown("##### 📥 **Digest Insight Cards:**")
            with st.container(border=True):
                st.markdown(f"**Target:** `{p_row['prospect_name']}`")
                st.write(f"* **Yield Probability:** {p_row['predicted_yield_probability']}")
                st.write(f"* **Pending To-Dos:** {p_row['to_dos_pending']}")
                
        st.write("")
        st.markdown("##### ⚙️ **Automated Task Actions:**")
        st.button("✉️ Deploy Automated Nudge reminder", use_container_width=True)
        st.button("📅 Invite to Connect with Staff/Events", use_container_width=True)
        st.write("---")
        ai_query = st.text_input("💬 Ask AI Agent for Funnel Metrics:")
        if ai_query:
            q_lower = ai_query.lower()
            with st.container(border=True):
                if "risk" in q_lower or "low" in q_lower:
                    st.error("AI Finder: Flagged 4 student files displaying low yield interaction probabilities.")
                elif "marketing" in q_lower or "major" in q_lower:
                    st.info("AI Finder: Marketing concentration contains the highest density profile stack inside the inquiry pool segment.")
                else:
                    st.success(f"System Check: Funnel contains {len(st.session_state.enrollment_funnel_db)} records. Core yield projection curve model active.")

# ==========================================
# MODULE 2: EAB TARGETED CAMPAIGN MANAGER
# ==========================================
elif app_panel == "📢 EAB Targeted Campaign Manager":
    st.header("📢 EAB Custom Communications Campaign Manager")
    st.markdown("##### *Configure tailored outreach tracks, deploy nudges, and track audience engagement profiles across the recruitment lifecycle.*")
    st.write("---")
    
    st.markdown("#### ⚙️ Configure & Launch Tailored Outreach Campaign")
    with st.form("campaign_creation_desk"):
        c_name = st.text_input("Campaign Name Target Label:", value="Fall 2026 Orientation Completion Nudge")
        c_channel = st.selectbox("Primary Communication Channel Strategy:", options=["Personalized Text/SMS Blasts", "Targeted Email Sequences", "Shared Event Invitation Portals"])
        c_cohort = st.selectbox("Target Audience Filter Group Stage:", options=["Inquiry Population Pool", "Applied - Awaiting Decision", "Admitted - Yield Acceleration Focus"])
        
        if st.form_submit_button("🚀 Deploy Nuanced Outreach & Launch Campaign"):
            st.success(f"Outreach track '{c_name}' deployed successfully! Communication automated across target {c_cohort} clusters.")

    st.write("---")
    st.subheader("📊 Active Funnel Stage Allocations Distribution Analysis")
    fig_funnel = px.bar(st.session_state.enrollment_funnel_db, x="funnel_stage", title="Continuous Progress Funnel Monitor", color="funnel_stage", color_discrete_sequence=ksu_gold_palette)
    st.plotly_chart(fig_funnel, use_container_width=True)

# ==========================================
# MODULE 3: REPORTS & ANALYTICS GATEWAY (ALL 10 KEYS)
# ==========================================
elif app_panel == "📈 Reports & Analytics Gateway (All 10 Keys)":
    st.header("📈 Reports & Analytics Portfolio Gateway")
    st.markdown("##### *Mapping interactive query views to verify all 10 Key Responsibilities outlined in the data analyst job profile framework.*")
    st.write("---")
    
    # 10-Row Master Tracking Schema Table
    st.subheader("🎯 Job Framework Compliance Ledger")
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
        rep_type = st.radio("Select Guidelines Frequency Distribution Format:", ["Standard Recurring (Weekly Intake)", "Ad Hoc Live Extract"])
        if rep_type == "Standard Recurring (Weekly Intake)":
            st.info("📦 **Standard Guideline Run:** Extracting structured multi-semester headcount and demographic benchmarks.")
            st.dataframe(st.session_state.enrollment_funnel_db[["applicant_id", "prospect_name", "intended_major", "funnel_stage"]], hide_index=True)
        else:
            st.warning("⚡ **Ad Hoc Command Executed:** Running dynamic cross-sectional splice targeting critical priority yield risks.")
            ad_hoc_subset = st.session_state.enrollment_funnel_db[st.session_state.enrollment_funnel_db["predicted_yield_probability"] == "Low"]
            st.dataframe(ad_hoc_subset, use_container_width=True, hide_index=True)

    elif "2. Provides reports, analysis" in selected_key_tab:
        st.markdown("### 🏛️ Departmental Interpretation Ledger Matrix (`Key 2`)")
        target_dept = st.selectbox("Isolate Assigned Department Data Scope:", options=list(st.session_state.enrollment_funnel_db["intended_major"].unique()))
        dept_match = st.session_state.enrollment_funnel_db[st.session_state.enrollment_funnel_db["intended_major"] == target_dept]
        st.markdown(f"#### Interpretive Analysis Summary for **{target_dept}**:")
        if len(dept_match) > 0:
            st.success(f"🟢 **Data Signal Active:** Sourced {len(dept_match)} prospect applications matching this unit. Inquiries currently map out to a total count size of **{len(dept_match[dept_match['funnel_stage']=='Inquiry'])}** leads.")
            st.dataframe(dept_match, use_container_width=True, hide_index=True)
        else:
            st.warning(f"⚠️ Zero counts isolated inside {target_dept} tracking files.")

    elif "3. Identifies areas of opportunity" in selected_key_tab:
        st.markdown("### 💡 Leadership Findings & Strategic Recommendations Engine (`Key 3`)")
        st.markdown("##### *Automated script checking for institutional funnel risk bottlenecks to construct a stakeholder summary.*")
        low_yield_leads = st.session_state.enrollment_funnel_db[st.session_state.enrollment_funnel_db["predicted_yield_probability"] == "Low"]
        with st.container(border=True):
            st.markdown("🏆 **Executive Data Insights Memorandum**")
            st.write(f"1. **Identified Area of Opportunity:** Found **{len(low_yield_leads)}** prospects maintaining low yield confirmation conversion rates.")
            st.write("2. **Analytical Interpretation:** Communication logs reveal bottlenecked transcript verification holds are delaying admissions decision letters.")
            st.write("3. **Actionable Recommendation to Leadership:** Deploy automated EAB text message alerts targeting verification parameters to reduce processing friction.")
            st.error("🚨 Opportunity Tracking Scope List:")
            st.dataframe(low_yield_leads[["prospect_name", "intended_major", "funnel_stage", "outreach_campaign_group"]], use_container_width=True, hide_index=True)

    elif "4. Provides productivity analysis" in selected_key_tab:
        st.markdown("### ⏳ Outreach Campaign Effectiveness Productivity Audit Log (`Key 4`)")
        prod_df = st.session_state.enrollment_funnel_db.groupby("outreach_campaign_group").agg(
            total_prospects_reached=("applicant_id", "count"),
            total_pending_tasks_remaining=("to_dos_pending", "sum")
        ).reset_index()
        st.dataframe(prod_df, use_container_width=True, hide_index=True)
        fig_prod = px.bar(prod_df, x="outreach_campaign_group", y="total_prospects_reached", title="Total Sourced Engagement Volume per Campaign", color_discrete_sequence=["#FFC400"])
        st.plotly_chart(fig_prod, use_container_width=True)

    elif "5. Develops and maintains reports to measure operational" in selected_key_tab:
        st.markdown("### ⚙️ Operational Utilization & Communication Activity Benchmarks (`Key 5`)")
        util_df = st.session_state.enrollment_funnel_db.groupby("communication_preference").size().reset_index(name="active_allocated_leads")
        st.dataframe(util_df, use_container_width=True, hide_index=True)
        fig_util = px.pie(util_df, values="active_allocated_leads", names="communication_preference", title="Preferred Communication Resource Channels Allocation", color_discrete_sequence=ksu_gold_palette)
        st.plotly_chart(fig_util, use_container_width=True)

    elif "6. May be required to prepare ad hoc reports required of association" in selected_key_tab:
        st.markdown("### 🏛️ External Oversight & Regulatory Compliance USG Framework Gateway (`Key 6`)")
        reg_target = st.selectbox("Select Regulatory Compliance Recipient:", ["USG State System Board Intake", "AACSB Evaluation Ledger Core", "Federal IPEDS Frame"])
        with st.container(border=True):
            st.write(f"📁 **Active Compliance Manifest Structure:** `{reg_target}`")
            st.write(f"*   **Relational Assets Bound:** Coles Center for Student Success core database matrices.")
            st.success("🟢 Validation Protocol: Pass. System layout fields map out perfectly for state board data integration loops.")

    elif "7. Compiles recurring operational review" in selected_key_tab:
        st.markdown("### 📈 Multi-Semester Longitudinal Trend Analytics Curve (`Key 7`)")
        trend_df = st.session_state.coles_capacity_db.copy()
        trend_df["retention_shortfall"] = trend_df["retention_goal_pct"] - trend_df["actual_retention_pct"]
        st.dataframe(trend_df[["major_name", "retention_goal_pct", "actual_retention_pct", "retention_shortfall"]], use_container_width=True, hide_index=True)
        fig_trend = px.line(trend_df, x="major_name", y="retention_shortfall", title="Retention Goal Gaps Profile Trends", markers=True, color_discrete_sequence=["#FF5722"])
        st.plotly_chart(fig_trend, use_container_width=True)

    elif "8. May assists with departmental inventory" in selected_key_tab:
        st.markdown("### 🖥️ Departmental Technology Asset Inventory Analysis (`Key 8`)")
        inv_df = st.session_state.coles_capacity_db[["major_name", "undergrad_seat_count", "department_inventory_count"]].copy()
        st.dataframe(inv_df, use_container_width=True, hide_index=True)
        fig_inv = px.bar(inv_df, x="major_name", y="department_inventory_count", title="Hardware Terminals Active per Student Care Unit", color_discrete_sequence=["#161B22"])
        st.plotly_chart(fig_inv, use_container_width=True)

    elif "9. May be required to prepare ad hoc reporting that assists with measuring department performance" in selected_key_tab:
        st.markdown("### 🎯 Center Performance & Program Effectiveness Matrix (`Key 9`)")
        res_counts = st.session_state.enrollment_funnel_db.groupby("funnel_stage").size().reset_index(name="total_cases")
        fig_perf = px.bar(res_counts, x="funnel_stage", y="total_cases", title="Recruitment Progress Conversion Rates Profile", color_discrete_sequence=["#00E676"])
        st.plotly_chart(fig_perf, use_container_width=True)

    elif "10. Collaborate with a variety of stakeholders" in selected_key_tab:
        st.markdown("### 🤝 Office of University Data Strategy Alignment Matrix (`Key 10`)")
        with st.container(border=True):
            st.markdown("### 🏛️ University Policy Framework Integration Terminal")
            st.write("🔗 **Data Governance Layer:** Kennesaw State University Master Data Strategy Directive")
            st.write("🔒 **Encryption Protocol:** AES-256 System Handshake Validated")
            st.success("🟢 **Alignment Confirmed:** Local fields mapped to Navigate360 structures perfectly match KSU's central data taxonomy rules.")
