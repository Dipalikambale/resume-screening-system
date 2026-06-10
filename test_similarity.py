from similarity import calculate_similarity

resume = """
python machine learning nlp streamlit
"""

job_description = """
python machine learning deep learning
"""

score = calculate_similarity(
    resume,
    job_description
)

print(score)