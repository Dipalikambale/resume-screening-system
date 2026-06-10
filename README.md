# AI Resume Screening System

An NLP-based Resume Screening System built using Python, NLTK, Scikit-learn, PDFPlumber, and Streamlit.

## Features

- Upload Resume PDF
- Extract text from resume
- Clean and preprocess text
- Calculate Resume-JD similarity using TF-IDF and Cosine Similarity
- Identify matched skills
- Identify missing skills
- Interactive Streamlit interface

## Tech Stack

- Python
- NLTK
- Scikit-learn
- PDFPlumber
- Streamlit

## Project Structure

resume-screening-system/
│
├── app.py
├── extractor.py
├── preprocessing.py
├── similarity.py
├── skills.py
│
├── requirements.txt
├── README.md

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Workflow

Resume PDF
↓
Text Extraction
↓
Preprocessing
↓
TF-IDF Vectorization
↓
Cosine Similarity
↓
Skill Matching
↓
Results Dashboard

## Author

Dipali Dhulappa Kambale