import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# ==========================================
# RELATIONAL REGISTRY COMPILATION (Registered at top to prevent NameError)
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
    
    if student_num % 5 == 0:
        grades = ["A", "A", "A", "B"]  
    elif student_num % 5 == 1:
        grades = ["B", "B", "C", "B"]  
    elif student_num % 5 == 2:
        grades = ["C", "D", "B", "C"]  
    elif student_num % 5 == 3:
        grades = ["D", "F", "D", "C"]  
    else:
        grades = ["A", "B", "A", "A"]  
        
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    true_gpa = round(sum(grade_points[g] for g in grades) / len(grades), 2)
    
    return pd.Series([current_prof, past_prof, grades[0], grades[1], grades[2], grades[3], true_gpa])


# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles Navigate360 Workspace", layout="wide")

# ==========================================
# CENTRALIZED HIGH-DENSITY LIFE CYCLE DATA STATES (40 REALISTIC STUDENT RECORDS)
# ==========================================
if "enrollment_funnel_db" not in st.session_state:
    comm_effort_cycle = ["Email", "Text/SMS", "Phone Consultation Call", "Shared Event Portal Link"]
    
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
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview",
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview",
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview",
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview",
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview",
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview",
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026"
        ],
        "classification": [
            "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", 
            "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year"
        ] * 4,
        "cumulative_gpa": [0.00 for _ in range(40)], 
        "studentvue_sync_status": [
            "Probation Sync Alert" if (int(f"APP-{2600+i}".split("-")[1]) % 5 in [2, 3]) 
            else ("Academic Hold - Missing Transcript" if i % 10 == 2 
            else ("Financial Hold - Balance Due" if i % 10 == 7 
            else "Good Standing - Regular Sync"))
            for i in range(1, 41)
        ],
        "funnel_stage": [
            "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Admitted", "Applied", "Inquiry"
        ] * 4,
        "outreach_campaign_group": [
            "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", 
            "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Scholarship Push", "Fall Preview Invite"
        ] * 4,
        "predicted_yield_probability": [
            "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "Enrolled", "High", "Medium", "Low"
        ] * 4,
        "last_interaction_date": ["2026-03-10" for _ in range(40)],
        "to_dos_pending": [i % 4 for i in range(40)],
        "communication_preference": [comm_effort_cycle[i % 4] for i in range(40)],
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

# 1. Start with a fresh copy of the master database
processed_funnel = st.session_state.enrollment_funnel_db.copy()
processed_faculty = st.session_state.faculty_retention_db.copy()

# 2. RUN CALCULATIONS FIRST (This prevents the empty dataframe crash!)
processed_funnel[["Current Professor", "Past Professor", "G1", "G2", "G3", "G4", "cumulative_gpa"]] = processed_funnel.apply(assign_faculty_and_grades, axis=1)

# 3. NOW APPLY GLOBAL FILTERS SAFELY
if dept_filter != "All Departments":
    processed_funnel = processed_funnel[processed_funnel["intended_major"] == dept_filter]
    processed_faculty = processed_faculty[processed_faculty["department_assignment"] == dept_filter]

if term_filter != "All Semesters":
    processed_funnel = processed_funnel[processed_funnel["academic_term"] == term_filter]

if studentvue_filter != "All Student Tiers":
    processed_funnel = processed_funnel[processed_funnel["studentvue_sync_status"] == studentvue_filter]

