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
        "applicant_id": [f"APP-{2600+i}" for i in range(1, 41)],
        "student_name": [
            "Michael Adam", "Nancy Aguas", "Peggy Aguila", "Margaret Aldrege", "James Alexander", 
            "Nathan Amador", "Chloe Bennett", "David Kim", "Taylor Brooks", "Maya Patel",
            "Alex Rivera", "Jordan Chang", "Sarah Jenkins", "Marcus Vance", "Elena Rostova", 
            "Ryan Gallagher", "Christian Diaz", "Olivia Martinez", "Ethan Wright", "Sophia Lopez",
            "Liam Gallagher", "Emma Watson", "Noah Centineo", "Ava DuVernay", "Oliver Stone", 
            "Isabella Rossellini", "Lucas Hedges", "Mia Farrow", "Benjamin Bratt", "Charlotte Gainsbourg",
            "Amos Diggory", "Cedric Diggory", "Fleur Delacour", "Viktor Krum", "Luna Lovegood", 
            "Neville Longbottom", "Ginny Weasley", "Fred Weasley", "George Weasley", "Percy Weasley"
        ],
        "intended_major": [
            "Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", 
            "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing",
            "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", 
            "Marketing", "Biology", "Accounting", "Cybersecurity", "Finance",
            "Management", "Marketing", "Information Systems", "Economics", "Biology",
            "Hospitality Management", "Accounting", "Finance", "Cybersecurity", "Management",
            "Entrepreneurship", "Marketing", "Hospitality Management", "Information Systems", "Biology",
            "Economics", "Accounting", "Finance", "Cybersecurity", "Management"
        ],
        "academic_term": [
            "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Spring 2026", "Fall 2026 Preview", 
            "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview",
            "Spring 2026", "Fall 2026 Preview", "Spring 2026", "Fall 2026 Preview", "Spring 2026",
            "Summer 2026", "Fall 2026 Preview", "Spring 2026", "Fall 2026 Preview", "Spring 2026",
            "Summer 2026", "Fall 2026 Preview", "Spring 2026", "Fall 2026 Preview", "Spring 2026",
            "Summer 2026", "Fall 2026 Preview", "Spring 2026", "Fall 2026 Preview", "Spring 2026",
            "Summer 2026", "Fall 2026 Preview", "Spring 2026", "Fall 2026 Preview", "Fall 2026 Preview",
            "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Spring 2026", "Summer 2026"
        ],
        "classification": ["Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year"] * 4,
        "cumulative_gpa": [0.00 for _ in range(40)], 
        "studentvue_sync_status": ["Good Standing - Regular Sync", "Good Standing - Regular Sync", "Academic Hold - Missing Transcript", "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Financial Hold - Balance Due", "Good Standing - Regular Sync", "Probation Sync Alert"] * 4,
        "funnel_stage": ["Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Admitted", "Applied", "Inquiry"] * 4,
        "outreach_campaign_group": ["Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Scholarship Push", "Fall Preview Invite"] * 4,
        "predicted_yield_probability": ["Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "High", "Medium", "Low"] * 4,
        "last_interaction_date": ["2026-03-10" for _ in range(40)],
        "to_dos_pending": [i % 4 for i in range(40)],
        "communication_preference": ["Email" if i % 2 == 0 else "Text/SMS" for i in range(40)],
        "category_tags": ["First Generation, Pell-Eligible" if i % 3 == 0 else "Good Academic Standing" for i in range(40)],
        "staff_meeting_prep_notes": [f"Sourced cohort record update tracking slot sequence flag {i}." for i in range(1, 41)]
    })

