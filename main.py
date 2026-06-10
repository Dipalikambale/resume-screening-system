from extractor import extract_text_from_pdf
from preprocessing import preprocess_text
from similarity import calculate_similarity
from skills import find_skill_matches

resume_text = extract_text_from_pdf(
    "DIPALI KAMBALE RESUME.pdf"
)


resume_processed = " ".join(
    preprocess_text(resume_text)
)


job_description = """
AI Engineer

Skills Required:

Python
Machine Learning
Deep Learning
NLP
Streamlit
TensorFlow
PyTorch
Data Analysis
"""


jd_processed = " ".join(
    preprocess_text(job_description)
)


score = calculate_similarity(
    resume_processed,
    jd_processed
)


print(f"Match Score: {score*100:.2f}%")
matched, missing = find_skill_matches(
    resume_processed,
    job_description
)

print(f"Match Score: {score * 100:.2f}%")

print("\nMatched Skills:")
for skill in matched:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing:
    print("-", skill)