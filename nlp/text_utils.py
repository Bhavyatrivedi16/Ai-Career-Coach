import re

def clean_text(text: str) -> str:
    """
    Clean and normalize resume text for NLP processing.

    Steps:
    - Convert to lowercase
    - Remove special characters
    - Normalize whitespace

    Args:
        text (str): Raw resume text

    Returns:
        str: Cleaned text
    """
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()