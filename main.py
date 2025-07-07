import streamlit as st
import fitz  # PyMuPDF
import requests
from prompts import (
    input_understanding_prompt,
    state_tracker_prompt,
    task_planner_prompt,
    output_generator_prompt,
    extract_skills_from_resume,
    extract_experience_from_resume,
)

# --- Config
API_KEY = "AIzaSyAnvpG66vwP9V6KtryVW36GyfLooVtFwvg"
GEMINI_MODEL = "models/gemini-2.0-flash"

st.set_page_config(page_title="AI Resume Assistant", layout="wide")


# --- Gemini Function
def ask_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/{GEMINI_MODEL}:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    body = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    return f"❌ ERROR {response.status_code}: {response.text}"


# --- PDF Extractor
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


# --- Custom CSS
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }
    .form-card {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        max-width: 800px;
        margin: auto;
    }
    .form-card input, .form-card textarea {
        font-size: 16px !important;
    }
    .analyze-btn {
        font-size: 16px !important;
        padding: 10px 30px;
        border-radius: 8px;
        background: linear-gradient(90deg, #0059ff, #0040ff);
        color: white;
        border: none;
        margin-top: 15px;
    }
    .analyze-btn:hover {
        background: linear-gradient(90deg, #0040ff, #002bcc);
    }
    .result-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 25px auto;
        max-width: 1100px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- Header with Logo
col1, col2 = st.columns([0.08, 0.92])
with col1:
    st.image("images/OIP.png", width=48)
with col2:
    st.markdown(
        "<h1 style='margin-bottom: 0;'>AI Resume Assistant</h1>", unsafe_allow_html=True
    )

st.markdown(
    "Get AI-powered resume analysis, mock questions, and gap detection based on your target job."
)

# --- Upload Form Centered
with st.form("resume_form"):
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("📄 Upload Resume & Job Details")
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    job_title = st.text_input("🎯 Target Job Title")
    job_description = st.text_area("💼 Paste Job Description", height=150)
    submitted = st.form_submit_button("🚀 Analyze Resume")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Analysis Section Full Width
if submitted:
    if not uploaded_file or not job_title or not job_description:
        st.warning("⚠️ Please upload your resume and fill all fields.")
    else:
        with st.spinner("🔍 Analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            skills = extract_skills_from_resume(resume_text)
            experience = extract_experience_from_resume(resume_text)

            user_profile = {
                "name": "Nirbhay",
                "job_title": job_title,
                "skills": skills,
                "experience": experience,
            }

            # Prompts
            understanding_prompt = input_understanding_prompt(
                resume_text, job_title, job_description
            )
            understanding_output = ask_gemini(understanding_prompt)

            state_prompt = state_tracker_prompt(user_profile)
            task_prompt = task_planner_prompt(resume_text, job_description)
            task_output = ask_gemini(task_prompt)

            format_prompt = output_generator_prompt(task_output)
            final_output = ask_gemini(format_prompt)

        # --- Output
        st.markdown(
            '<div class="result-card"><h4>📌 Resume Understanding</h4>',
            unsafe_allow_html=True,
        )
        st.markdown(understanding_output, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            '<div class="result-card"><h4>🧠 Tracked User Context</h4>',
            unsafe_allow_html=True,
        )
        st.code(state_prompt)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            '<div class="result-card"><h4>🛠️ AI Suggestions</h4>', unsafe_allow_html=True
        )
        st.text(task_output)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            '<div class="result-card"><h4>✅ Final Output (Markdown)</h4>',
            unsafe_allow_html=True,
        )
        st.markdown(final_output, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.success("✅ Resume analysis complete!")
