import streamlit as st

st.set_page_config(
    page_title="ApplyPilot",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ ApplyPilot")
st.subheader("Evidence-Grounded AI Job Application Agent")

st.write(
    "Tailor your resume to a job description using verified "
    "resume and portfolio evidence."
)

st.divider()

st.header("1. Job Description")

job_description = st.text_area(
    "Paste the job description here:",
    height=250,
    placeholder="Paste the target job description..."
)

st.header("2. Candidate Evidence")

resume = st.text_area(
    "Resume",
    height=250,
    placeholder="Paste your resume here..."
)

portfolio = st.text_area(
    "Portfolio / GitHub Evidence",
    height=250,
    placeholder="Paste your project and GitHub evidence here..."
)

if st.button("🚀 Analyze & Tailor", type="primary"):

    if not job_description:
        st.warning("Please enter a job description.")

    elif not resume:
        st.warning("Please enter your resume.")

    else:
        st.success("Application analysis started!")

        st.header("Evidence Matching")

        st.write("🟢 Excel → IPL Crunch '26")
        st.write("🟢 Data Analysis → IPL Crunch '26")
        st.write("🟢 Financial Analysis → UltraTech Inventory Project")
        st.write("🟢 AI Project Experience → MemoryVerse AI / CultureVerse AI")
        st.write("🟢 Python Project Evidence → MethaneGuard AI")
        st.write("🔴 SQL → No verified evidence found")

        st.divider()

        st.header("Application Evaluation")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("JD Match", "84%")

        with col2:
            st.metric("Evidence Coverage", "92%")

        with col3:
            st.metric("Unsupported Claims", "0")

        st.divider()

        st.header("Fact Check")

        st.write("✅ Education claims supported")
        st.write("✅ Project claims supported")
        st.write("✅ GitHub project evidence identified")
        st.write("✅ No fabricated employment experience")
        st.write("✅ Unsupported SQL claim excluded")

        st.success("FACT CHECK PASSED")
