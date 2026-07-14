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
    # Robust construction to ensure all arrays are exactly 40 in length
    data = {
        "applicant_id": [f"APP-{2600+i}" for i in range(1, 41)],
        "student_name": [f"Student {i}" for i in range(1, 41)],
        "intended_major": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"] * 4,
        "academic_term": ["Spring 2026", "Summer 2026", "Fall 2026 Preview", "Spring 2026"] * 10,
        "classification": ["Second Year", "First Year", "Fourth Year", "Third Year"] * 10,
        "cumulative_gpa": [3.5] * 40,
        "studentvue_sync_status": ["Good Standing - Regular Sync"] * 40,
        "funnel_stage": ["Enrolled", "Admitted", "Applied", "Inquiry"] * 10,
        "outreach_campaign_group": ["Completed Yield"] * 40,
        "predicted_yield_probability": ["High"] * 40,
        "last_interaction_date": ["2026-03-10"] * 40,
        "to_dos_pending": [1] * 40,
        "communication_preference": ["Email"] * 40,
        "category_tags": ["Good Academic Standing"] * 40,
        "staff_meeting_prep_notes": [f"Record update {i}" for i in range(1, 41)]
    }
    st.session_state.enrollment_funnel_db = pd.DataFrame(data)

if "faculty_retention_db" not in st.session_state:
    st.session_state.faculty_retention_db = pd.DataFrame({
        "faculty_name": ["Dr. Smith", "Prof. Jones"] * 10,
        "department_assignment": ["Biology", "Accounting"] * 10,
        "appointment_track": ["Tenured"] * 20,
        "faculty_staff_status": ["Active"] * 20,
        "tenure_years_at_institution": [5.0] * 20,
        "semester_credit_hours_load": [400] * 20,
        "faculty_retention_hazard_flag": ["Low Risk"] * 20,
        "estimated_departure_timeline": ["Stable"] * 20,
        "retention_notes": ["Stable profile"] * 20,
        "faculty_id": [f"FAC-{i}" for i in range(200, 220)]
    })

if "coles_capacity_db" not in st.session_state:
    st.session_state.coles_capacity_db = pd.DataFrame({
        "major_name": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "undergrad_seat_count": [850, 1250, 680, 410, 350, 980, 240, 890, 1650, 1420],
        "retention_goal_pct": [84.0] * 10,
        "actual_retention_pct": [81.0] * 10,
        "department_inventory_count": [50] * 10
    })

ksu_gold_palette = ["#FFC400", "#00E676", "#FF5722", "#00B0FF", "#AA00FF", "#FF3D00", "#E0E0E0"]

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("Coles Navigate360")
app_panel = st.sidebar.radio("Select Operational Workspace Desk:", 
                             options=["Student Lifecycle Portal", "Faculty Retention Terminal", "EAB Campaign Manager", "Reports and Analytics Gateway"])

# ==========================================
# MODULE 4: REPORTS & ANALYTICS GATEWAY (KEY 1)
# ==========================================
if app_panel == "Reports and Analytics Gateway":
    st.header("Reports and Analytics Portfolio Gateway")
    
    ledger_df = pd.DataFrame({
        "Key ID": [f"Key {i}" for i in range(1, 11)],
        "Job Description Requirement Statement": [
            "Compiles standard and ad hoc reports",
            "Provides reports, analysis and data interpretation",
            "Identifies areas of opportunity",
            "Provides productivity analysis reports",
            "Develops and maintains reports",
            "Prepares ad hoc regulatory reports",
            "Compiles recurring operational review",
            "Assists with departmental inventory reporting",
            "Prepares ad hoc performance reporting",
            "Collaborates with campus stakeholders"
        ]
    })
    st.table(ledger_df)
    
    selected_key_tab = st.selectbox("Select Compliance Report:", options=list(ledger_df["Job Description Requirement Statement"]))
    
    if "Compiles standard and ad hoc reports" in selected_key_tab:
        st.markdown("### Key 1: Standardized vs. Ad Hoc Task Triage Console")
        rep_type = st.radio("Select Data Intake Stream:", ["Standard Recurring (Weekly Ingestion)", "Ad Hoc Live Extract Requests"])
        
        master_triage_db = pd.DataFrame({
            "Source Assigned Department": ["Finance", "IS Care Unit", "Finance", "Economics", "Admissions", "Advising", "Registrar", "Management", "IS Care Unit", "Admissions"],
            "Requested Operational Task": ["Daily Sales Audit", "Equipment Audit", "Revenue Reconciliation", "Trend Run", "EAB Analysis", "Sync Exception Report", "FTE Validation", "Grade Distribution", "Security Access Run", "Demographic Intake"],
            "Operational Priority Tier": ["ROUTINE TASK", "HIGH EMERGENCY", "CRITICAL EMERGENCY", "ROUTINE TASK", "ROUTINE TASK", "ROUTINE TASK", "ROUTINE TASK", "ROUTINE TASK", "ROUTINE TASK", "ROUTINE TASK"],
            "Days Open Pending": [1, 2, 0, 14, 7, 5, 4, 3, 2, 1]
        })
        
        clean_df = master_triage_db.copy()
        
        # FIXED LOGIC: Using bitwise operator | and parentheses to prevent ValueError
        if rep_type == "Standard Recurring (Weekly Ingestion)":
            output_df = clean_df[clean_df["Operational Priority Tier"] == "ROUTINE TASK"].sort_values(by="Days Open Pending", ascending=False)
        else:
            output_df = clean_df[(clean_df["Operational Priority Tier"] == "CRITICAL EMERGENCY") | (clean_df["Operational Priority Tier"] == "HIGH EMERGENCY")].sort_values(by="Days Open Pending", ascending=False)
            
        output_df.index = range(1, len(output_df) + 1)
        st.table(output_df)
