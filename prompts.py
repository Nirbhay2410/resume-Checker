def input_understanding_prompt(resume, job_title, job_description):
    return f"""
You are an AI resume assistant.

Candidate Resume:
{resume}

Target Job Title: {job_title}
Job Description:
{job_description}

Extract skills, experience, and role expectations to understand what this candidate needs to succeed.
"""


def state_tracker_prompt(user_profile):
    return f"""
Track this user context:
Name: {user_profile.get("name")}
Role: {user_profile.get("job_title")}
Skills: {', '.join(user_profile.get("skills", []))}
Experience: {user_profile.get("experience")}

Maintain this across all turns. Ask for missing info if needed.
"""


def task_planner_prompt(resume, job_description):
    return f"""
Compare this resume with the job description below.
- Suggest 3 resume improvement tips.
- Generate 5 mock interview questions.
- Identify 2 skill gaps with brief suggestions.

Resume:
{resume}

Job Description:
{job_description}
"""


def output_generator_prompt(response_text):
    return f"""
Format this output clearly using markdown with sections:
## Resume Tips
## Interview Questions
## Skill Gap Feedback

Response:
{response_text}
"""


def extract_skills_from_resume(resume_text):
    keywords = [
        "Python",
        "SQL",
        "Java",
        "Machine Learning",
        "Deep Learning",
        "Data Visualization",
        "Streamlit",
        "YOLO",
        "OpenCV",
        "CNN",
        "Pandas",
        "Numpy",
        "Scikit-learn",
        "Keras",
        "Matplotlib",
        "Roboflow",
        "Google Colab",
        "Jupyter",
        "HTML",
        "CSS",
    ]
    return [kw for kw in keywords if kw.lower() in resume_text.lower()]


def extract_experience_from_resume(resume_text):
    if "EXPERIENCE" in resume_text.upper():
        start = resume_text.upper().find("EXPERIENCE")
        end = resume_text.upper().find("PROJECTS")
        if end == -1:
            end = len(resume_text)
        return resume_text[start:end].strip()
    return "Experience section not found."
