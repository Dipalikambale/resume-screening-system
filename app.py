import streamlit as st
import tempfile

from extractor import extract_text_from_pdf
from preprocessing import preprocess_text
from similarity import calculate_similarity
from skills import find_skill_matches


st.title("AI Resume Screening System")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)


if st.button("Analyze"):

    if uploaded_file is not None and job_description:

        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp_file:

            tmp_file.write(
                uploaded_file.read()
            )

            pdf_path = tmp_file.name

        # Extract resume text
        resume_text = extract_text_from_pdf(
            pdf_path
        )

        # Preprocess texts
        resume_processed = " ".join(
            preprocess_text(resume_text)
        )

        jd_processed = " ".join(
            preprocess_text(job_description)
        )

        # Similarity Score
        score = calculate_similarity(
            resume_processed,
            jd_processed
        )

        # Skill Matching
        matched, missing = find_skill_matches(
            resume_processed,
            job_description
        )
        # st.write("Matched:", matched)
        # st.write("Missing:", missing)
        st.write("Resume Processed Preview:")
        st.write(resume_processed[:500])

        st.write("Job Description Preview:")
        st.write(job_description)

        # Results
        st.subheader("Results")

        percentage = round(score * 100, 2)

        st.write(f"Match Score: {percentage}%")

        st.progress(min(score, 1.0))
        

        st.subheader("Matched Skills")

        if matched:
            for skill in matched:
                st.write(f"✅ {skill}")
        else:
            st.write("No matched skills found.")

        st.subheader("Missing Skills")

        if missing:
            for skill in missing:
                st.write(f"❌ {skill}")
        else:
            st.write("No missing skills detected.")