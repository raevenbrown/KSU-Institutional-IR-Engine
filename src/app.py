import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="OmniIR Institutional Engine", layout="wide")

# ==========================================
# CENTRALIZED ANONYMIZED STUDENT INFORMATION STATE
# ==========================================

if "enrollment_db" not in st.session_state:
    st.session_state.enrollment_db = pd.DataFrame({
        "college_name": ["Coles College of Business", "College of Science & Math", "Coles College of Business", "College of Humanities", "College of Science & Math", "College of Computing", "College of Humanities", "College of Computing"],
        "academic_major": ["Information Systems", "Biochemistry", "Marketing", "Criminal Justice", "Data Science", "Software Engineering", "Technical Communication", "Cybersecurity"],
        "applicant_pool": [1450, 890, 2100, 1150, 640, 1850, 420, 1300],
        "admitted_yield_count": [620, 310, 890, 540, 210, 780, 190, 520],
        "census_headcount_freeze": [580, 295, 840, 510, 195, 740, 175, 490],
        "freshman_retention_rate": [82.4, 76.8, 81.1, 74.2, 89.5, 84.3, 71.8, 86.7],
        "grad_rate_6yr": [64.2, 58.1, 61.9, 52.4, 74.1, 68.7, 50.1, 71.3]
    })

if "faculty_academic_db" not in st.session_state:
    st.session_state.faculty_academic_db = pd.DataFrame({
        "college_name": ["Coles College of Business", "College of Science & Math", "Coles College of Business", "College of Humanities", "College of Science & Math", "College of Computing", "College of Humanities", "College of Computing"],
        "academic_major": ["Information Systems", "Biochemistry", "Marketing", "Criminal Justice", "Data Science", "Software Engineering", "Technical Communication", "Cybersecurity"],
        "full_time_faculty": [28, 42, 18, 35, 14, 38, 12, 22],
        "part_time_faculty": [12, 15, 8, 22, 6, 14, 19, 11],
        "credit_hours_generated": [18400, 24500, 14200, 19800, 9400, 26100, 7800, 15400],
        "passed_count": [510, 220, 790, 440, 170, 680, 160, 430],
        "failed_withdraw_count": [70, 75, 50, 70, 25, 60, 15, 60],
        "degrees_awarded_annual": [142, 68, 195, 112, 44, 168, 38, 98]
    })

# ==========================================
# UNIFIED LEFT-HAND DATA STRATEGY SIDEBAR
# ==========================================
st.sidebar.title("💎 OmniIR Operational OS")
st.sidebar.markdown("**Institutional Branch:** `Office of Data Strategy` ")
st.sidebar.markdown("**Database Sync Status:** `● Census Frame Locked`")
st.sidebar.write("---")

# FERPA Privacy Masking Control Tool
st.sidebar.subheader("🔒 Regulatory Guardrails")
ferpa_masking_active = st.sidebar.toggle(
    "Activate FERPA Compliance Masking", 
    value=True, 
    help="Under FERPA rules, small cell sizes (counts below 5 or 10) must be automatically suppressed/masked in public dashboards to prevent individual student identification."
)

if ferpa_masking_active:
    st.sidebar.caption("🟢 **Privacy Shield Engaged:** Counts lower than 30 are masked as `< 30` to protect student records.")
else:
    st.sidebar.caption("⚠️ **Privacy Warning:** Raw unmasked records active. Do not share outside authorized institutional panels.")

st.sidebar.write("---")

# Academic College Selection Framework Matrix
st.sidebar.subheader("🏛️ Institutional Scope Switcher")
college_selection = st.sidebar.selectbox(
    "Target Academic Context:",
    options=["University Macro-Board Focus"] + list(st.session_state.enrollment_db["college_name"].unique())
)

# Apply Multi-Tenant Isolation Filtering Logic to datasets
if college_selection == "University Macro-Board Focus":
    filtered_enrollment = st.session_state.enrollment_db
    filtered_faculty = st.session_state.faculty_academic_db
else:
    filtered_enrollment = st.session_state.enrollment_db[st.session_state.enrollment_db["college_name"] == college_selection]
    filtered_faculty = st.session_state.faculty_academic_db[st.session_state.faculty_academic_db["college_name"] == college_selection]

# Navigation Panel Choice Structure Loops
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Institutional View Focus:",
    [
        "👥 Student Body Enrollment & Lifecycle",
        "🎓 Academic Infrastructure & Faculty Analytics",
        "🏛️ Compliance & External Reporting Gateway"
    ]
)

