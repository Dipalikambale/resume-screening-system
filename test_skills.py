from skills import find_skill_matches

resume = """
python machine learning nlp pandas
"""

job_description = """
python machine learning deep learning
tensorflow pytorch nlp
"""

matched, missing = find_skill_matches(
    resume,
    job_description
)

print("Matched Skills:")
print(matched)

print()

print("Missing Skills:")
print(missing)