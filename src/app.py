import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles Navigate360 Workspace", layout="wide")

# ==========================================
# CENTRALIZED HIGH-DENSITY LIFE CYCLE DATA STATES (40 REALISTIC STUDENT RECORDS)
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
            "Summer 2026", "Fall 2026 Preview", "Spring 2026", "Fall 2026 Preview", "Spring 2026",
            "Summer 2026", "Fall 2026 Preview", "Spring 2026", "Fall 2026 Preview", "Fall 2026 Preview"
        ],
        "classification": [
            "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", 
            "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year",
            "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", 
            "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year",
            "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", 
            "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year",
            "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", 
            "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year"
        ],
        "cumulative_gpa": [0.00 for _ in range(40)], 
        "studentvue_sync_status": [
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Academic Hold - Missing Transcript", 
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Good Standing - Regular Sync", 
            "Good Standing - Regular Sync", "Financial Hold - Balance Due", "Good Standing - Regular Sync", 
            "Probation Sync Alert", "Good Standing - Regular Sync", "Academic Hold - Missing Transcript",
            "Good Standing - Regular Sync", "Probation Sync Alert", "Good Standing - Regular Sync",
            "Good Standing - Regular Sync", "Financial Hold - Balance Due", "Good Standing - Regular Sync",
            "Academic Hold - Missing Transcript", "Good Standing - Regular Sync", "Good Standing - Regular Sync",
            "Probation Sync Alert", "Good Standing - Regular Sync", "Financial Hold - Balance Due",
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Good Standing - Regular Sync",
            "Academic Hold - Missing Transcript", "Good Standing - Regular Sync", "Good Standing - Regular Sync",
            "Probation Sync Alert", "Good Standing - Regular Sync", "Financial Hold - Balance Due",
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Academic Hold - Missing Transcript",
            "Good Standing - Regular Sync", "Probation Sync Alert", "Good Standing - Regular Sync", "Financial Hold - Balance Due"
        ],
        "funnel_stage": [
            "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Admitted", "Applied", "Inquiry",
            "Enrolled", "Enrolled", "Enrolled", "Admitted", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Admitted", "Enrolled",
            "Enrolled", "Enrolled", "Enrolled", "Admitted", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Admitted", "Enrolled",
            "Enrolled", "Enrolled", "Enrolled", "Admitted", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Admitted", "Inquiry"
        ],
        "outreach_campaign_group": [
            "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", 
            "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Scholarship Push", "Fall Preview Invite",
            "Completed Yield", "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Completed Yield",
            "Completed Yield", "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Completed Yield",
            "Completed Yield", "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Completed Yield",
            "Completed Yield", "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Completed Yield",
            "Completed Yield", "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Completed Yield",
            "Completed Yield", "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Fall Preview Invite"
        ],
        "predicted_yield_probability": [
            "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "High", "Medium", "Low",
            "Enrolled", "Enrolled", "Enrolled", "High", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "High", "Enrolled",
            "Enrolled", "Enrolled", "Enrolled", "High", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "High", "Enrolled",
            "Enrolled", "Enrolled", "Enrolled", "High", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "High", "Low"
        ],
        "last_interaction_date": ["2026-03-10" for _ in range(40)],
        "to_dos_pending": [i % 4 for i in range(40)],
        "communication_preference": ["Email" if i % 2 == 0 else "Text/SMS" for i in range(40)],
        "category_tags": ["First Generation, Pell-Eligible" if i % 3 == 0 else "Good Academic Standing" for i in range(40)],
        "staff_meeting_prep_notes": [f"Sourced cohort record update tracking slot sequence flag {i}." for i in range(1, 41)]
    })

