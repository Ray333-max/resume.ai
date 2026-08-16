from google import genai
from pdf_reader import resume_text

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

job_title = input("What job are you applying for? ")

prompt = f"""
You are a professional resume reviewer and ATS expert.

Analyze the following resume for the specific job the user wants.

TARGET JOB:
{job_title}

RESUME:
{resume_text}

Give the following:

1. Overall Resume Score out of 100
2. Skills Match Score out of 100
3. Experience Match Score out of 100
4. Education Match Score out of 100
5. ATS Score out of 100
6. Skills the candidate has that match the job
7. Important skills missing from the resume
8. Weaknesses in the resume
9. Specific improvements the candidate should make
10. A final verdict explaining how suitable this resume is for the target job

Be honest and critical. Do not give a high score just to be encouraging.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n========== RESUME ANALYSIS ==========\n")
print(response.text)
