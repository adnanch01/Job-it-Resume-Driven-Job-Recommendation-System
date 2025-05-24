# backend/job_scraper.py

import requests
from bs4 import BeautifulSoup


def get_jobs():
    return [
        {
            "title": "Backend Engineer Intern",
            "company": "MockTech",
            "location": "Remote",
            "tags": ["Python", "Flask", "AWS"],
            "description": "Work with Python and Flask APIs on AWS cloud.",
            "link": "https://mocktech.com/jobs/backend-intern"
        },
        {
            "title": "Frontend Developer",
            "company": "DesignHub",
            "location": "San Francisco",
            "tags": ["React", "TypeScript"],
            "description": "Build responsive UIs using React and Tailwind CSS.",
            "link": "https://designhub.io/careers/frontend-dev"
        },
        {
            "title": "ML Engineer Intern",
            "company": "AI Labs",
            "location": "Remote",
            "tags": ["TensorFlow", "Python", "NLP"],
            "description": "Contribute to NLP projects using TensorFlow and Hugging Face.",
            "link": "https://ailabs.org/ml-intern"
        }
    ]


    return jobs
