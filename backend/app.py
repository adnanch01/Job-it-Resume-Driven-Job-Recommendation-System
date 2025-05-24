# backend/app.py
from flask import Flask, request, jsonify
from resume_parser import parse_resume
from matcher import match_resume_with_jobs
from job_scraper import get_jobs




app = Flask(__name__)

@app.route('/')
def home():
    return "Job Matcher Backend is running!"

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['resume']
    text = parse_resume(file)

    if "Unsupported file type" in text:
        return jsonify({'error': text}), 400

    return jsonify({'resume_text': text})


@app.route('/scrape-jobs', methods=['GET'])
def scrape_jobs():
    jobs = get_jobs()
    return jsonify(jobs)

@app.route('/match', methods=['POST'])
def match_jobs():
    data = request.json

    if 'resume_text' not in data or 'jobs' not in data:
        return jsonify({"error": "Missing resume_text or jobs"}), 400

    matched = match_resume_with_jobs(data['resume_text'], data['jobs'])
    return jsonify(matched)


if __name__ == '__main__':
    app.run(debug=True)
