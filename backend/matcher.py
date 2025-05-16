# backend/matcher.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_with_jobs(resume_text, jobs):
    results = []

    for job in jobs:
        job_description = job.get('description', '')
        
        # Combine texts for vectorization
        documents = [resume_text, job_description]

        # Create TF-IDF matrix
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Compute cosine similarity (resume = index 0, job = index 1)
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        match_percentage = round(similarity * 100, 2)

        results.append({
            "title": job.get("title"),
            "company": job.get("company"),
            "location": job.get("location"),
            "link": job.get("link"),
            "match": match_percentage,
            "tags": job.get("tags", []),
            "description": job.get("description")
        })

    # Sort by best match first
    results = sorted(results, key=lambda x: x["match"], reverse=True)
    return results