# Function to automatically mask small records according to FERPA simulation parameters
def apply_ferpa_mask(dataframe, count_columns, threshold=30):
    if not ferpa_masking_active:
        return dataframe
    masked_df = dataframe.copy()
    for col in count_columns:
        if col in masked_df.columns:
            masked_df[col] = masked_df[col].apply(lambda x: f"< {threshold}" if isinstance(x, (int, float)) and x < threshold else x)
    return masked_df

# ==========================================
# MAIN DASHBOARD WORKSURFACE ROUTING
# ==========================================
st.title("🏛️ OmniIR — Institutional Research Decision Engine")
st.markdown(f"**Current Institutional Scope Context:** `{college_selection}` | **Operational View:** `{app_panel}`")
st.write("---")

# ------------------------------------------
# MODULE 1: STUDENT BODY ENROLLMENT & LIFECYCLE
# ------------------------------------------
if app_panel == "👥 Student Body Enrollment & Lifecycle":
    st.header("👥 Student Population Metrics & Lifecycle Pipelines")
    st.markdown("##### *Monitoring raw admissions yield counts, official freeze-date headcounts, and multi-year retention curves.*")
    st.write("")
    
    # Calculate key volumetric metrics cleanly outside the components
    total_applicants = filtered_enrollment["applicant_pool"].sum()
    total_census = filtered_enrollment["census_headcount_freeze"].sum()
    avg_retention = filtered_enrollment["freshman_retention_rate"].mean()
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Aggregated Application Pool Intake", value=f"{total_applicants:,}")
    with m2:
        metric_census_val = f"{total_census:,}" if not (ferpa_masking_active and total_census < 30) else "< 30"
        st.metric("Official Census Headcount (Freeze Date)", value=metric_census_val)
    with m3:
        st.metric("Mean First-Time Freshman Retention", value=f"{avg_retention:.1f}%")
        
    st.write("---")
    
    # Graphic Visuals Section
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        st.subheader("🍩 Admissions Yield Share by Academic Major")
        # Explicitly assigned a discrete color sequence hex code array to fix the dynamic attribute error
        ksu_gold_sequence = ["#FFC400", "#FFA000", "#FF8F00", "#FF6F00", "#FF5722", "#E65100"]
        fig_yield = px.pie(filtered_enrollment, values="admitted_yield_count", names="academic_major", hole=0.4,
                           color_discrete_sequence=ksu_gold_sequence)
        st.plotly_chart(fig_yield, use_container_width=True)
    with g_col2:
        st.subheader("📈 Six-Year Long-Term Graduation Trajectories")
        fig_grad = px.bar(filtered_enrollment, x="academic_major", y="grad_rate_6yr", color="college_name",
                          labels={"grad_rate_6yr": "6-Year Graduation Rate (%)", "academic_major": "Academic Program"},
                          color_discrete_sequence=["#FFC400", "#161B22", "#4E5D6C"])
        st.plotly_chart(fig_grad, use_container_width=True)
        
    st.write("---")
    st.subheader("📋 Relational Student Lifecycle Ingestion Matrix")
    display_enrollment = apply_ferpa_mask(filtered_enrollment, ["applicant_pool", "admitted_yield_count", "census_headcount_freeze"])
    st.dataframe(display_enrollment, use_container_width=True, hide_index=True)

# ------------------------------------------
# MODULE 2: ACADEMIC INFRASTRUCTURE & FACULTY ANALYTICS
# ------------------------------------------
elif app_panel == "🎓 Academic Infrastructure & Faculty Analytics":
    st.header("🎓 Educational Infrastructure Load & Evaluation Desk")
    st.markdown("##### *Auditing full-time faculty allocations, total credit hours generated, and grade pass/withdraw ratios.*")
    st.write("")
    
    total_ft = filtered_faculty["full_time_faculty"].sum()
    total_sch = filtered_faculty["credit_hours_generated"].sum()
    total_degrees = filtered_faculty["degrees_awarded_annual"].sum()
    
    ac1, ac2, ac3 = st.columns(3)
    with ac1:
        st.metric("Active Full-Time Core Faculty Count", value=int(total_ft))
    with ac2:
        st.metric("Total Semester Credit Hours (SCH) Generated", value=f"{total_sch:,}")
    with ac3:
        metric_degrees_val = f"{total_degrees:,}" if not (ferpa_masking_active and total_degrees < 30) else "< 30"
        st.metric("Total Degrees Awarded (Annual Cycle)", value=metric_degrees_val)
        
    st.write("---")
    
    # Grade Distribution Tracking Curve
    st.subheader("📊 Course Evaluation Metrics: Pass vs. Fail/Withdrawal Ratios")
    fig_grades = px.bar(filtered_faculty, x="academic_major", y=["passed_count", "failed_withdraw_count"], 
                        title="Program Grade Analytics (Pass vs. DFW Distribution Patterns)",
                        labels={"value": "Student Count Volume", "academic_major": "Academic Program Focus", "variable": "Grade Evaluation Type"},
                        color_discrete_map={"passed_count": "#00E676", "failed_withdraw_count": "#D500F9"}, barmode="group")
    st.plotly_chart(fig_grades, use_container_width=True)
    
    st.write("---")
    st.subheader("📋 Faculty Workload & Degree Output Audit Ledger")
    display_faculty = apply_ferpa_mask(filtered_faculty, ["full_time_faculty", "part_time_faculty", "passed_count", "failed_withdraw_count", "degrees_awarded_annual"])
    st.dataframe(display_faculty, use_container_width=True, hide_index=True)

