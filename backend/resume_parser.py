import PyPDF2
import docx
import io
import re

# --- Predefined skill keywords (extendable) ---
SKILL_KEYWORDS = {
    "python", "java", "c++", "sql", "javascript", "typescript",
    "html", "css", "react", "flask", "django", "aws", "git",
    "tensorflow", "pytorch", "docker", "kubernetes", "postgresql",
    "mongodb", "firebase", "bash", "linux", "node.js", "fastapi",
    "numpy", "pandas", "scikit-learn"
}


# --- Resume File Parsers ---
def parse_pdf(file_stream):
    pdf_reader = PyPDF2.PdfReader(file_stream)
    text = ''
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text.strip()

def parse_docx(file_stream):
    doc = docx.Document(file_stream)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text.strip()


# --- Skills Extractor ---
def extract_skills(resume_text):
    resume_text = resume_text.lower()
    skills_found = set()
    for skill in SKILL_KEYWORDS:
        if skill in resume_text:
            skills_found.add(skill)
    return list(skills_found)


# --- Experience Section Extractor ---
def extract_experience_section(resume_text):
    lines = resume_text.splitlines()
    experience_lines = []
    capture = False

    for line in lines:
        # Start capturing from "Experience" or similar section
        if re.search(r'\b(experience|work experience|employment)\b', line.strip(), re.IGNORECASE):
            capture = True
            continue
        if capture:
            # Stop capturing if we hit a new section heading (e.g., EDUCATION)
            if line.strip() == "" or re.match(r'^[A-Z ]{2,}$', line.strip()):
                break
            experience_lines.append(line.strip())

    return "\n".join(experience_lines).strip()


# --- Main Resume Parser Function ---
def parse_resume(file):
    filename = file.filename.lower()
    file_stream = io.BytesIO(file.read())

    if filename.endswith('.pdf'):
        text = parse_pdf(file_stream)
    elif filename.endswith('.docx'):
        text = parse_docx(file_stream)
    else:
        return "Unsupported file type. Only PDF and DOCX are allowed."

    skills = extract_skills(text)
    experience = extract_experience_section(text)

    return {
        "raw_text": text,
        "skills": skills,
        "experience": experience
    }
