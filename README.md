# 💎 KSU-Institutional-IR-Engine
An enterprise-grade, regulatory-compliant Institutional Research (IR) analytics suite engineered to transform raw campus data arrays into formalized, audit-ready data models for high-level stakeholders.

## 🏢 Project Architecture & Scope
This system replicates an institutional business data analyst platform configured for university-wide data governance. Shifting away from small, localized student operations, this architecture models macro-level tracking frameworks across student body lifecycles and educational resources. A central university researcher or state auditor can monitor global system metrics or seamlessly filter data parameters down to an isolated academic college on demand.

* **👉 View the Live Interactive Portal Here:** [YOUR_STREAMLIT_LIVE_URL_HERE]

---

### 🗄️ Phase 1: Relational Institutional Modeling (SQL)
Designed a centralized university data schema modeling structured academic structures. The framework preserves complete internal data integrity via intentional parent-child indexing fields, isolating tracking points across three primary analytical domains.
* **Master Client Colleges Table:** Defines corporate campus domains (tracking College Names, Academic Major codes, and Target Enrollment Caps).
* **Workload Lifecycle Logs Table:** Records row metrics mapping operational credit metrics (capturing Student Headcounts at the Semester Freeze Date, Full-Time Faculty workloads, Grade Pass/DFW counts, and Graduate Completion awards).
* **Code Links:** `database/ir_schema.sql` | `database/ir_seed_payload.sql`

---

### ⚙️ Phase 2: Regulatory Transformation & FERPA Masking Logic
Engineered a secure data engineering layer using Python and the `pandas` library to replace fragile input tracking methods with an automated data pipeline equipped with structural privacy guardrails.
* **Census Data Ingestion Routing:** Pulls distributed major matrices and normalizes counts precisely at the university's standardized semester "freeze milestone".
* **Automated FERPA Cell Suppression:** Applies custom boolean conditioning arrays to evaluate live datasets, automatically catching small cell counts (values < 30) and masking them securely to protect student records in public dashboards.
* **Code Link:** `src/app.py`

---

### 🖥️ Phase 3: High-Density Institutional Research Workstation (Streamlit)
Developed a white-labeled, dark-themed analytics portal with custom accent configurations built specifically to present complex datasets clearly to university leadership and external auditors.
* **Student Population Lifecycle Analytics:** Generates multi-year cohort retention curves and enrollment yield matrices to track long-term graduation trends across various programs.
* **Faculty Allocation & Course Evaluation Maps:** Plots interactive group bar charts visualizing passed counts versus fail/withdrawal (DFW) categories to help administrators monitor course performance patterns.
* **Forensic Compliance Data Dispatcher:** Features a dedicated data review console that maps finalized data assets to the specific reporting frameworks required by the University System of Georgia (USG), federal IPEDS, and national publications like U.S. News & World Report.
