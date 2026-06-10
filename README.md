# AI Resume Screening System
<img width="857" height="388" alt="image" src="https://github.com/user-attachments/assets/82d16c5a-e812-4abe-be22-84ead714eaf2" />


## Overview

AI Resume Screening System is an NLP-based application that analyzes resumes against job descriptions and calculates a match score. The system extracts text from PDF resumes, preprocesses the content, performs similarity analysis using TF-IDF and Cosine Similarity, and identifies matched and missing skills.

This project demonstrates Natural Language Processing (NLP), Information Retrieval, and Machine Learning concepts using Python.

---

## Features

* Upload Resume PDF
* Extract text from PDF resumes
* Clean and preprocess text using NLP techniques
* Calculate Resume-JD similarity score
* Identify matched skills
* Identify missing skills
* Interactive Streamlit web application
* ATS-style resume evaluation

---

## Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Streamlit
* NLTK
* Scikit-learn
* PDFPlumber
* NumPy
* Pandas

### Version Control

* Git
* GitHub

---

## Project Workflow

Resume PDF
↓
PDF Text Extraction
↓
Text Preprocessing
↓
TF-IDF Vectorization
↓
Cosine Similarity
↓
Skill Matching
↓
Match Score Generation
↓
Results Dashboard

---

## Project Structure

resume-screening-system/

├── app.py

├── extractor.py

├── preprocessing.py

├── similarity.py

├── skills.py

├── requirements.txt

├── README.md

└── screenshots/

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Dipalikambale/resume-screening-system.git
```

Navigate to the project directory:

```bash
cd resume-screening-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Sample Use Case

1. Upload a resume PDF.
2. Paste a job description.
3. Click Analyze.
4. View:

   * Match Score
   * Matched Skills
   * Missing Skills

---

## Future Improvements

* BERT-based semantic similarity
* Resume ranking for multiple candidates
* Skill extraction using Named Entity Recognition (NER)
* Job recommendation system
* Resume improvement suggestions
* Database integration

---

## Skills Demonstrated

* Python Programming
* Natural Language Processing (NLP)
* Text Preprocessing
* TF-IDF Vectorization
* Cosine Similarity
* Streamlit Application Development
* Git & GitHub
* Machine Learning Fundamentals

---

## Author

Dipali Dhulappa Kambale

Aspiring AI Engineer | Python | Machine Learning | NLP
