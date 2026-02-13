import spacy
from sentence_transformers import SentenceTransformer
from typing import List

from nlp.text_utils import clean_text

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load sentence transformer for embeddings
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Centralized skill vocabulary (can be expanded later)
SKILL_KEYWORDS = [
    "python", "java", "sql", "machine learning", "deep learning",
    "nlp", "data analysis", "pandas", "numpy", "statistics",
    "tensorflow", "pytorch", "spacy", "bert", "excel",
    "data visualization", "model deployment"
]


def extract_skills(resume_text: str) -> List[str]:
    """
    Extract skills from resume text using
    cleaned keyword matching + NLP normalization.

    Args:
        resume_text (str): Raw resume text

    Returns:
        List[str]: List of extracted skills
    """
    cleaned_text = clean_text(resume_text)

    found_skills = set()

    for skill in SKILL_KEYWORDS:
        if skill in cleaned_text:
            found_skills.add(skill)

    return sorted(found_skills)


def generate_resume_embedding(resume_text: str):
    """
    Generate a semantic embedding for the resume
    using Sentence Transformers.

    Args:
        resume_text (str): Raw resume text

    Returns:
        numpy.ndarray: Resume embedding vector
    """
    cleaned_text = clean_text(resume_text)

    if not cleaned_text:
        return None

    embedding = embedding_model.encode(cleaned_text)
    return embedding