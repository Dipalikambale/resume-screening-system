def find_skill_matches(resume_text, job_description):

    skills = [
        "python",
        "machine learning",
        "deep learning",
        "nlp",
        "tensorflow",
        "pytorch",
        "streamlit",
        "git",
        "github"
    ]

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matched = []
    missing = []

    for skill in skills:

        if skill in job_description:

            if skill in resume_text:
                matched.append(skill)
            else:
                missing.append(skill)

    return matched, missing