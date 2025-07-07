# 💼 AI Resume Assistant using Gemini API

A Streamlit-based web app that uses Google's **Gemini API** to analyze resumes, extract skills and experience, and generate personalized resume feedback, mock interview questions, and skill gap suggestions.

---

## 🔍 Features

- 📄 Upload and parse PDF resumes
- 🎯 Input your target job title and description
- 🤖 AI-generated:
  - Resume improvement tips
  - Role-specific mock interview questions
  - Skill gap analysis
- ✨ Clean UI with modern styling
- 🧠 Powered by **Google Gemini 2.0 Flash**

---

## 📸 Demo

![Demo Screenshot]
![image](https://github.com/user-attachments/assets/28d2d4d0-8550-4945-80ce-206f7ac20fb9)

![image](https://github.com/user-attachments/assets/2560f085-a888-41fc-a263-2cd423e5650a)
![image](https://github.com/user-attachments/assets/e93b88ea-d7b5-4194-90f5-c952f2143105) ![image](https://github.com/user-attachments/assets/3c962243-257f-4d0d-bda2-e874a2da5a57)
![image](https://github.com/user-attachments/assets/4eb06936-af21-41b0-8634-4a4d05532d29)







---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework
- [Gemini API](https://makersuite.google.com/app) – AI backend
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) – PDF text extraction
- `requests`, `dotenv` – API calls and config

---

## 🚀 How It Works

1. Upload your resume in PDF format.
2. Enter the job title you're applying for and paste the job description.
3. The Gemini-powered assistant:
   - Extracts relevant info from your resume
   - Compares it to the job description
   - Returns improvement suggestions, mock questions, and skill feedback
4. The app presents responses in a clean, markdown-formatted UI.

---

## 📂 Project Structure

ai-resume-assistant/

├── main.py # Streamlit app

├── prompts.py # All prompt templates and skill extraction logic

├── requirements.txt # Python dependencies

├── images/

│ └── OIP.png # Logo


