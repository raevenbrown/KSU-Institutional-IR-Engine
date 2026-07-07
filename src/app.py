import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Coles Navigate360 System Console", layout="wide")

# ==========================================
# CENTRALIZED REALISTIC NAVIGATE360 STUDENT BASE
# ==========================================

if "navigate_students_db" not in st.session_state:
    st.session_state.navigate_students_db = pd.DataFrame({
        "student_id": ["87650214", "04218579", "14538206", "46581097", "94753108", "81295374", "JIH339188", "JIH884120", "JIH662199", "JIH551043"],
        "student_name": ["Michael Adam", "Nancy Aguas", "Peggy Aguila", "Margaret Aldrege", "James Alexander", "Nathan Amador", "Chloe Bennett", "David Kim", "Taylor Brooks", "Maya Patel"],
        "student_major": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "classification": ["Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "First Year", "Fourth Year", "Third Year", "Second Year", "Fourth Year"],
        "transfer_student": ["No", "No", "Yes", "No", "No", "Yes", "No", "No", "No", "No"],
        "gpa_df_count": [2, 0, 1, 0, 2, 0, 0, 1, 0, 0],
        "repeated_courses": [1, 0, 0, 0, 2, 0, 0, 0, 1, 0],
        "withdrawn_courses": [0, 0, 0, 1, 3, 0, 0, 0, 1, 0],
        "missed_markers": [3, 0, 1, 0, 4, 0, 0, 2, 0, 0],
        "cumulative_gpa": [2.85, 3.31, 2.45, 3.82, 1.95, 2.88, 3.12, 2.15, 3.64, 3.22],
        "total_credits_earned": [27.0, 51.0, 18.0, 94.0, 72.0, 45.0, 14.0, 112.0, 88.0, 62.0],
        "credit_completion_pct": [90, 100, 85, 96, 64, 100, 100, 78, 92, 100],
        "predicted_support_level": ["High Risk", "Low Risk", "Medium Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk"],
        "category_tags": [
            "Completed probation requirement, Financial Aid, First generation student, Full-Time, Pre-enrollment risk, Study group member",
            "Adult learner, Full-Time",
            "Completed probation requirement, Financial Aid, First generation student, Full-Time, Pre-enrollment risk, Study group member",
            "Active holds, Transfer student",
            "Completed probation requirement, Financial Aid, First generation student, Full-Time, Good Academic Standing, Honors student, Pell-Eligible, Pre-enrollment risk, Re-enrollment grant recipient, Sports In-Season, Study group member, Transfer-Intending, TRIO Success",
            "Pell-Eligible, Financial Aid, First generation student, Full-Time",
            "First generation student, Full-Time",
            "Pell-Eligible, Financial Aid, Study group member",
            "Good Academic Standing, Honors student, Full-Time",
            "Pell-Eligible, Active holds"
        ],
        "appointment_care_unit": ["Academic Advising", "Academic Advising", "Academic Advising", "Career Coaching", "Internship & Co-op Advising", "Academic Advising", "Student Engagement", "Academic Advising", "Career Coaching", "Academic Advising"],
        "assigned_staff_owner": ["Beth Allen", "Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe", "Sarah Jenkins", "Stacey Nebriaga", "Tyler Pede", "Michael Gabriele"],
        "reason_category": ["Course Performance Concerns", "Graduation Check", "Registration Auth", "Resume Polish", "Co-op Sign-off", "Prerequisite Check", "Leadership Intake", "Course Override", "Career Fair Prep", "Change of Major"],
        "case_status": ["Open", "Open", "In Progress", "Open", "Open", "Resolved", "Open", "In Progress", "Open", "Resolved"],
        "appointment_summary_report": ["James was missing class because of a part-time job. Connected him with financial aid. Recommended tutoring.", "", "Reviewing transfer credits from state college.", "", "", "Cleared registration holds.", "", "Processing course override codes.", "", "Forms processed."]
    })

# Persistent Session State 2: Advisor Availability Shift Ledger
if "advisor_availability_db" not in st.session_state:
    st.session_state.advisor_availability_db = pd.DataFrame({
        "days_of_week": ["Mon, Wed, Fri", "Mon", "Mon", "Fri", "Fri", "Tue, Wed, Thu"],
        "times": ["8:00am - 5:00pm ET", "9:00am - 5:30pm ET", "9:00am - 5:30pm ET", "9:00am - 4:30pm ET", "9:00am - 4:30pm ET", "8:00am - 4:00pm ET"],
        "dates": ["Fall 2026", "Forever", "Forever", "Forever", "Forever", "Forever"],
        "location": ["Advising Center", "One Stop Student Services", "Advising Center", "Financial Aid Center", "Advising Center", "Advising Center"],
        "purpose": ["Academic Planning for Appointments/Drop-Ins/Campaigns", "BIO-101, Course-based Tutoring", "Academic Planning, Changing a Major, General Advising", "Applying for Financial Aid", "Academic Planning, Changing a Major, General Advising", "Academic Planning, Changing a Major, General Advising"],
        "care_unit": ["Advising", "Tutoring", "Advising", "Financial Aid", "Advising", "Advising"],
        "personal_link": ["No", "No", "Yes", "No", "No", "No"],
        "meeting_type": ["In-person, Video (Zoom)", "In-person", "WhatsApp Video Call", "In-person", "In-person", "WhatsApp Video Call"]
    })

# Master Coles Capacity Reference Frame
if "coles_capacity_db" not in st.session_state:
    st.session_state.coles_capacity_db = pd.DataFrame({
        "major_name": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "undergrad_seat_count": [850, 1250, 680, 410, 350, 980, 240, 890, 1650, 1420],
        "semester_credit_hours": [12400, 18400, 9100, 5200, 4800, 24500, 3100, 9400, 19800, 14200],
        "retention_goal_pct": [84.0, 85.0, 88.0, 80.0, 82.0, 82.0, 80.0, 88.0, 80.0, 85.0],
        "actual_retention_pct": [81.2, 82.4, 86.7, 79.1, 81.5, 76.8, 80.2, 89.5, 74.2, 81.1]
    })

ksu_gold_palette = ["#FFC400", "#FFA000", "#FF8F00", "#FF6F00", "#FF5722", "#E65100", "#4E5D6C", "#161B22"]

# ==========================================
# NAVIGATE360 NATIVE FILTER SIDEBAR SYSTEM
# ==========================================
st.sidebar.title("🛡️ Navigate360 Core")
st.sidebar.markdown("**User Access Role:** `Advisor Terminal Suite`")
st.sidebar.write("---")

st.sidebar.subheader("🔍 Filters Panel")
major_filter = st.sidebar.selectbox("Filter Enrollment Major Context:", options=["All majors"] + list(st.session_state.coles_capacity_db["major_name"].unique()))
class_filter = st.sidebar.selectbox("Filter Classification Level:", options=["All classifications", "First Year", "Second Year", "Third Year", "Fourth Year"])

processed_df = st.session_state.navigate_students_db.copy()
if major_filter != "All majors":
    processed_df = processed_df[processed_df["student_major"] == major_filter]
if class_filter != "All classifications":
    processed_df = processed_df[processed_df["classification"] == class_filter]

st.sidebar.write("---")
st.sidebar.subheader("🏁 Navigation Modules")
app_panel = st.sidebar.radio("Select View Desk:", ["📋 Staff Home: Student Profile Inspector", "📅 Scheduling Desk & Availability Manager", "📊 Population Health Dashboard"])

# ==========================================
# MODULE 1: STAFF HOME — STUDENT INSPECTOR
# ==========================================
if app_panel == "📋 Staff Home: Student Profile Inspector":
    main_workspace, ai_sidebar_col = st.columns([3, 1])
    
    with main_workspace:
        st.markdown("## 📋 Staff Home — Student Profile Inspector")
        st.write("---")
        
        if len(processed_df) > 0:
            selected_student_name = st.selectbox("👤 Select Student Profile File to Inspect:", options=list(processed_df["student_name"].unique()))
            
            # FIXED: Safe explicit condition matching instead of fragile shared-index indexer lookup matrix tracking
            master_match = st.session_state.navigate_students_db[st.session_state.navigate_students_db["student_name"] == selected_student_name]
            idx = master_match.index[0]
            s_row = master_match.loc[idx]
            
            with st.container(border=True):
                st.markdown(f"### Student File: **{s_row['student_name']}** | ID: `{s_row['student_id']}`")
                st.write("")
                kpi_c1, kpi_c2, kpi_c3, kpi_c4 = st.columns(4)
                with kpi_c1: 
                    st.metric("Course Grade D/F", value=int(s_row["gpa_df_count"]))
                    st.metric("Cumulative GPA", value=f"{s_row['cumulative_gpa']:.2f}")
                with kpi_c2: 
                    st.metric("Repeated Courses", value=int(s_row["repeated_courses"]))
                    st.metric("Total Credits Earned", value=f"{s_row['total_credits_earned']:.1f}")
                with kpi_c3: 
                    st.metric("Withdrawn Courses", value=int(s_row["withdrawn_courses"]))
                    st.metric("Credit Completion Ratio", value=f"{s_row['credit_completion_pct']}%")
                with kpi_c4: 
                    st.metric("Missed Success Markers", value=int(s_row["missed_markers"]))
                    st.metric("Predicted Support Level", value=s_row["predicted_support_level"])
            
            st.write("")
            st.subheader("📋 Profile Institutional Category Tags & Background Parameters")
            with st.container(border=True):
                st.markdown(f"**🏷️ System Category Tags:** `{s_row['category_tags']}`")
                st.write("---")
                det_c1, det_c2 = st.columns(2)
                with det_c1:
                    st.markdown(f"**Academic Concentration Major:** `{s_row['student_major']}`")
                    st.markdown(f"**Classification Cohort Track:** `{s_row['classification']}`")
                with det_c2:
                    st.markdown(f"**Assigned Staff Core Owner:** `{s_row['assigned_staff_owner']}`")
                    st.markdown(f"**Current Care Reason Category:** `{s_row['reason_category']}`")
                    
            st.write("")
            st.subheader("📥 Appointment Summary Report & Historic Case Logs")
            with st.container(border=True):
                st.markdown(f"*\"{s_row['appointment_summary_report'] if s_row['appointment_summary_report'] else 'No summary reports recorded.'}\"*")
                
            st.write("---")
            st.subheader("🛠️ Advisor Database Field Modification Console")
            w_in1, w_in2, w_in3 = st.columns([1, 1, 2])
            with w_in1:
                state_update = st.selectbox("Update Case Status Field:", options=["Open", "In Progress", "Resolved"])
            with w_in2:
                staff_update = st.selectbox("Modify Staff Owner Assignment:", options=["Beth Allen", "Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", "Emily Holzgrefe"])
            with w_in3:
                note_add = st.text_input("Append Text Entry to Appointment Summary Notes:")
                
            if st.button("🚀 Commit Workflow Modification to System Pipelines", use_container_width=True):
                st.session_state.navigate_students_db.at[idx, "case_status"] = state_update
                st.session_state.navigate_students_db.at[idx, "assigned_staff_owner"] = staff_update
                if note_add:
                    st.session_state.navigate_students_db.at[idx, "appointment_summary_report"] = f"{s_row['appointment_summary_report']} | {note_add}".strip(" | ")
                st.success("Operational changes logged successfully to backend tables!")
                st.rerun()
        else:
            st.warning("No records match the active filtering parameters inside the left panel configuration.")
            
        st.write("---")
        st.subheader("📋 Full Filtered Caseload Ingestion Matrix View")
        st.dataframe(processed_df[["student_id", "student_name", "student_major", "cumulative_gpa", "category_tags"]], use_container_width=True, hide_index=True)

    with ai_sidebar_col = ai_sidebar_col, st.container():
        st.markdown("### 🤖 Navigate AI Assistant")
        st.caption("EAB Responsible Higher-Ed Model Active")
        st.write("---")
        if len(processed_df) > 0 and 's_row' in locals():
            st.markdown("##### ⚡ **Dynamic Briefing Session Notes:**")
            with st.container(border=True):
                st.markdown(f"**Target Focus:** `{s_row['student_name']}`")
                st.write(f"* **Current Risk Factor:** {s_row['predicted_support_level']}")
                st.write(f"* **Touchpoint Summary:** {s_row['reason_category']}")
        st.write("")
        st.markdown("##### ⚙️ **Quick Macro Prompts:**")
        st.button("🎯 Create an Action Campaign", use_container_width=True)
        st.button("📋 Help Me Prep for Appointment", use_container_width=True)
        st.write("---")
        ai_prompt_input = st.text_input("💬 Ask the System AI Data Finder:")
        if ai_prompt_input:
            p_lower = ai_prompt_input.lower()
            with st.container(border=True):
                if "risk" in p_lower or "alert" in p_lower:
                    risk_subset = st.session_state.navigate_students_db[st.session_state.navigate_students_db["predicted_support_level"] == "High Risk"]
                    st.error(f"Isolated {len(risk_subset)} high-risk files:")
                    st.dataframe(risk_subset[["student_name", "student_major", "cumulative_gpa"]], hide_index=True)
                elif "michael" in p_lower or "adam" in p_lower:
                    st.success("Profile Summary: Michael Adam is a Second Year Biology major with 2 D/F marks and 3 missed success markers. He has active probation requirements logged.")
                else:
                    st.info(f"System Baseline: Directory contains {len(st.session_state.navigate_students_db)} active records. System mean GPA: {st.session_state.navigate_students_db['cumulative_gpa'].mean():.2f}")

# ==========================================
# MODULE 2: SCHEDULING DESK & AVAILABILITY MANAGER
# ==========================================
elif app_panel == "📅 Scheduling Desk & Availability Manager":
    st.header("📅 Scheduling Desk & Staff Availability Manager")
    st.write("---")
    
    tab_avail, tab_book = st.tabs(["🔒 My Availability Configuration Terminal", "🤝 Multi-Criteria Appointment Booking Engine"])
    
    with tab_avail:
        st.subheader("Available Consulting Times Matrix")
        st.dataframe(st.session_state.advisor_availability_db, use_container_width=True, hide_index=True)
        st.write("---")
        
        st.markdown("#### ⚙️ Append New Availability Constraint Block")
        with st.form("availability_form", clear_on_submit=True):
            av_col1, av_col2, av_col3 = st.columns(3)
            with av_col1:
                av_days = st.text_input("Days of Week Configuration:", value="Mon, Wed, Fri")
                av_times = st.text_input("Active Target Time Block Hours:", value="8:00am - 5:00pm ET")
            with av_col2:
                av_loc = st.selectbox("Explicit Physical Location Suite:", options=["Advising Center", "One Stop Student Services Center", "Financial Aid Center"])
                av_unit = st.selectbox("Care Unit Sector Category:", options=["Advising", "Tutoring", "Financial Aid"])
            with av_col3:
                av_purp = st.text_input("Authorized Consulting Purpose:", value="Academic Planning, General Advising")
                av_mtype = st.selectbox("Meeting Type Transmission Format:", options=["In-person", "In-person, Video (Zoom)", "WhatsApp Video Call"])
                
            if st.form_submit_button("🚀 Inject Availability Block Into Active Matrix"):
                new_avail_row = pd.DataFrame({
                    "days_of_week": [av_days], "times": [av_times], "dates": ["Fall 2026"],
                    "location": [av_loc], "purpose": [av_purp], "care_unit": [av_unit],
                    "personal_link": ["No"], "meeting_type": [av_mtype]
                })
                st.session_state.advisor_availability_db = pd.concat([st.session_state.advisor_availability_db, new_avail_row], ignore_index=True)
                st.success("Authorized schedule modification applied successfully!")
                st.rerun()

    with tab_book:
        st.subheader("Schedule Interactive Appointment Form")
        book_left, book_right = st.columns([1, 2])
        
        with book_left:
            st.markdown("##### **1. Selection Filters**")
            b_unit = st.selectbox("Care Unit Target:", options=["Advising", "Tutoring", "Financial Aid"])
            b_loc = st.selectbox("Location Target Suite:", options=["Advising Center", "One Stop Student Services Center", "Financial Aid Center"])
            b_serv = st.selectbox("Service Classification Purpose:", options=["Academic Planning", "Course-based Tutoring", "Change of Major Intake", "Financial Aid Check"])
            b_mtype = st.selectbox("Meeting Type Format Option:", options=["In-person", "Video (Zoom)", "WhatsApp Video Call"])
            b_date = st.date_input("Select Appointment Target Date Milestone:", value=date(2026, 9, 1))
            
        with book_right:
            st.markdown("##### **2. Select An Organizer (Staff Resource Directory List)**")
            organizer_df = pd.DataFrame({
                "Select": [False, False, False, False],
                "Organizer Staff Name": ["Beth Allen", "Jack Wheeler", "Jack Whitmore", "Jack Whitten"],
                "Available Ingress Reference Windows Times": [
                    "For: Appointments/Drop-Ins/Campaigns Mon-Fri 12:00pm - 5:00pm ET",
                    "For: Appointments/Drop-Ins/Campaigns Mon 9:00am - 5:30pm ET",
                    "For: Appointments/Drop-Ins/Campaigns Mon, Wed, Fri 8:00am - 5:00pm ET (Fall 2026)",
                    "For: Appointments/Drop-Ins/Campaigns Fri 9:00am - 4:30pm ET"
                ]
            })
            st.data_editor(organizer_df, use_container_width=True, hide_index=True)
            
            st.write("---")
            st.markdown("##### **3. Choose A Grid Time Slot Matrix Allocation**")
            time_slots_data = pd.DataFrame({
                "Time Slot Windows": ["12:00pm - 12:45pm ET", "12:45pm - 1:30pm ET", "1:30pm - 2:15pm ET", "2:15pm - 3:00pm ET", "3:00pm - 3:45pm ET"],
                "08/31 (SUN)": ["DROP-IN", "DROP-IN", "DROP-IN", "DROP-IN", "DROP-IN"],
                "09/01 (MON)": ["DROP-IN", "DROP-IN", "DROP-IN", "DROP-IN", "DROP-IN"],
                "09/02 (TUE)": ["0/1 Available", "0/1 Available", "0/1 Available", "✅ Select Slot", "0/1 Available"]
            })
            st.dataframe(time_slots_data, use_container_width=True, hide_index=True)
            
            if st.button("💾 Save Finalized Appointment Frame to Navigate Core Schema Pipeline", use_container_width=True):
                st.success(f"Appointment processed for target date matching {b_date} under {b_serv} processing tracks!")

# ==========================================
# MODULE 3: POPULATION HEALTH ANALYTICS
# ==========================================
elif app_panel == "📊 Population Health Dashboard":
    st.header("📊 Population Health Dashboard & Resource Analytics")
    st.write("---")
    
    display_metrics = st.session_state.coles_capacity_db.copy()
    if major_filter != "All majors":
        display_metrics = display_metrics[display_metrics["major_name"] == major_filter]
        
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        fig_ret = px.bar(display_metrics, x="major_name", y=["retention_goal_pct", "actual_retention_pct"],
                         title="Retention Matrix Analysis: Coles Goals vs. Actual Proportions", barmode="group",
                         color_discrete_sequence=["#FFC400", "#161B22"])
        st.plotly_chart(fig_ret, use_container_width=True)
    with g_col2:
        fig_seats = px.pie(display_metrics, values="undergrad_seat_count", names="major_name", hole=0.4,
                           title="Enrollment Metric Distribution Shares", color_discrete_sequence=ksu_gold_palette)
        st.plotly_chart(fig_seats, use_container_width=True)