if "faculty_retention_db" not in st.session_state:
    st.session_state.faculty_retention_db = pd.DataFrame({
        "faculty_id": [f"FAC-{200+i}" for i in range(1, 21)],
        "faculty_name": ["Dr. Stacey Nebriaga", "Prof. Michael Gabriele", "Dr. Tyler Pede", "Dr. Thomas Anderson", "Prof. Emily Holzgrefe", "Dr. Sarah Jenkins", "Dr. David Vance", "Prof. Elena Rostova", "Dr. Robert Langdon", "Prof. Minerva McGonagall", "Dr. Alan Grant", "Dr. Ellie Sattler", "Prof. Charles Xavier", "Dr. Henry Wu", "Dr. Ian Malcolm", "Prof. Albus Dumbledore", "Dr. Severus Snape", "Prof. Gilderoy Lockhart", "Dr. Remus Lupin", "Dr. Pomona Sprout"],
        "department_assignment": ["Biology", "Information Systems", "Economics", "Management", "Marketing", "Accounting", "Cybersecurity", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing", "Hospitality Management", "Entrepreneurship", "Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance"],
        "appointment_track": ["Tenured Faculty", "Non-Tenure Lecturer", "Tenure-Track Assistant", "Tenured Faculty", "Non-Tenure Clinical", "Tenure-Track Assistant", "Tenured Faculty", "Non-Tenure Lecturer", "Tenured Faculty", "Tenured Faculty", "Tenure-Track Assistant", "Tenured Faculty", "Tenured Faculty", "Non-Tenure Lecturer", "Non-Tenure Clinical", "Tenured Faculty", "Tenured Faculty", "Non-Tenure Lecturer", "Tenure-Track Assistant", "Tenured Faculty"],
        "faculty_staff_status": ["Active - Full Instructional Load", "Active - Full Instructional Load", "Pending Tenure Review Notice", "Sabbatical - Research Active", "Active - Full Instructional Load", "Pending Tenure Review Notice", "Active - Full Instructional Load", "Medical Leave", "Active - Full Instructional Load", "Active - Full Instructional Load", "Pending Tenure Review Notice", "Active - Full Instructional Load", "Sabbatical - Research Active", "Active - Full Operations Load", "Active - Full Instructional Load", "Active - Full Instructional Load", "Active - Full Instructional Load", "Medical Leave", "Pending Tenure Review Notice", "Active - Full Instructional Load"],
        "tenure_years_at_institution": [12.5, 3.0, 4.5, 16.0, 2.5, 5.0, 14.0, 1.5, 8.0, 22.0, 3.5, 11.0, 19.5, 4.0, 1.0, 35.0, 15.0, 2.0, 5.5, 13.0],
        "semester_credit_hours_load": [420, 580, 390, 310, 620, 410, 330, 600, 450, 300, 510, 400, 280, 590, 610, 200, 350, 550, 430, 380],
        "faculty_retention_hazard_flag": ["Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "Medium Risk", "Low Risk", "Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "High Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk"],
        "estimated_departure_timeline": ["Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)"],
        "retention_notes": ["Stable institutional asset profiles verified.", "Seeking timeline promotion track clarification.", "Progressing toward standard tenure review.", "Endowed academic chairholder active.", "Needs structural retention strategy intervention.", "Research grant funding targets secured.", "Approaching standard retirement matrix horizon.", "Market salary compression issues logged.", "Stable institutional asset profiles verified.", "Seeking timeline promotion track clarification.", "Progressing toward standard tenure review.", "Endowed academic chairholder active.", "Needs structural retention strategy intervention.", "Research grant funding targets secured.", "Approaching standard retirement matrix horizon.", "Market salary compensation logs updated.", "Stable institutional asset profiles verified.", "Seeking timeline promotion track clarification.", "Progressing toward standard tenure review.", "Endowed academic chairholder active."]
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

ksu_gold_palette = ["#FFC400", "#00E676", "#FF5722", "#00B0FF", "#AA00FF", "#FF3D00", "#E0E0E0"]

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("Coles Navigate360")
processed_funnel = st.session_state.enrollment_funnel_db.copy()
processed_faculty = st.session_state.faculty_retention_db.copy()

dept_filter = st.sidebar.selectbox("Filter by Department:", ["All Departments"] + list(st.session_state.coles_capacity_db["major_name"].unique()))
if dept_filter != "All Departments":
    processed_funnel = processed_funnel[processed_funnel["intended_major"] == dept_filter]
    processed_faculty = processed_faculty[processed_faculty["department_assignment"] == dept_filter]

nav_options = ["Student Lifecycle Portal (StudentVue)", "Faculty Retention Terminal", "EAB Targeted Campaign Manager", "Reports and Analytics Gateway (All 10 Keys)"]
app_panel = st.sidebar.radio("Select Operational Workspace Desk:", options=nav_options)

# ==========================================
# MODULES
# ==========================================
if app_panel == "Student Lifecycle Portal (StudentVue)":
    st.markdown("## Staff Home: Funnel Progress")
    if len(processed_funnel) > 0:
        selected_prospect = st.selectbox("Select Student Record:", options=list(processed_funnel["student_name"].unique()))
        p_row = processed_funnel[processed_funnel["student_name"] == selected_prospect].iloc[0]
        st.write(f"**Classification:** {p_row['classification']} | **Major:** {p_row['intended_major']}")
    st.table(processed_funnel)

elif app_panel == "Faculty Retention Terminal":
    st.header("Faculty Retention Terminal")
    col1, col2 = st.columns(2)
    with col1:
        dept_fac_filter = st.selectbox("Filter by Department:", ["All Departments"] + list(processed_faculty["department_assignment"].unique()))
    with col2:
        sort_choice = st.selectbox("Sort Faculty By:", ["Name (A-Z)", "Tenure Years (High to Low)"])

    display_df = processed_faculty.copy()
    if dept_fac_filter != "All Departments":
        display_df = display_df[display_df["department_assignment"] == dept_fac_filter]
    
    if sort_choice == "Tenure Years (High to Low)":
        display_df = display_df.sort_values(by="tenure_years_at_institution", ascending=False)
    else:
        display_df = display_df.sort_values(by="faculty_name")
        
    st.table(display_df)
    st.plotly_chart(px.bar(display_df, x="faculty_name", y="tenure_years_at_institution", color="appointment_track"))

elif app_panel == "EAB Targeted Campaign Manager":
    st.header("EAB Targeted Campaign Manager")
    st.write("Campaign management controls active.")
    st.plotly_chart(px.histogram(processed_funnel, x="funnel_stage", color="funnel_stage"))

elif app_panel == "Reports and Analytics Gateway (All 10 Keys)":
    st.header("Reports and Analytics Portfolio Gateway")
    selected_key_tab = st.selectbox("Select Compliance Report:", [
        "Compiles standard and ad hoc reports",
        "Provides reports, analysis and data interpretation",
        "Identifies areas of opportunity and presents findings",
        "Provides productivity analysis reports",
        "Develops and maintains reports to measure operational",
        "May be required to prepare ad hoc reports required of association",
        "Compiles recurring operational review that includes trend analysis",
        "May assists with departmental inventory reporting",
        "May be required to prepare ad hoc reporting that assists with measuring department performance",
        "Collaborate with a variety of stakeholders across campus"
    ])

    if "Compiles standard and ad hoc reports" in selected_key_tab:
        st.write("Key 1: Standardized Triage Console active.")
    
    elif "Provides reports, analysis and data interpretation" in selected_key_tab:
        st.markdown("### Key 2: Departmental Interpretation Ledger Matrix")
        raw_fac_data = st.session_state.faculty_retention_db.copy()
        c_filt, c_sort = st.columns(2)
        with c_filt:
            dept_select = st.selectbox("Filter Key 2 by Department:", ["All Departments"] + list(raw_fac_data["department_assignment"].unique()), key="k2_dept")
        with c_sort:
            sort_by = st.selectbox("Sort Key 2 Faculty By:", ["Name (A-Z)", "Tenure Years (High to Low)"], key="k2_sort")
        if dept_select != "All Departments":
            raw_fac_data = raw_fac_data[raw_fac_data["department_assignment"] == dept_select]
        if sort_by == "Tenure Years (High to Low)":
            raw_fac_data = raw_fac_data.sort_values(by="tenure_years_at_institution", ascending=False)
        else:
            raw_fac_data = raw_fac_data.sort_values(by="faculty_name")
        st.table(raw_fac_data)
        st.plotly_chart(px.bar(raw_fac_data, x="faculty_name", y="semester_credit_hours_load", color="appointment_track"))

    elif "Identifies areas of opportunity and presents findings" in selected_key_tab:
        st.write("Key 3: Leadership Findings active.")
    elif "Provides productivity analysis reports" in selected_key_tab:
        st.write("Key 4: Productivity Analysis active.")
    elif "Develops and maintains reports to measure operational" in selected_key_tab:
        st.write("Key 5: Operational Utilization active.")
    elif "May be required to prepare ad hoc reports required of association" in selected_key_tab:
        st.write("Key 6: Regulatory Compliance active.")
    elif "Compiles recurring operational review that includes trend analysis" in selected_key_tab:
        st.write("Key 7: Trend Analytics active.")
    elif "May assists with departmental inventory reporting" in selected_key_tab:
        st.write("Key 8: Inventory Reporting active.")
    elif "May be required to prepare ad hoc reporting that assists with measuring department performance" in selected_key_tab:
        st.write("Key 9: Performance Matrix active.")
    elif "Collaborate with a variety of stakeholders across campus" in selected_key_tab:
        st.write("Key 10: Data Strategy Alignment active.")
