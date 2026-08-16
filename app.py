import streamlit as st
import fitz
from google import genai

# -------------------------
# PAGE
# -------------------------

st.set_page_config(
    page_title="Resume AI Analyzer",
    page_icon="🤖"
)

st.title("🤖 Resume AI Analyzer")
st.write("Upload your resume and enter the job you're applying for.")

# -------------------------
# API
# -------------------------

client = genai.Client(api_key="AQ.Ab8RN6LFZDT3FGHPbALLj7LdC9mPI0a_qAaUsVP9J4Ktx3NVEg")

# -------------------------
# USER INPUT
# -------------------------

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

job_title = st.text_input(
    "What job are you applying for?"
)

# -------------------------
# ANALYZE
# -------------------------

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload your resume.")

    elif not job_title:
        st.warning("Please enter a job title.")

    else:

        # Read PDF
        document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        resume_text = ""

        for page in document:
            resume_text += page.get_text()

        document.close()

        # AI prompt
        prompt = f"""
You are a professional resume reviewer and ATS expert.

Analyze this resume for the target job.

TARGET JOB:
{job_title}

RESUME:
{resume_text}

Give:

1. Overall Resume Score out of 100
2. Skills Match Score
3. Experience Match Score
4. Education Match Score
5. ATS Score
6. Matching skills
7. Missing skills
8. Resume weaknesses
9. Specific improvements
10. Final verdict

Be honest and critical.
"""

        # Gemini
        with st.spinner("Analyzing your resume..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        # Result
        st.subheader("📊 Resume Analysis")

        st.write(response.text)