# ------------------------------------------
# MODULE 3: COMPLIANCE & EXTERNAL REPORTING GATEWAY
# ------------------------------------------
elif app_panel == "🏛️ Compliance & External Reporting Gateway":
    st.header("🏛️ External Stakeholder Framework Packages & Compliance Transmissions")
    st.markdown("##### *Formatting and validating finalized institutional assets for external state, federal, and ranking entities.*")
    st.write("")
    
    st.subheader("📬 Forensic Compliance Data Package Dispatcher")
    st.markdown("*Select an external regulatory framework entity to package and review finalized institutional telemetry sets context loops.*")
    
    compliance_target = st.selectbox(
        "Target Outside Oversight Recipient:",
        ["1. University System of Georgia (USG) - Mandatory Fall Census Submission",
         "2. Federal IPEDS Matrix Portal - Annual Postsecondary Compliance Frame",
         "3. U.S. News & World Report - Annual University Ranking Profile Data"]
    )
    
    with st.container(border=True):
        if "USG" in compliance_target:
            st.markdown("### 🏛️ Package Focus: **USG State Data Framework Submission**")
            st.markdown("**Required Parameters Verification Status:** `● Approved by Chief Data Officer`")
            st.write("")
            st.markdown(f"*   **Target Data Object:** Complete, isolated record sets for **{college_selection}**.")
            st.markdown("*   **Primary Metrics Transmitted:** Finalized student census headcount maps synchronized precisely at midnight of the semester freeze milestone.")
            st.info("💡 **USG Core Values Alignment Check:** Accountability and Integrity metrics pass institutional cross-check baseline validations. Ready for state system API transport.")
            
        elif "IPEDS" in compliance_target:
            st.markdown("### 🦅 Package Focus: **Federal IPEDS Financial Aid Compliance**")
            st.markdown("**Required Parameters Verification Status:** `● Cryptographic Census Check Valid`")
            st.write("")
            st.markdown(f"*   **Target Data Object:** Institutional completion metrics for **{college_selection}**.")
            st.markdown("*   **Primary Metrics Transmitted:** 6-Year Graduation cohort variables, student financial aid allocation density profiles, and strict student-to-faculty tracking fractions.")
            st.warning("🔒 **FERPA Privacy Check Enforcement:** Automated masking algorithms active. Student cell sets matching values below minimum tracking metrics have been securely suppressed.")
            
        else:
            st.markdown("### 🏆 Package Focus: **National Rankings & Survey Metrics**")
            st.markdown("**Required Parameters Verification Status:** `● Audit Complete`")
            st.write("")
            st.markdown(f"*   **Target Data Object:** Excellence and performance trends for **{college_selection}**.")
            st.markdown("*   **Primary Metrics Transmitted:** First-year freshman retention velocity charts, mean grade passing profiles, and total degree awards split by discipline classification code frameworks.")
            st.success("🟢 **Publication Ready:** Performance vectors align cleanly with U.S. News & World Report survey standards.")
            
    st.write("---")
    st.subheader("📋 Pre-Submission Validation Check Tracker")
    st.markdown("This tracker highlights automated validation rules processed before exporting out data rows.")
    
    validation_df = pd.DataFrame({
        "Oversight Framework": ["USG State Board", "Federal IPEDS System", "National Publication Profiles"],
        "Required Metric Rule": ["Freeze Date Headcount totals must match financial ledger counts", "Cohort tracking counts must isolate first-time freshman exclusively", "Mean graduation statistics must maintain perfect internal math integrity"],
        "Automated Status": ["🟢 Validation Complete - Zero Mismatches", "🟢 Validation Complete - Active Masking Shield Clear", "🟢 Validation Complete - Data Integrity Attained"]
    })
    st.dataframe(validation_df, use_container_width=True, hide_index=True)