if "faculty_retention_db" not in st.session_state:
    st.session_state.faculty_retention_db = pd.DataFrame({
        "faculty_id": [f"FAC-{200+i}" for i in range(1, 21)],
        "faculty_name": [
            "Dr. Stacey Nebriaga", "Prof. Michael Gabriele", "Dr. Tyler Pede", "Dr. Thomas Anderson", 
            "Prof. Emily Holzgrefe", "Dr. Sarah Jenkins", "Dr. David Vance", "Prof. Elena Rostova",
            "Dr. Robert Langdon", "Prof. Minerva McGonagall", "Dr. Alan Grant", "Dr. Ellie Sattler",
            "Prof. Charles Xavier", "Dr. Henry Wu", "Dr. Ian Malcolm", "Prof. Albus Dumbledore",
            "Dr. Severus Snape", "Prof. Gilderoy Lockhart", "Dr. Remus Lupin", "Dr. Pomona Sprout"
        ],
        "department_assignment": [
            "Biology", "Information Systems", "Economics", "Management", "Marketing", 
            "Accounting", "Cybersecurity", "Finance", "Hospitality Management", "Information Systems", 
            "Management", "Marketing", "Hospitality Management", "Entrepreneurship", "Biology",
            "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance"
        ],
        "appointment_track": [
            "Tenured Faculty", "Non-Tenure Lecturer", "Tenure-Track Assistant", "Tenured Faculty", 
            "Non-Tenure Clinical", "Tenure-Track Assistant", "Tenured Faculty", "Non-Tenure Lecturer",
            "Tenured Faculty", "Tenured Faculty", "Tenure-Track Assistant", "Tenured Faculty",
            "Tenured Faculty", "Non-Tenure Lecturer", "Non-Tenure Clinical", "Tenured Faculty",
            "Tenured Faculty", "Non-Tenure Lecturer", "Tenure-Track Assistant", "Tenured Faculty"
        ],
        "faculty_staff_status": [
            "Active - Full Instructional Load", "Active - Full Instructional Load", "Pending Tenure Review Notice", 
            "Sabbatical - Research Active", "Active - Full Instructional Load", "Pending Tenure Review Notice", 
            "Active - Full Instructional Load", "Medical Leave", "Active - Full Instructional Load",
            "Active - Full Instructional Load", "Pending Tenure Review Notice", "Active - Full Instructional Load",
            "Sabbatical - Research Active", "Active - Full Operations Load", "Active - Full Instructional Load",
            "Active - Full Instructional Load", "Active - Full Instructional Load", "Medical Leave",
            "Pending Tenure Review Notice", "Active - Full Instructional Load"
        ],
        "tenure_years_at_institution": [
            12.5, 3.0, 4.5, 16.0, 2.5, 5.0, 14.0, 1.5,
            8.0, 22.0, 3.5, 11.0, 19.5, 4.0, 1.0, 35.0,
            15.0, 2.0, 5.5, 13.0
        ],
        "semester_credit_hours_load": [
            420, 580, 390, 310, 620, 410, 330, 600,
            450, 300, 510, 400, 280, 590, 610, 200,
            350, 550, 430, 380
        ],
        "faculty_retention_hazard_flag": [
            "Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "Medium Risk",
            "Low Risk", "Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "High Risk", "Low Risk",
            "Low Risk", "High Risk", "Low Risk", "Low Risk"
        ],
        "estimated_departure_timeline": [
            "Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years",
            "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Immediate Risk (<1 Year)", "Stable (>5 Years)",
            "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)"
        ],
        "retention_notes": [
            "Stable institutional asset profiles verified.", "Seeking timeline promotion track clarification.",
            "Progressing toward standard tenure review.", "Endowed academic chairholder active.",
            "Needs structural retention strategy intervention.", "Research grant funding targets secured.",
            "Approaching standard retirement matrix horizon.", "Market salary compression issues logged.",
            "Stable institutional asset profiles verified.", "Seeking timeline promotion track clarification.",
            "Progressing toward standard tenure review.", "Endowed academic chairholder active.",
            "Needs structural retention strategy intervention.", "Research grant funding targets secured.",
            "Approaching standard retirement matrix horizon.", "Market salary compensation logs updated.",
            "Stable institutional asset profiles verified.", "Seeking timeline promotion track clarification.",
            "Progressing toward standard tenure review.", "Endowed academic chairholder active."
        ]
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
# SIDEBAR NAVIGATION INTERFACE
# ==========================================
st.sidebar.title("Coles Navigate360")
st.sidebar.markdown("**Operational Hub:** `Center for Student Success`")
st.sidebar.write("---")

st.sidebar.subheader("Layer Visibility Options")
show_students = st.sidebar.checkbox("Show Student Data Tracks", value=True)
show_faculty = st.sidebar.checkbox("Show Faculty Staff Tracks", value=True)
st.sidebar.write("---")

st.sidebar.subheader("Global Scope Filters")
dept_filter = st.sidebar.selectbox("Filter by Academic Department Major:", options=["All Departments"] + list(st.session_state.coles_capacity_db["major_name"].unique()))
term_filter = st.sidebar.selectbox("Target Academic Term Horizon:", options=["All Semesters", "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview"])
studentvue_filter = st.sidebar.selectbox("StudentVue Registration Profile Status:", options=["All Student Tiers", "Good Standing - Regular Sync", "Academic Hold - Missing Transcript", "Financial Hold - Balance Due", "Probation Sync Alert"])
faculty_status_filter = st.sidebar.selectbox("Faculty Staff Administrative Status:", options=["All Faculty Tiers", "Active - Full Instructional Load", "Pending Tenure Review Notice", "Sabbatical - Research Active"])

processed_funnel = st.session_state.enrollment_funnel_db.copy()
processed_faculty = st.session_state.faculty_retention_db.copy()

if dept_filter != "All Departments":
    processed_funnel = processed_funnel[processed_funnel["intended_major"] == dept_filter]
    processed_faculty = processed_faculty[processed_faculty["department_assignment"] == dept_filter]

if term_filter != "All Semesters":
    processed_funnel = processed_funnel[processed_funnel["academic_term"] == term_filter]

if studentvue_filter != "All Student Tiers":
    processed_funnel = processed_funnel[processed_funnel["studentvue_sync_status"] == studentvue_filter]

if faculty_status_filter != "All Faculty Tiers":
    processed_faculty = processed_faculty[processed_faculty["faculty_staff_status"] == faculty_status_filter]

# ==========================================
# RELATIONAL REGISTRY COMPILATION
# ==========================================
def assign_faculty_and_grades(row):
    major = row["intended_major"]
    dept_fac = st.session_state.faculty_retention_db[st.session_state.faculty_retention_db["department_assignment"] == major]
    if len(dept_fac) >= 2:
        current_prof = dept_fac.iloc[0]["faculty_name"]
        past_prof = dept_fac.iloc[1]["faculty_name"]
    elif len(dept_fac) == 1:
        current_prof = dept_fac.iloc[0]["faculty_name"]
        past_prof = "Dr. Stacey Nebriaga (Gen-Ed)"
    else:
        current_prof = "Dr. Thomas Anderson (Adjunct)"
        past_prof = "Prof. Minerva McGonagall"
        
    student_num = int(row["applicant_id"].split("-")[1])
    
    if student_num % 4 == 0:
        grades = ["A", "A", "A", "A"]  
    elif student_num % 4 == 1:
        grades = ["A", "B", "A", "A"]  
    elif student_num % 4 == 2:
        grades = ["A", "B", "B", "A"]  
    else:
        grades = ["B", "B", "C", "B"]  
        
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    true_gpa = round(sum(grade_points[g] for g in grades) / len(grades), 2)
    
    return pd.Series([current_prof, past_prof, grades[0], grades[1], grades[2], grades[3], true_gpa])

processed_funnel[["Current Professor", "Past Professor", "G1", "G2", "G3", "G4", "cumulative_gpa"]] = processed_funnel.apply(assign_faculty_and_grades, axis=1)

st.sidebar.write("---")
st.sidebar.subheader("Navigation Terminal")

nav_options = []
if show_students: nav_options.append("Student Lifecycle Portal (StudentVue)")
if show_faculty: nav_options.append("Faculty Retention Terminal")
if show_students: nav_options.append("EAB Targeted Campaign Manager")
nav_options.append("Reports and Analytics Gateway (All 10 Keys)")

app_panel = st.sidebar.radio("Select Operational Workspace Desk:", options=nav_options)

# ==========================================
# MODULE 1: STUDENT LIFECYCLE PORTAL
# ==========================================
if app_panel == "Student Lifecycle Portal (StudentVue)":
    main_workspace, ai_assistant_col = st.columns([3, 1])
    
    with main_workspace:
        st.markdown("## Staff Home: Funnel Progress and Prospect Management")
        st.write("---")
        
        fc1, fc2, fc3, fc4 = st.columns(4)
        with fc1: st.metric("Sourced Active Records Focus", value=len(processed_funnel))
        with fc2: st.metric("Admitted Student Pipeline", value=len(processed_funnel[processed_funnel["funnel_stage"] == "Admitted"]))
        with fc3: st.metric("Enrolled Yield Conversion", value=len(processed_funnel[processed_funnel["funnel_stage"] == "Enrolled"]))
        with fc4: 
            if "to_dos_pending" in processed_funnel.columns and len(processed_funnel) > 0:
                st.metric("Open Reminders/To-Dos", value=int(processed_funnel["to_dos_pending"].sum()))
            else: st.metric("Open Reminders/To-Dos", value=0)
        
        st.write("")
        if len(processed_funnel) > 0:
            selected_prospect = st.selectbox("Select Active Student Record Dossier to Audit:", options=list(processed_funnel["student_name"].unique()))
            master_match = processed_funnel[processed_funnel["student_name"] == selected_prospect]
            idx = master_match.index[0]
            p_row = master_match.loc[idx]
            
            status_map = {
                "Enrolled": "On-Track / Approved for Graduation Degree Yield",
                "Admitted": "Active Enrolled / Pre-Registration Advising Track",
                "Applied": "Institutional Outbound Route / Voluntarily Transferred",
                "Inquiry": "Academic Dismissal / Flunked Out Risk"
            }
            current_status = status_map.get(p_row['funnel_stage'], "Active Tracking")
            
            with st.container(border=True):
                st.markdown(f"### Comprehensive Student Lifecycle Dossier: **{p_row['student_name']}**")
                st.markdown(f"**Student Identification Hash:** `{p_row['applicant_id']}` | **Classification:** `{p_row['classification']}`")
                st.write("---")
                
                t1, t2, t3 = st.columns(3)
                with t1:
                    st.markdown("#### 1. Entry and Enrollment")
                    st.write(f"* **Initial Matriculation Term:** {p_row['academic_term']}")
                    st.write(f"* **Declared Focus Field Major:** {p_row['intended_major']}")
                    st.write(f"* **Cumulative Grade Point Index (GPA):** **{p_row['cumulative_gpa']}**")
                with t2:
                    st.markdown("#### 2. Current Status")
                    st.write(f"* **EAB Campaign Track Status:** {p_row['outreach_campaign_group']}")
                    st.write(f"* **Current Registry Sync Vector:** {p_row['studentvue_sync_status']}")
                with t3:
                    st.markdown("#### 3. Retention Outcome")
                    st.info(f"**Current Standing Result:**\n{current_status}")
                
                st.write("---")
                
                st.markdown("#### Comprehensive Student Career Academic Transcript Matrix")
                transcript_history = pd.DataFrame({
                    "Academic Semester": [p_row['academic_term'], "Fall 2025", "Spring 2025", "Fall 2024"],
                    "Course Code and Subject Title": [
                        f"{p_row['intended_major']} 4400: Senior Seminar Capstone", 
                        f"{p_row['intended_major']} 3300: Advanced Analytical Systems", 
                        "BUSA 2100: Business Communication Foundations", 
                        "ENGL 1101: Composition Rhetoric Core"
                    ],
                    "Assigned Instructor": [
                        p_row['Current Professor'], 
                        p_row['Past Professor'], 
                        "Dr. Stacey Nebriaga (Gen-Ed)", 
                        "Prof. Minerva McGonagall"
                    ],
                    "Earned Mark / Letter Grade": [p_row['G1'], p_row['G2'], p_row['G3'], p_row['G4']]
                })
                st.dataframe(transcript_history.astype(str), hide_index=True)

            st.write("")
            st.subheader("AI Assistant: Automated Meeting Prep Insights")
            with st.container(border=True):
                st.markdown(f"*Institutional Digest Material:* **\"{p_row['staff_meeting_prep_notes']}\"**")
                
            st.write("---")
            st.subheader("Streamline Applicant Progress Queue Tasks")
            w1, w2, w3 = st.columns([1, 1, 2])
            with w1: stage_update = st.selectbox("Advance Student Status Outcome:", options=["Enrolled", "Admitted", "Applied", "Inquiry"])
            with w2: camp_update = st.selectbox("Reassign Outreach Campaign:", options=["Completed Yield", "Fall Preview Invite", "Scholarship Push", "Housing Deposit Nudge"])
            with w3: append_note = st.text_input("Append Diagnostic Communication Log Entry:")
                
            if st.button("Commit Adjustments to Centralized Funnel View"):
                st.session_state.enrollment_funnel_db.at[idx, "funnel_stage"] = stage_update
                st.session_state.enrollment_funnel_db.at[idx, "outreach_campaign_group"] = camp_update
                if append_note: st.session_state.enrollment_funnel_db.at[idx, "staff_meeting_prep_notes"] = f"{p_row['staff_meeting_prep_notes']} | CDO Edit: {append_note}"
                st.success("Funnel attributes modified updates pushed live.")
                st.rerun()
        else: st.warning("No tracking records match filters.")
            
        st.write("---")
        st.subheader("📋 Centralized View: Filtered Recruitment Pipeline Ledger")
        st.dataframe(processed_funnel[["applicant_id", "student_name", "intended_major", "academic_term", "funnel_stage", "cumulative_gpa", "Current Professor", "Past Professor"]].astype(str), hide_index=True)

    with ai_assistant_col:
        st.markdown("### AI Assistant")
        st.write("---")
        if len(processed_funnel) > 0 and 'p_row' in locals():
            with st.container(border=True):
                st.markdown(f"**Target Focus:** `{p_row['student_name']}`")
                st.write(f"* **Term Scope:** {p_row['academic_term']}")
                st.write(f"* **Yield Probability:** {p_row['predicted_yield_probability']}")
        st.write("")
        st.button("Deploy Automated Nudge reminder")
        st.button("Invite to Connect with Staff/Events")

# ==========================================
# MODULE 2: FACULTY RETENTION TERMINAL
# ==========================================
elif app_panel == "Faculty Retention Terminal":
    st.header("Faculty Roster Retention and Workload Terminal")
    st.markdown("##### *Auditing teacher tenure years, credit hour generation workloads, and administrative retention risk variables.*")
    st.write("---")
    
    if len(processed_faculty) > 0:
        faculty_picker = st.selectbox("Select Detailed Faculty Profile File to Open:", options=list(processed_faculty["faculty_name"].unique()))
        f_row = processed_faculty[processed_faculty["faculty_name"] == faculty_picker].iloc[0]
        
        with st.container(border=True):
            st.markdown(f"### Academic Staff File: **{f_row['faculty_name']}** | ID: `{f_row['faculty_id']}`")
            st.write("")
            f_c1, f_c2, f_c3 = st.columns(3)
            with f_c1:
                st.markdown(f"**Departmental Unit:** `{f_row['department_assignment']}`")
                st.markdown(f"**Appointment Track:** `{f_row['appointment_track']}`")
                st.markdown(f"**Teacher Status Update:** `{f_row['faculty_staff_status']}`")
            with f_c2:
                st.markdown(f"**Tenure Longevity Curve:** `{f_row['tenure_years_at_institution']} Years STAYING`")
                st.markdown(f"**Instructional Load Metric:** `{f_row['semester_credit_hours_load']} SCH`")
            with f_c3:
                st.markdown(f"**Attrition Risk Tier:** `{f_row['faculty_retention_hazard_flag']}`")
                st.markdown(f"**Departure Horizon Estimate:** `{f_row['estimated_departure_timeline']}`")
            
            st.write("---")
            
            total_taught = int(f_row['tenure_years_at_institution'] * (f_row['semester_credit_hours_load'] / 3) * 1.8)
            passed_students = int(total_taught * 0.88)
            graduated_students = int(passed_students * 0.94)
            failed_students = int(total_taught * 0.07)
            current_students = int(f_row['semester_credit_hours_load'] / 3)
            
            st.markdown("#### Longitudinal Instructional and Student Outcomes Ledger")
            st.write(f"* **Total Taught:** {total_taught:,} Students")
            st.write(f"* **Historical Passed:** {passed_students:,} Students")
            st.write(f"* **Historical Graduated:** {graduated_students:,} Students")
            st.write(f"* **Historical Failed:** {failed_students:,} Students")
            st.write(f"* **Active Enrollment:** {current_students} Students")
            
            st.write("---")
            st.markdown(f"**HR Analyst Log entries:** *\"{f_row['retention_notes']}\"*")
            
        st.write("---")
        f_g1, f_g2 = st.columns(2)
        with f_g1:
            fig_tenure = px.bar(processed_faculty, x="faculty_name", y="tenure_years_at_institution", title="Institutional Tenure Longevity Profiles", color="appointment_track", color_discrete_sequence=ksu_gold_palette)
            st.plotly_chart(fig_tenure)
        with f_g2:
            fig_hazard = px.pie(processed_faculty, values="semester_credit_hours_load", names="faculty_retention_hazard_flag", title="Workload (SCH) Distribution Tiers", hole=0.4, color_discrete_sequence=["#00E676", "#FFC400", "#FF5722"])
            st.plotly_chart(fig_hazard)
    else: st.warning("No teacher metrics log segments match active filters.")

# ==========================================
# MODULE 3: EAB TARGETED CAMPAIGN MANAGER
# ==========================================
elif app_panel == "EAB Targeted Campaign Manager":
    st.header("EAB Custom Communications Campaign Manager")
    st.write("---")
    
    c_name = st.text_input("Campaign Name Target Label:", value="Fall 2026 Orientation Completion Nudge")
    c_channel = st.selectbox("Primary Communication Channel Strategy:", options=["All Strategy Channels", "Personalized Text/SMS Blasts", "Targeted Email Sequences", "Shared Event Invitation Portals"])
    c_cohort = st.selectbox("Target Audience Filter Group Stage:", options=["All Cohort Groups", "Inquiry Population Pool", "Applied - Awaiting Decision", "Admitted - Yield Acceleration Focus"])
    
    st.write("")
    if st.button("Deploy Nuanced Outreach and Launch Campaign"):
        st.success(f"Outreach track '{c_name}' deployed successfully!")

    st.write("---")
    st.subheader("Continuous Progress Funnel Monitor")
    
    chart_data = processed_funnel.copy()
    
    if c_channel == "Personalized Text/SMS Blasts":
        chart_data = chart_data[chart_data["communication_preference"] == "Text/SMS"]
    elif c_channel == "Targeted Email Sequences":
        chart_data = chart_data[chart_data["communication_preference"] == "Email"]
        
    if c_cohort == "Inquiry Population Pool":
        chart_data = chart_data[chart_data["funnel_stage"] == "Inquiry"]
    elif c_cohort == "Applied - Awaiting Decision":
        chart_data = chart_data[chart_data["funnel_stage"] == "Applied"]
    elif c_cohort == "Admitted - Yield Acceleration Focus":
        chart_data = chart_data[chart_data["funnel_stage"] == "Admitted"]

    fig_funnel = px.histogram(
        chart_data, 
        x="funnel_stage", 
        title="Active Progress Pipeline Allocations Profile", 
        color="funnel_stage", 
        color_discrete_sequence=ksu_gold_palette
    )
    st.plotly_chart(fig_funnel)

# ==========================================
# MODULE 4: REPORTS & ANALYTICS GATEWAY
# ==========================================
elif app_panel == "Reports and Analytics Gateway (All 10 Keys)":
    st.header("Reports and Analytics Portfolio Gateway")
    st.markdown("##### *Mapping interactive query views to verify all 10 Key Responsibilities.*")
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
        "Dashboard Validation Status": ["Engine Integrated and Deployable"] * 10
    })
    st.dataframe(ledger_df.astype(str), hide_index=True)
    st.write("---")
    
    selected_key_tab = st.selectbox("Select Active Compliance Report to Query Natively:", options=list(ledger_df["Job Description Requirement Statement"]))
    st.write("---")
    
    if "1. Compiles standard and ad hoc" in selected_key_tab:
        st.markdown("### Key 1: Standardized vs. Ad Hoc Task Triage Console")
        st.caption("Navigate360 Implementation Workflow: Inbound queue tracking live request tickets generated by assigned KSU departments.")
        
        rep_type = st.radio("Select Target Data Intake Flow Stream:", ["Standard Recurring (Weekly Ingestion)", "Ad Hoc Live Extract Requests"])
        
        triage_data = pd.DataFrame({
            "Originating Department Name": [
                "Coles College Office of Finance", "Information Systems Care Unit", "Department of Economics", 
                "Admissions and Yield Hub", "Coles Undergraduate Advising", "Office of the Registrar", 
                "Department of Management", "Coles College Office of Finance", "Information Systems Care Unit", 
                "Admissions and Yield Hub"
            ],
            "Requested Operational Task": [
                "Daily Sales Summary Metric Audit and Workload Extract", 
                "Ad-Hoc Equipment Inventory Hardware Utilization Audit", 
                "Recurring Trailing Longitudinal Multi-Semester Trend Run", 
                "EAB Targeted Campaign Communication Productivity Analysis",
                "Weekly StudentVue Advising Sync Status Exception Report",
                "FTE Census Enrollment Validation Ledger Data Compilations",
                "Standard Core Course Grade Distribution Capacity Audit",
                "Urgent End-of-Month Revenue and Fee Discrepancy Reconciliation",
                "Emergency Cybersecurity Lab Software Key Utilization Pull",
                "Ad-Hoc High-Risk Dropout Cohort Extraction Analysis"
            ],
            "Request Classification Track": [
                "Ad Hoc Live Extract Requests", "Ad Hoc Live Extract Requests", "Standard Recurring (Weekly Ingestion)", 
                "Standard Recurring (Weekly Ingestion)", "Standard Recurring (Weekly Ingestion)", "Standard Recurring (Weekly Ingestion)", 
                "Standard Recurring (Weekly Ingestion)", "Ad Hoc Live Extract Requests", "Standard Recurring (Weekly Ingestion)", 
                "Standard Recurring (Weekly Ingestion)"
            ],
            "Urgency Matrix Rating Indicator": [
                "CRITICAL SEVERITY (Immediate Turnaround Vector)", "HIGH URGENCY (Same-Day Processing Queue)", 
                "ROUTINE TIMELINE (Monday Morning Autopilot)", "ROUTINE TIMELINE (Monday Morning Autopilot)",
                "ROUTINE TIMELINE (Monday Morning Autopilot)", "ROUTINE TIMELINE (Monday Morning Autopilot)",
                "ROUTINE TIMELINE (Monday Morning Autopilot)", "CRITICAL SEVERITY (Immediate Turnaround Vector)",
                "ROUTINE TIMELINE (Monday Morning Autopilot)", "ROUTINE TIMELINE (Monday Morning Autopilot)"
            ]
        })
        
        clean_df = triage_data.copy().astype(str)
        filtered_triage = clean_df[clean_df["Request Classification Track"] == str(rep_type)]
        
        st.markdown(f"#### Incoming Functional Request Log — [Active Streams: {len(filtered_triage)} Departmental Tickets]")
        
        if len(filtered_triage) == 0:
            st.info("No active tickets found matching this category workflow track.")
        else:
            for index, row in filtered_triage.iterrows():
                with st.container(border=True):
                    st.markdown(f"Department Source: {row['Originating Department Name']}")
                    st.markdown(f"Task Description: {row['Requested Operational Task']}")
                    st.markdown(f"Urgency Scale Rank: {row['Urgency Matrix Rating Indicator']}")

    elif "2. Provides reports, analysis and data interpretation" in selected_key_tab:
        st.markdown("### Key 2: Departmental Interpretation Ledger Matrix")
        c_act, c_graph = st.columns(2)
        with c_act:
            st.info("Assigned Department Core Infrastructure Summary Profile")
            st.dataframe(processed_faculty[["faculty_name", "department_assignment", "appointment_track", "faculty_staff_status", "tenure_years_at_institution"]].astype(str), hide_index=True)
        with c_graph:
            fig_key2 = px.bar(processed_faculty, x="faculty_name", y="semester_credit_hours_load", title="Semester Credit Hours Generation Load by Faculty Member", color="appointment_track", color_discrete_sequence=ksu_gold_palette)
            st.plotly_chart(fig_key2)

    elif "3. Identifies areas of opportunity" in selected_key_tab:
        st.markdown("### Key 3: Leadership Findings & Strategic Recommendations Engine")
        low_gpa_leads = processed_funnel[processed_funnel["cumulative_gpa"] < 3.4] if len(processed_funnel) > 0 else pd.DataFrame()
        with st.container(border=True):
            st.markdown("🏆 **Executive Data Insights Memorandum**")
            st.write(f"1. **Identified Area of Opportunity:** Found **{len(low_gpa_leads)}** active records maintaining cumulative GPA indices under the 3.4 line.")
            st.write("2. **Actionable Recommendation:** Deploy automated EAB communications targeting validation parameters to reduce block friction.")
        if len(low_gpa_leads) > 0:
            st.error("🚨 Opportunity Tracking Watchlist:")
            st.dataframe(low_gpa_leads[["student_name", "intended_major", "academic_term", "cumulative_gpa"]].astype(str), hide_index=True)

    elif "4. Provides productivity analysis reports" in selected_key_tab:
        st.markdown("### Key 4: Outreach Campaign Effectiveness Productivity Audit Log")
        if len(processed_funnel) > 0:
            prod_df = processed_funnel.groupby("outreach_campaign_group").agg(total_prospects_reached=("applicant_id", "count"), total_pending_tasks=("to_dos_pending", "sum"), mean_gpa_index=("cumulative_gpa", "mean")).reset_index()
            c_p1, c_p2 = st.columns(2)
            with c_p1: st.dataframe(prod_df.astype(str), hide_index=True)
            with c_p2:
                fig_prod = px.bar(prod_df, x="outreach_campaign_group", y="total_prospects_reached", title="Total Sourced Engagement Volume per Campaign Group", color="outreach_campaign_group", color_discrete_sequence=ksu_gold_palette)
                st.plotly_chart(fig_prod)

    elif "5. Develops and maintains reports to measure operational" in selected_key_tab:
        st.markdown("### Key 5: Operational Utilization & Activity Benchmarks")
        if len(processed_funnel) > 0:
            util_df = processed_funnel.groupby("communication_preference").size().reset_index(name="active_allocated_leads")
            c_u1, c_u2 = st.columns(2)
            with c_u1: st.dataframe(util_df.astype(str), hide_index=True)
            with c_u2:
                fig_util = px.pie(util_df, values="active_allocated_leads", names="communication_preference", title="Preferred Communication Channel Share Metrics Allocation", color_discrete_sequence=ksu_gold_palette, hole=0.4)
                st.plotly_chart(fig_util)

    elif "6. May be required to prepare ad hoc reports required of association" in selected_key_tab:
        st.markdown("### Key 6: External Oversight & Regulatory Compliance Framework Gateway")
        reg_target = st.selectbox("Select Regulatory Compliance Recipient Guideline Context:", ["USG State System Board Intake", "AACSB Evaluation Ledger Core", "Federal IPEDS Frame"])
        key6_data = processed_funnel.copy()
        
        with st.container(border=True):
            st.markdown(f"📁 **Active Compliance Manifest Structure:** `{reg_target}`")
            if reg_target == "USG State System Board Intake":
                st.success("🟢 Validation Protocol: Pass. System payload layout fields map out perfectly for state board data loops.")
                key6_data = key6_data[key6_data["cumulative_gpa"] >= 3.5]
            elif reg_target == "AACSB Evaluation Ledger Core":
                st.success("🟢 Validation Protocol: Pass. Faculty load matrices comply 100% with global AACSB data ingestion schemas.")
                key6_data = key6_data[key6_data["intended_major"].isin(["Accounting", "Economics", "Finance", "Management", "Marketing"])]
            elif reg_target == "Federal IPEDS Frame":
                st.success("🟢 Validation Protocol: Pass. Taxonomy outputs line up perfectly for electronic transmission to NCES.")
                key6_data = key6_data[key6_data["cumulative_gpa"] < 3.5]

        st.write("")
        st.markdown(f"#### Compliance Sub-Cohort Ledger Data View ({reg_target}) — [Total Records: {len(key6_data)} Students]")
        st.dataframe(key6_data[["applicant_id", "student_name", "intended_major", "academic_term", "cumulative_gpa", "Current Professor", "Past Professor"]].astype(str), hide_index=True)

    elif "7. Compiles recurring operational review that includes trend analysis" in selected_key_tab:
        st.markdown("### Key 7: Multi-Semester Longitudinal Trend Analytics Curve")
        trend_df = st.session_state.coles_capacity_db.copy()
        trend_df["retention_shortfall"] = trend_df["retention_goal_pct"] - trend_df["actual_retention_pct"]
        c_t1, c_t2 = st.columns([2, 3])
        with c_t1: st.dataframe(trend_df[["major_name", "retention_goal_pct", "actual_retention_pct", "retention_shortfall"]].astype(str), hide_index=True)
        with c_t2:
            fig_trend = px.line(trend_df, x="major_name", y="retention_shortfall", title="Longitudinal Retention Shortfall Gaps Trends Profile", markers=True, color_discrete_sequence=["#FF5722"])
            st.plotly_chart(fig_trend)

    elif "8. May assists with departmental inventory" in selected_key_tab:
        st.markdown("### Key 8: Departmental Technology Asset Inventory Analysis")
        c_i1, c_i2 = st.columns(2)
        with c_i1: st.dataframe(st.session_state.coles_capacity_db[["major_name", "undergrad_seat_count", "department_inventory_count"]].astype(str), hide_index=True)
        with c_i2:
            fig_inv = px.bar(st.session_state.coles_capacity_db, x="major_name", y="department_inventory_count", title="Hardware Kiosk Terminals Deployed by Care Hub Unit", color="major_name", color_discrete_sequence=ksu_gold_palette)
            st.plotly_chart(fig_inv)

    elif "9. May be required to prepare ad hoc reporting that assists with measuring department performance" in selected_key_tab:
        st.markdown("### Key 9: Center Performance & Program Effectiveness Matrix")
        if len(processed_funnel) > 0:
            res_counts = processed_funnel.groupby("funnel_stage").size().reset_index(name="total_cases")
            c_pf1, f_pf2 = st.columns(2)
            with c_pf1: st.dataframe(res_counts.astype(str), hide_index=True)
            with f_pf2:
                fig_perf = px.bar(res_counts, x="funnel_stage", y="total_cases", title="Recruitment Progress Conversion Rates Performance Profile", color="funnel_stage", color_discrete_sequence=ksu_gold_palette)
                st.plotly_chart(fig_perf)

    elif "10. Collaborate with a variety of stakeholders across campus" in selected_key_tab:
        st.markdown("### Key 10: Office of University Data Strategy Alignment Matrix")
        sync_scope = st.selectbox("Select Synchronization Scope Ring Natively:", ["All Synced Records", "Sync Failures / Alerts Only"])
        key10_data = processed_funnel.copy()
        if sync_scope == "Sync Failures / Alerts Only":
            key10_data = key10_data[key10_data["studentvue_sync_status"].str.contains("Hold|Alert")]
            
        with st.container(border=True):
            st.markdown("### University Policy Policy Mapping Framework Terminal")
            st.write("🔗 **Data Governance Layer:** Kennesaw State University Master Data Strategy Directive Compliance standard verified.")
            st.write("📡 **API Synchronization Endpoint Handshake:** `https://data-strategy.kennesaw.edu/v1/sync` active.")
            st.success("🟢 **Alignment Confirmed:** Local fields mapped perfectly match KSU's central data strategy taxonomy.")

        st.write("---")
        st.markdown(f"#### Central Synchronization Taxonomy Audit Ledger ({sync_scope}) — [Total Records: {len(key10_data)} Students]")
        st.dataframe(key10_data[["applicant_id", "student_name", "intended_major", "academic_term", "funnel_stage", "Current Professor", "Past Professor", "cumulative_gpa", "studentvue_sync_status"]].astype(str), hide_index=True)

I think it's because python 3.14 can you write it over without emojis anywhere in data states please completely text safe no emoji even in keys or maps tags anywhere? Make everything pure text string safely. Use basic markdown style elements instead of emojis. Fix line 9 error. Change use container width to false for safety fallback everywhere.