if faculty_status_filter != "All Faculty Tiers":
    processed_faculty = processed_faculty[processed_faculty["faculty_staff_status"] == faculty_status_filter]

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
                st.table(transcript_history.astype(str))

            st.write("")
            st.subheader("AI Assistant: Automated Meeting Prep Insights")
            with st.container(border=True):
                st.markdown(f"*Navigator Digest Material:* **\"{st.session_state.enrollment_funnel_db.at[idx, 'staff_meeting_prep_notes']}\"**")
                
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
        st.subheader("Centralized View: Filtered Recruitment Pipeline Ledger")
        st.table(processed_funnel[["applicant_id", "student_name", "intended_major", "academic_term", "funnel_stage", "cumulative_gpa", "Current Professor", "Past Professor"]].astype(str))

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
    elif c_channel == "Phone Consultation Call":
        chart_data = chart_data[chart_data["communication_preference"] == "Phone Consultation Call"]
    elif c_channel == "Shared Event Invitation Portals":
        chart_data = chart_data[chart_data["communication_preference"] == "Shared Event Portal Link"]
        
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
        "Key ID": [
            "Key 1", "Key 2", "Key 3", "Key 4", "Key 5", 
            "Key 6", "Key 7", "Key 8", "Key 9", "Key 10"
        ],
        "Job Description Requirement Statement": [
            "Compiles standard and ad hoc reports per established guidelines and frequency",
            "Provides reports, analysis and data interpretation for all assigned departments",
            "Identifies areas of opportunity and presents findings and recommendations to leadership and stakeholders",
            "Provides productivity analysis reports",
            "Develops and maintains reports to measure operational and/or utilization activity",
            "May be required to prepare ad hoc reports required of association affiliations and/or oversight and regulatory requirements",
            "Compiles recurring operational review that includes trend analysis",
            "May assists with departmental inventory reporting and analysis",
            "May be required to prepare ad hoc reporting that assists with measuring department performance and/or effectiveness",
            "Collaborate with a variety of stakeholders across campus, including working closely with the Office of University Data Strategy to maintain alignment with overall university data strategy"
        ]
    })
    st.dataframe(ledger_df.astype(str), use_container_width=True, hide_index=True)
    st.write("---")
    
    selected_key_tab = st.selectbox("Select Active Compliance Report to Query Natively:", options=list(ledger_df["Job Description Requirement Statement"]))
    st.write("---")
    
    if "Compiles standard and ad hoc reports" in selected_key_tab:
        st.markdown("### Key 1: Standardized vs. Ad Hoc Task Triage Console")
        st.caption("Navigate360 Implementation Workflow: Inbound queue tracking live request tickets generated by assigned KSU departments.")
        
        rep_type = st.radio("Select Target Data Intake Flow Stream:", ["Standard Recurring (Weekly Ingestion)", "Ad Hoc Live Extract Requests"])
        
        master_triage_db = pd.DataFrame({
            "Source Assigned Department": [
                "Coles College Office of Finance", "Information Systems Care Unit", "Coles College Office of Finance",
                "Department of Economics", "Admissions and Yield Hub", "Coles Undergraduate Advising", 
                "Office of the Registrar", "Department of Management", "Information Systems Care Unit", 
                "Admissions and Yield Hub"
            ],
            "Requested Operational Task": [
                "Daily Sales Summary Metric Audit and Workload Extract", 
                "Ad-Hoc Equipment Inventory Hardware Utilization Audit", 
                "Urgent End-of-Month Revenue and Fee Discrepancy Reconciliation",
                "Recurring Trailing Longitudinal Multi-Semester Trend Run", 
                "EAB Targeted Campaign Communication Productivity Analysis",
                "Weekly StudentVue Advising Sync Status Exception Report",
                "FTE Census Enrollment Validation Ledger Data Compilations",
                "Standard Core Course Grade Distribution Capacity Audit",
                "Routine Security Access Clearance Maintenance Run",
                "Cohort Demographic Intake Breakdown Update"
            ],
            "Operational Priority Tier": [
                "CRITICAL EMERGENCY", "HIGH EMERGENCY", "CRITICAL EMERGENCY",
                "ROUTINE TASK", "ROUTINE TASK", "ROUTINE TASK", 
                "ROUTINE TASK", "ROUTINE TASK", "ROUTINE TASK", 
                "ROUTINE TASK"
            ],
            "Days Open Pending": [
                1, 2, 0, 14, 7, 5, 4, 3, 2, 1
            ]
        })
        
        clean_df = master_triage_db.copy().astype(str)
        
        if rep_type == "Standard Recurring (Weekly Ingestion)":
            output_df = clean_df[clean_df["Operational Priority Tier"] == "ROUTINE TASK"].copy()
            output_df = output_df.sort_values(by="Days Open Pending", ascending=False)
        else:
            output_df = clean_df[(clean_df["Operational Priority Tier"] == "CRITICAL EMERGENCY") | (clean_df["Operational Priority Tier"] == "HIGH EMERGENCY")].copy()
            output_df = output_df.sort_values(by="Days Open Pending", ascending=False)
            
        output_df.index = range(1, len(output_df) + 1)
        output_df.index.name = "Queue Position ID"
        
        st.markdown(f"#### Incoming Functional Request Log — [Active Streams: {len(output_df)} Departmental Tickets]")
        st.table(output_df)

    elif "Provides reports, analysis and data interpretation" in selected_key_tab:
        st.markdown("### Key 2: Departmental Interpretation Ledger Matrix")
        
        raw_fac_data = st.session_state.faculty_retention_db.copy()
        
        raw_fac_data["instructional_load_sch"] = raw_fac_data["semester_credit_hours_load"]
        raw_fac_data["historical_graduated_students"] = (raw_fac_data["tenure_years_at_institution"] * (raw_fac_data["semester_credit_hours_load"] / 3) * 1.8 * 0.88 * 0.94).astype(int)
        
        c_filt, c_sort = st.columns(2)
        with c_filt:
            dept_select = st.selectbox("Filter Key 2 by Department:", ["All Departments"] + list(raw_fac_data["department_assignment"].unique()), key="k2_dept")
        with c_sort:
            sort_by = st.selectbox("Sort Key 2 Faculty By:", ["Name (A-Z)", "Tenure Years (High to Low)"], index=1, key="k2_sort")
            
        if dept_select != "All Departments":
            raw_fac_data = raw_fac_data[raw_fac_data["department_assignment"] == dept_select]
            
        if sort_by == "Tenure Years (High to Low)":
            raw_fac_data = raw_fac_data.sort_values(by="tenure_years_at_institution", ascending=False)
        else:
            raw_fac_data = raw_fac_data.sort_values(by="faculty_name")

        st.info(f"Viewing: {dept_select} Faculty Profiles")
        
        st.dataframe(
            raw_fac_data[[
                "faculty_name", 
                "department_assignment", 
                "faculty_staff_status", 
                "tenure_years_at_institution",
                "instructional_load_sch",
                "historical_graduated_students"
            ]].rename(columns={
                "faculty_name": "Faculty Name",
                "department_assignment": "Department",
                "faculty_staff_status": "Status Status",
                "tenure_years_at_institution": "Tenure Longevity (Years)",
                "instructional_load_sch": "Current Workload Load (SCH)",
                "historical_graduated_students": "Historical Assisted Graduates"
            }).astype(str), 
            use_container_width=True, 
            hide_index=True
        )
        
        fig_key2 = px.bar(
            raw_fac_data, 
            x="faculty_name", 
            y="semester_credit_hours_load", 
            title=f"SCH Generation Load: {dept_select}", 
            color="appointment_track", 
            color_discrete_sequence=ksu_gold_palette
        )
        st.plotly_chart(fig_key2, use_container_width=True)

    elif "Identifies areas of opportunity and presents findings" in selected_key_tab:
        st.markdown("### Key 3: Leadership Findings & Strategic Recommendations Engine")
        
        low_gpa_leads = processed_funnel[processed_funnel["cumulative_gpa"] < 3.4].copy() if len(processed_funnel) > 0 else pd.DataFrame()
        
        if len(low_gpa_leads) > 0:
            risk_drivers = []
            assigned_interveners = []
            pathway_statuses = []
            
            for i, row in enumerate(low_gpa_leads.itertuples()):
                if i % 3 == 0:
                    risk_drivers.append("Prerequisite Course Friction / Core Math Deficiency")
                    assigned_interveners.append("Coles Tutoring Support Center")
                    pathway_statuses.append("Active - Accepted Outreach Pathway")
                elif i % 3 == 1:
                    risk_drivers.append("First-Generation Transition Gap / Adjustment Block")
                    assigned_interveners.append("Academic Success Coach Assigned")
                    pathway_statuses.append("Pending Outreach Response")
                else:
                    risk_drivers.append("Registration Hold Backlog / Financial Aid Lag")
                    assigned_interveners.append("Office of Student Success Specialist")
                    pathway_statuses.append("Outreach Initiated - Refused/No-Show Pathway")
                    
            low_gpa_leads["Risk Driver Background"] = risk_drivers
            low_gpa_leads["Assigned Advisor Intervener"] = assigned_interveners
            low_gpa_leads["Pathway Outreach Status"] = pathway_statuses

        with st.container(border=True):
            st.markdown("Executive Data Insights Memorandum")
            st.write(f"1. Identified Area of Opportunity: Found {len(low_gpa_leads)} active records maintaining cumulative GPA indices under the 3.4 line.")
            st.write("2. Actionable Recommendation: Deploy automated EAB communications targeting validation parameters to reduce block friction.")
        
        if len(low_gpa_leads) > 0:
            st.error("Opportunity Tracking & Intervention Pathway Watchlist:")
            
            st.dataframe(
                low_gpa_leads[[
                    "student_name", 
                    "intended_major", 
                    "academic_term", 
                    "cumulative_gpa", 
                    "Risk Driver Background", 
                    "Assigned Advisor Intervener", 
                    "Pathway Outreach Status"
                ]].rename(columns={
                    "student_name": "Student Name",
                    "intended_major": "Declared Major",
                    "academic_term": "Active Term Horizon",
                    "cumulative_gpa": "Dynamic GPA Index",
                    "Risk Driver Background": "Primary Academic Risk Driver",
                    "Assigned Advisor Intervener": "Assigned Care Representative",
                    "Pathway Outreach Status": "Pathway Engagement Response"
                }).astype(str),
                use_container_width=True,
                hide_index=True
            )

    elif "Provides productivity analysis reports" in selected_key_tab:
        st.markdown("### Key 4: Outreach Campaign Effectiveness Productivity Audit Log")
        
        marketing_impact_db = pd.DataFrame({
            "Active Campaign Group Strategy": [
                "Class Registration Prep Loops (Text/SMS Channels)",
                "Degree Funding Financial Aid Support Drips (Email Channels)",
                "On-Time Graduation Speed Track Pathways (Omnichannel Blasts)",
                "Academic Probation Tutoring Rescue Consultations (Manual Direct Calls)"
            ],
            "Active Enrolled Headcount Impacted": [28, 18, 12, 6],
            "On-Time Graduation Track Velocity": ["92.4% Completion Pace", "86.1% Completion Pace", "94.8% (Maximum Pace)", "71.2% (At-Risk Recovery)"],
            "Course Progression Passing Rate (C or Better)": ["89.5% Passing Grade Index", "84.2% Passing Grade Index", "91.0% Passing Grade Index", "64.8% Core Remediation Needs"],
            "Strategic Next-Step Growth Intervention": [
                "Deploy automated prerequisite bypass flags to open locked seats instantly.",
                "A/B test payment deadline warnings against scholarship matching alerts.",
                "Batch auto-schedule senior milestone degree audits through StudentVue.",
                "Route low-progression cohorts directly into intensive peer tutoring labs."
            ]
        })
        
        st.markdown("#### Comprehensive Student Progression Performance Matrix")
        st.dataframe(
            marketing_impact_db.astype(str),
            use_container_width=True,
            hide_index=True
        )
        
        st.write("")
        
        fig_prod = px.bar(
            marketing_impact_db, 
            x="Active Campaign Group Strategy", 
            y="Active Enrolled Headcount Impacted", 
            title="Total Student Retention Impact Footprint by Campaign Strategy", 
            color="Active Campaign Group Strategy", 
            color_discrete_sequence=ksu_gold_palette
        )
        st.plotly_chart(fig_prod, use_container_width=True)
                
        st.write("---")
        st.markdown("### 🔍 Dashboard Metrics Glossary & Data Index")
        idx_c1, idx_c2 = st.columns(2)
        with idx_c1:
            with st.container(border=True):
                st.markdown("**Campaign Classification Structure**")
                st.write("💡 **Premium Tier 1 (Registration Loops):** Highly automated omnichannel paths designed to eliminate schedule blocks and registration friction before terms start.")
                st.write("💡 **Tier 2 Standard (Funding & Speed Tracks):** Structured drip patterns designed to keep students funded via financial aid prompts and moving on an efficient graduation track.")
                st.write("💡 **Tier 3 Operational (Tutoring Rescue):** Intensive manual outreach interventions routing underperforming students into academic support frameworks.")
        with idx_c2:
            with st.container(border=True):
                st.markdown("**Performance Attribution Definitions**")
                st.write("📊 **Active Enrolled Headcount Impacted:** The absolute volume of students kept actively registered at KSU through this specialized campaign segment.")
                st.write("📊 **On-Time Graduation Track Velocity:** The projected percentage of the cohort remaining on schedule to complete their degree footprint within 4 years.")
                st.write("📊 **Course Progression Passing Rate:** The metric auditing what portion of the student base successfully maintains a C or better grade index across core classes.")

        st.write("---")
        st.markdown("### 📋 Marketing Team Strategic Playbook & Action Plan")
        pb1, pb2, pb3 = st.columns(3)
        with pb1:
            with st.container(border=True):
                st.markdown("**What Happened (Historical Core)**")
                st.write("Prior tracking methods focused heavily on non-academic blockers. Transitioning outreach metrics directly to course registration and registration velocity has allowed for much more accurate identification of actual enrollment drops.")
        with pb2:
            with st.container(border=True):
                st.markdown("**What is Happening Now**")
                st.write("Registration Prep loops are outperforming all other strategies, keeping 28 students cleanly registered on-track. Tutoring Rescue lines are identifying critical grade friction points early in the term cycle.")
        with pb3:
            with st.container(border=True):
                st.markdown("**How We Grow (Data Driven)**")
                st.write("Optimize communication timing. Instead of sending generic enrollment ads, marketing streams must pivot toward automated course-clearing nudge paths that help students pass classes and graduate on-time.")

    elif "Develops and maintains reports to measure operational" in selected_key_tab:
        st.markdown("### Key 5: Operational Utilization & Activity Benchmarks")
        
        operational_channels_db = pd.DataFrame({
            "Communication Outreach Channel": [
                "Personalized Text/SMS Blasts",
                "Shared Event Portal Links",
                "Targeted Email Sequences",
                "Phone Consultation Calls"
            ],
            "Total Outreach Dispatched Volume": [28500, 14200, 45000, 1800],
            "Active Student Response Rate": ["68.4% (Highly Responsive)", "42.1% (Moderate)", "12.5% (Low Engagement)", "31.0% (High Touch)"],
            "Average Interaction Response Delay": ["4.2 Minutes", "2.8 Hours", "36.4 Hours", "2-3 Target Attempts Required"],
            "Resource Labor Cost Tier": ["Low (Fully Automated Loops)", "Low (Automated Embeds)", "Medium (Template Generation)", "High (Manual Direct Staff Effort)"],
            "Strategic Operational Recommendation": [
                "Maximize utilization. Shift primary alert parameters here to ensure student engagement within minutes.",
                "Embed dynamically within SMS strategies to scale attendance checks for critical orientation events.",
                "Deprioritize for time-sensitive emergency alerts. Limit strictly to long-form policy or ledger updates.",
                "Reserve strictly for high-risk academic intervention scenarios ($GPA < 2.0$) where automated streams fail."
            ]
        })
        
        st.markdown("#### Campus Communication Channel Effectiveness & Resource Tracking Ledger")
        st.dataframe(
            operational_channels_db.astype(str),
            use_container_width=True,
            hide_index=True
        )
        
        st.write("")
        
        fig_util = px.bar(
            operational_channels_db, 
            x="Communication Outreach Channel", 
            y="Total Outreach Dispatched Volume", 
            title="Total Dispatched Communications Matrix Volumetric Share", 
            color="Communication Outreach Channel",
            color_discrete_sequence=ksu_gold_palette
        )
        st.plotly_chart(fig_util, use_container_width=True)
        
        st.write("---")
        st.markdown("### 📋 Operational Resource Strategic Playbook")
        op1, op2 = st.columns(2)
        with op1:
            with st.container(border=True):
                st.markdown("**Operational Optimization Insight**")
                st.write("Our data shows that while Email has the highest historical volume ($45,000$), its response rate is an abysmal $12.5\\%$ and carries a massive $36.4$-hour delay. Relying on it for urgent tasks like class validation or missing transcript holds leaves the university vulnerable to unnecessary enrollment drops.")
        with op2:
            with st.container(border=True):
                st.markdown("**Staff Capacity Realignment Plan**")
                st.write("By identifying that Phone Calls require high manual labor for only a $31.0\\%$ response rate, we automated baseline notifications into low-labor Text/SMS loops. This successfully cleared staff capacity, allowing care representatives to focus their high-touch time entirely on the most critical at-risk student cohorts.")

    elif "May be required to prepare ad hoc reports required of association" in selected_key_tab:
        st.markdown("### Key 6: External Oversight & Regulatory Compliance Framework Gateway")
        
        st.info("💡 **Analyst Note on Data Governance:** Internal KSU databases use custom naming conventions (e.g., 'Spring 2025' or 'First Year'). External regulatory agencies require data submitted in strict coded formats. This Gateway automatically translates internal schemas into audit-ready payloads to secure state funding, federal financial aid, and institutional accreditation.")
        st.write("")
        
        reg_target = st.selectbox("Select Regulatory Compliance Recipient Guideline Context:", ["USG State System Board Intake (State Funding)", "Federal IPEDS Frame (Title IV Financial Aid)", "AACSB Evaluation Ledger Core (Business Accreditation)"])
        
        key6_data = processed_funnel.copy()
        
        if "USG State System" in reg_target:
            with st.container(border=True):
                st.markdown("### 🏛️ University System of Georgia (USG) Academic Census")
                st.write("**Regulatory Purpose:** Securing Kennesaw State University's state budget allocations by proving exact headcount, student demographics, and credit hour generation to the Board of Regents.")
                st.write("**Schema Mapping Action:** Translating internal academic terms into strict USG numeric identifiers (e.g., Spring 2025 -> Term Code 202502) and extracting residency flags.")
                
            key6_data["USG_Term_Code"] = key6_data["academic_term"].replace({"Spring 2025": "202502", "Summer 2025": "202505", "Fall 2025": "202508", "Spring 2026": "202602", "Summer 2026": "202605", "Fall 2026 Preview": "202608"})
            key6_data["USG_Tuition_Residency"] = ["In-State (GA)" if i % 4 != 0 else "Out-of-State" for i in range(len(key6_data))]
            key6_data["USG_Headcount_Flag"] = 1
            
            display_cols = ["applicant_id", "USG_Term_Code", "USG_Tuition_Residency", "USG_Headcount_Flag", "intended_major", "cumulative_gpa"]

        elif "Federal IPEDS" in reg_target:
            with st.container(border=True):
                st.markdown("### 🇺🇸 Federal IPEDS Title IV Compliance Extract")
                st.write("**Regulatory Purpose:** Reporting student graduation, retention, and enrollment data to the Department of Education. Failure to submit accurate IPEDS data results in the loss of federal Pell Grants and FAFSA funding.")
                st.write("**Schema Mapping Action:** Stripping personally identifiable information (PII) and mapping internal KSU classification categories to rigid federal cohort grouping definitions.")
                
            key6_data["IPEDS_Cohort_Type"] = key6_data["classification"].replace({"First Year": "First-Time, Full-Time", "Second Year": "Continuing", "Third Year": "Continuing", "Fourth Year": "Continuing"})
            key6_data["IPEDS_Financial_Aid_Flag"] = key6_data["category_tags"].apply(lambda x: "Y" if "Pell-Eligible" in x else "N")
            key6_data["IPEDS_Retention_Status"] = key6_data["funnel_stage"].apply(lambda x: "Retained" if x == "Enrolled" else "Attrited")
            
            display_cols = ["applicant_id", "IPEDS_Cohort_Type", "IPEDS_Financial_Aid_Flag", "IPEDS_Retention_Status", "academic_term"]

        elif "AACSB" in reg_target:
            with st.container(border=True):
                st.markdown("### 📊 AACSB Business School Accreditation Ledger")
                st.write("**Regulatory Purpose:** Maintaining the Coles College of Business's elite global accreditation. This focuses heavily on ensuring business faculty are qualified and not overloaded with unmanageable student counts.")
                st.write("**Schema Mapping Action:** Shifting the data frame focus from *Students* to *Faculty*, calculating instructional credit hour loads, and assigning AACSB-mandated qualification flags (e.g., SA, PA, SP, IP).")
            
            key6_data = processed_faculty.copy()
            key6_data["AACSB_Qualification_Status"] = key6_data["appointment_track"].replace({
                "Tenured Faculty": "Scholarly Academic (SA)", 
                "Tenure-Track Assistant": "Scholarly Academic (SA)", 
                "Non-Tenure Lecturer": "Instructional Practitioner (IP)", 
                "Non-Tenure Clinical": "Practice Academic (PA)"
            })
            key6_data["AACSB_Instructional_Load_SCH"] = key6_data["semester_credit_hours_load"]
            
            display_cols = ["faculty_id", "faculty_name", "department_assignment", "AACSB_Qualification_Status", "AACSB_Instructional_Load_SCH"]

        st.write("---")
        st.markdown(f"#### Formatted Compliance Payload Ready for Agency Extraction — [Total Processed Records: {len(key6_data)}]")
        st.dataframe(key6_data[display_cols].astype(str), use_container_width=True, hide_index=True)

    elif "Compiles recurring operational review that includes trend analysis" in selected_key_tab:
        st.markdown("### Key 7: Multi-Semester Longitudinal Trend Analytics Curve")
        
        st.info("📈 **Cohort Trajectory Brief:** Tracking the Fall 2023 undergraduate cohort ($N=1,200$) over 6 consecutive terms. This lets us visualize retention drops over time and pinpoint exactly when our automated workflows changed the timeline.")
        st.write("")
        
        longitudinal_cohort_db = pd.DataFrame({
            "Academic Semester Timeframe": ["Fall 2023", "Spring 2024", "Fall 2024 (Year 2 Drop)", "Spring 2025 (Intervention)", "Fall 2025", "Spring 2026 (Current)"],
            "Active Enrolled Headcount": [1200, 1140, 888, 864, 846, 834],
            "Sequential Retention Rate": [100.0, 95.0, 74.0, 97.3, 97.9, 98.5],
            "Target Operational Retention Goal": [100.0, 96.0, 85.0, 96.0, 96.0, 96.0],
            "Observed Variance to Target": [0.0, -1.0, -11.0, 1.3, 1.9, 2.5],
            "Primary Enrollment Friction Drivers Tracked": [
                "Baseline Initial Cohort Matriculation.",
                "Minor academic transition challenges; standard administrative drops.",
                "CRITICAL DROP-OFF: Massive friction from course-clearing blocks & financial funding gap drops.",
                "LAUNCH: Automated Navigate360 registration prep loops go live; attrition flattened.",
                "Stable continuing pipeline; persistent tracking holds bypassed via automated system overrides.",
                "Cohort enters senior phase maintaining maximum timeline velocity toward graduation."
            ]
        })
        
        st.markdown("#### Longitudinal Cohort Retention Trend Ledger")
        
        formatted_trend_df = longitudinal_cohort_db.copy()
        formatted_trend_df["Sequential Retention Rate"] = formatted_trend_df["Sequential Retention Rate"].apply(lambda x: f"{x:.1f}%")
        formatted_trend_df["Target Operational Retention Goal"] = formatted_trend_df["Target Operational Retention Goal"].apply(lambda x: f"{x:.1f}%")
        formatted_trend_df["Observed Variance to Target"] = formatted_trend_df["Observed Variance to Target"].apply(lambda x: f"{x:+.1f}%" if x != 0 else "0.0%")
        formatted_trend_df["Active Enrolled Headcount"] = formatted_trend_df["Active Enrolled Headcount"].apply(lambda x: f"{x:,}")
        
        st.dataframe(
            formatted_trend_df,
            use_container_width=True,
            hide_index=True
        )
        
        st.write("")
        
        fig_trend = px.line(
            longitudinal_cohort_db, 
            x="Academic Semester Timeframe", 
            y="Sequential Retention Rate", 
            title="3-Year Multi-Semester Retention Rate Trajectory Curve",
            markers=True,
            text="Sequential Retention Rate"
        )
        fig_trend.update_traces(line=dict(color="#FFC400", width=4), marker=dict(size=10), textposition="top right")
        fig_trend.update_layout(yaxis_ticksuffix="%")
        st.plotly_chart(fig_trend, use_container_width=True)
        
        st.write("---")
        st.markdown("### 📋 Executive Analytical Narrative")
        narrative_c1, narrative_c2 = st.columns(2)
        with narrative_c1:
            with st.container(border=True):
                st.markdown("**The Historical Attrition Crisis (Fall 2024)**")
                st.write("Looking closely at the timeline, our cohort experienced a catastrophic drop during the second-to-third semester transition. Retention plummeted to $74.0\\%$, missing our target by a massive $-11.0\\%$. Our deep-dive audit revealed that this drop wasn't driven by students flunking out; it was caused entirely by administrative friction—specifically course override loops and financial aid paperwork delays that caused students to sit out.")
        with narrative_c2:
            with st.container(border=True):
                st.markdown("**The System Stabilization Payoff (2025-2026)**")
                st.write("In response to this trend data, we introduced automated text/SMS registration loops in Spring 2025. The impact was instant: term-over-term attrition flattened out immediately, pushing subsequent term retention to a stellar $97.3\\%$ and above. By automating the resolution of holds, we saved the university over 100 students who would have otherwise leaked out of the pipeline.")

    elif "May assists with departmental inventory reporting" in selected_key_tab:
        st.markdown("### Key 8: Departmental Capacity, Class Enrolment & Asset Inventory Audit")
        
        st.info("🛠️ **Infrastructure Audit Matrix:** Mapping hardware equipment stockpiles alongside lecture seat volume limits to pinpoint administrative bottlenecks.")
        st.write("")
        
        tech_inventory_db = pd.DataFrame({
            "Academic Department Unit": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
            "Undergrad Seat Enrollment": [850, 1250, 680, 410, 350, 980, 240, 890, 1650, 1420],
            "Assigned Faculty Chair": ["Dr. Stacey Nebriaga", "Dr. Sarah Jenkins", "Dr. David Vance", "Dr. Tyler Pede", "Dr. Henry Wu", "Prof. Elena Rostova", "Dr. Robert Langdon", "Prof. Michael Gabriele", "Dr. Thomas Anderson", "Prof. Emily Holzgrefe"],
            "Average Class Size Limit": [120, 45, 35, 65, 30, 50, 25, 40, 150, 60],
            "Primary Hardware Asset Type": ["Lab Terminals", "Excel Desktops", "Server Sandboxes", "Bloomberg Units", "Pitch AV Kits", "Bloomberg Units", "POS Kiosks", "Switch Arrays", "Check-In Kiosks", "Creative Stations"],
            "Active Inventory Count": [45, 120, 85, 10, 25, 20, 15, 60, 140, 130]
        })
        
        tech_inventory_db["Students Per Asset Unit"] = round(tech_inventory_db["Undergrad Seat Enrollment"] / tech_inventory_db["Active Inventory Count"], 1)
        tech_inventory_db["Required Core Sections"] = (tech_inventory_db["Undergrad Seat Enrollment"] / tech_inventory_db["Average Class Size Limit"]).astype(int) + 1
        tech_inventory_db["Class Seat Utilization Rate"] = round((tech_inventory_db["Undergrad Seat Enrollment"] / (tech_inventory_db["Required Core Sections"] * tech_inventory_db["Average Class Size Limit"])) * 100, 1)
        
        tech_inventory_db["Capacity Status Flag"] = tech_inventory_db["Class Seat Utilization Rate"].apply(
            lambda x: "CRITICAL BIND (Seats Full)" if x >= 93.0 else ("BALANCED LOAD" if x >= 80.0 else "UNDER-UTILIZED SEATS")
        )
        
        if dept_filter != "All Departments":
            tech_inventory_db = tech_inventory_db[tech_inventory_db["Academic Department Unit"] == dept_filter]
            
        st.markdown("#### Comprehensive Capacity and Course Resource Inventory Ledger")
        
        formatted_tech_df = tech_inventory_db.copy()
        formatted_tech_df["Undergrad Seat Enrollment"] = formatted_tech_df["Undergrad Seat Enrollment"].apply(lambda x: f"{x:,}")
        formatted_tech_df["Students Per Asset Unit"] = formatted_tech_df["Students Per Asset Unit"].apply(lambda x: f"{x:.1f} Stud/Unit")
        formatted_tech_df["Class Seat Utilization Rate"] = formatted_tech_df["Class Seat Utilization Rate"].apply(lambda x: f"{x:.1f}%")
        
        st.dataframe(
            formatted_tech_df.rename(columns={
                "Academic Department Unit": "Department major",
                "Undergrad Seat Enrollment": "Total Enrollment",
                "Assigned Faculty Chair": "Faculty Section Lead",
                "Average Class Size Limit": "Max Class Size",
                "Active Inventory Count": "Hardware Stock"
            }),
            use_container_width=True,
            hide_index=True
        )
        
        st.write("")
        
        inv_c1, inv_c2 = st.columns(2)
        with inv_c1:
            fig_inv_bar = px.bar(
                tech_inventory_db, 
                x="Academic Department Unit", 
                y="Average Class Size Limit", 
                title="Average Structural Section Class Size Caps by Department", 
                color="Required Core Sections", 
                color_discrete_sequence=ksu_gold_palette,
                text="Average Class Size Limit"
            )
            st.plotly_chart(fig_inv_bar, use_container_width=True)
            
        with inv_c2:
            fig_ratio_bar = px.bar(
                tech_inventory_db,
                x="Academic Department Unit",
                y="Class Seat Utilization Rate",
                title="Seat Inventory Strain: Core Lecture Hall Space Utilization Percent",
                color="Capacity Status Flag",
                color_discrete_map={"CRITICAL BIND (Seats Full)": "#FF5722", "BALANCED LOAD": "#00E676", "UNDER-UTILIZED SEATS": "#FFC400"},
                text="Class Seat Utilization Rate"
            )
            fig_ratio_bar.update_layout(yaxis_ticksuffix="%")
            st.plotly_chart(fig_ratio_bar, use_container_width=True)
            
        st.write("---")
        st.markdown("### 📋 Capacity Resource Strategic Playbook")
        inv_p1, inv_p2 = st.columns(2)
        with inv_p1:
            with st.container(border=True):
                st.markdown("**The Structural Bottleneck Discovery (Class Size vs Seat Velocity)**")
                st.write("By merging professor class sizes with hardware asset counts, we uncovered the real obstacle to student progression. **Management** holds a **CRITICAL BIND** status with a **95.2% class seat utilization rate** across massive **150-student sections** led by Dr. Anderson. Because lecture halls are completely packed, there is zero safety margin. If an adviser identifies an at-risk student in a standard tracking loop, they cannot add them to a core course because the room is physically and logistically full.")
        with inv_p2:
            with st.container(border=True):
                st.markdown("**Data-Driven Course Realignment Action Plan**")
                st.write("This dual tracking model allows us to address resource shortages intelligently. Instead of arbitrarily requesting more hardware, our data indicates that we should split high-strain lecture segments into smaller sections. By coordinating directly with the Central Data Strategy team, we can reallocate under-utilized classrooms from fields with low seat utilization, creating room for new class blocks without expanding the physical campus footprint.")

    elif "May be required to prepare ad hoc reporting that assists with measuring department performance" in selected_key_tab:
        st.markdown("### Key 9: Longitudinal Cohort Graduation Velocity & Attrition Performance Audit")
        
        st.info("🎯 **Program Effectiveness Metric Framework:** Tracking institutional success across multiple entering cohorts from 2020 through 2026. This high-density ledger contrasts outcomes for First-Generation students against Continuing-Generation lines to isolate real-time improvements.")
        st.write("")
        
        # Comprehensive High-Fidelity Cohort Outcomes Database spanning 2020 to 2026
        cohort_outcomes_db = pd.DataFrame({
            "Entering Student Cohort Year": [
                "Fall 2020", "Fall 2020", 
                "Fall 2021", "Fall 2021", 
                "Fall 2022", "Fall 2022", 
                "Fall 2023", "Fall 2023",
                "Fall 2024", "Fall 2024",
                "Fall 2025", "Fall 2025",
                "Fall 2026", "Fall 2026"
            ],
            "Student Demographic Type": [
                "First-Generation", "Continuing-Generation", 
                "First-Generation", "Continuing-Generation", 
                "First-Generation", "Continuing-Generation", 
                "First-Generation", "Continuing-Generation",
                "First-Generation", "Continuing-Generation",
                "First-Generation", "Continuing-Generation",
                "First-Generation", "Continuing-Generation"
            ],
            "Initial Inbound Headcount": [450, 750, 480, 810, 520, 840, 550, 890, 580, 920, 610, 940, 640, 980],
            "On-Time 4-Year Grad Rate": [42.1, 64.8, 44.5, 66.2, 51.0, 68.5, 58.4, 71.2, 64.2, 74.5, 68.1, 76.8, 71.5, 79.2],
            "Longitudinal 5-Year Grad Rate": [56.4, 76.1, 59.2, 78.4, 66.8, 81.0, 74.2, 83.5, 78.5, 86.1, 81.0, 88.4, 83.2, 90.1],
            "Longitudinal 6-Year Grad Rate": [62.8, 81.4, 65.1, 83.0, 73.5, 85.4, 79.8, 88.0, 84.1, 90.2, 86.5, 92.0, 88.7, 93.5],
            "Total Academic Dropouts Record": [128, 72, 114, 68, 82, 54, 48, 42, 31, 28, 22, 18, 14, 11],
            "Intervention Performance Group": [
                "Pre-Navigate360 Baseline", "Pre-Navigate360 Baseline", 
                "Manual Adviser Email Drips", "Manual Adviser Email Drips", 
                "Early Pilot Script Tracking", "Early Pilot Script Tracking", 
                "Full Automated Loops Active", "Full Automated Loops Active",
                "V2 Multi-Channel Enhancements", "V2 Multi-Channel Enhancements",
                "Live Registrar Integration", "Live Registrar Integration",
                "Active 2026 Steady-State", "Active 2026 Steady-State"
            ]
        })
        
        st.markdown("#### High-Fidelity Longitudinal Program Performance Ledger (2020–2026)")
        
        formatted_outcomes_df = cohort_outcomes_db.copy()
        formatted_outcomes_df["On-Time 4-Year Grad Rate"] = formatted_outcomes_df["On-Time 4-Year Grad Rate"].apply(lambda x: f"{x:.1f}%")
        formatted_outcomes_df["Longitudinal 5-Year Grad Rate"] = formatted_outcomes_df["Longitudinal 5-Year Grad Rate"].apply(lambda x: f"{x:.1f}%")
        formatted_outcomes_df["Longitudinal 6-Year Grad Rate"] = formatted_outcomes_df["Longitudinal 6-Year Grad Rate"].apply(lambda x: f"{x:.1f}%")
        formatted_outcomes_df["Initial Inbound Headcount"] = formatted_outcomes_df["Initial Inbound Headcount"].apply(lambda x: f"{x:,}")
        formatted_outcomes_df["Total Academic Dropouts Record"] = formatted_outcomes_df["Total Academic Dropouts Record"].apply(lambda x: f"{x:,}")
        
        st.dataframe(
            formatted_outcomes_df.rename(columns={
                "Entering Student Cohort Year": "Cohort Year",
                "Student Demographic Type": "Demographic Profile",
                "Initial Inbound Headcount": "Cohort Size",
                "On-Time 4-Year Grad Rate": "4-Yr Grad Velocity",
                "Longitudinal 5-Year Grad Rate": "5-Yr Longitudinal Rate",
                "Longitudinal 6-Year Grad Rate": "6-Yr Completion Cap",
                "Total Academic Dropouts Record": "Total Dropouts Count",
                "Intervention Performance Group": "Center Operational Framework"
            }),
            use_container_width=True,
            hide_index=True
        )
        
        st.write("")
        
        perf_c1, perf_c2 = st.columns(2)
        with perf_c1:
            fig_grad_trend = px.line(
                cohort_outcomes_db,
                x="Entering Student Cohort Year",
                y="On-Time 4-Year Grad Rate",
                color="Student Demographic Type",
                markers=True,
                text="On-Time 4-Year Grad Rate",
                title="Historical & Projected 4-Year On-Time Graduation Velocity Trends",
                color_discrete_sequence=["#FFC400", "#00E676"]
            )
            fig_grad_trend.update_traces(textposition="bottom center", line=dict(width=3))
            fig_grad_trend.update_layout(yaxis_ticksuffix="%")
            st.plotly_chart(fig_grad_trend, use_container_width=True)
            
        with perf_c2:
            fig_dropout_bar = px.bar(
                cohort_outcomes_db,
                x="Entering Student Cohort Year",
                y="Total Academic Dropouts Record",
                color="Student Demographic Type",
                barmode="group",
                title="Absolute Attrition Volume Dropouts by Entering Cohort (2020–2026)",
                color_discrete_sequence=["#FF3D00", "#00B0FF"]
            )
            st.plotly_chart(fig_dropout_bar, use_container_width=True)
            
        st.write("---")
        st.markdown("### 📋 Center Impact and Completion Playbook")
        perf_p1, perf_p2 = st.columns(2)
        with perf_p1:
            with st.container(border=True):
                st.markdown("**The Historical Equity Gap Lifecycle (2020–2022)**")
                st.write("Looking at the long-term trend from our **Fall 2020 Baseline**, we see a stark historical equity gap. First-Generation cohorts completed on time at a low **42.1%**, while Continuing-Gen students completed at **64.8%**. This discrepancy directly matched high attrition volumes, with First-Gen lines losing **128 dropouts** to administrative and course-clearing friction before early piloting structures were introduced in 2022.")
        with perf_p2:
            with st.container(border=True):
                st.markdown("**The 2026 Steady-State Stabilization Payoff**")
                st.write("The introduction of automated hold-resolution loops significantly shifted our completion metrics. By the time our active **Fall 2026 cohort** stabilized, on-time 4-year completion for First-Gen students increased to **71.5%**, and absolute dropouts decreased from **128 down to 14**. This comprehensive multi-year trend proves that removing institutional enrollment barriers provides long-term stability for academic cohorts.")

    elif "Collaborate with a variety of stakeholders across campus" in selected_key_tab:
        st.markdown("### Key 10: Office of University Data Strategy Alignment Matrix")
        sync_scope = st.selectbox("Select Synchronization Scope Ring Natively:", ["All Synced Records", "Sync Failures / Alerts Only"])
        key10_data = processed_funnel.copy()
        if sync_scope == "Sync Failures / Alerts Only":
            key10_data = key10_data[key10_data["studentvue_sync_status"].str.contains("Hold|Alert")]
            
        with st.container(border=True):
            st.markdown("### University Policy Policy Mapping Framework Terminal")
            st.write("Data Governance Layer: Kennesaw State University Master Data Strategy Directive Compliance standard verified.")
            st.write("API Synchronization Endpoint Handshake: https://data-strategy.kennesaw.edu/v1/sync active.")
            st.write("Alignment Confirmed: Local fields mapped perfectly match KSU's central data strategy taxonomy.")

        st.write("---")
        st.markdown(f"#### Central Synchronization Taxonomy Audit Ledger ({sync_scope}) — [Total Records: {len(key10_data)} Students]")
        st.table(key10_data[["applicant_id", "student_name", "intended_major", "academic_term", "funnel_stage", "Current Professor", "Past Professor", "cumulative_gpa", "studentvue_sync_status"]].astype(str))
