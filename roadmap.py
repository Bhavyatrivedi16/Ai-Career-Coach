# career/roadmap.py

ROLE_ROADMAP = {
    "Data Scientist": {
        "foundations": ["statistics", "sql"],
        "core": ["exploratory data analysis", "data visualization"],
        "advanced": ["feature engineering", "model evaluation"]
    },
    "Machine Learning Engineer": {
        "foundations": ["scikit-learn", "data pipelines"],
        "core": ["deep learning", "pytorch", "tensorflow"],
        "advanced": ["model deployment", "mlops"]
    },
    "NLP Engineer": {
        "foundations": ["natural language processing", "text preprocessing"],
        "core": ["nltk", "spacy"],
        "advanced": ["bert", "transformers"]
    },
    "Data Analyst": {
        "foundations": ["excel", "statistics"],
        "core": ["sql", "data visualization"],
        "advanced": ["power bi", "tableau"]
    }
}


def generate_roadmap(role, missing_skills):
    roadmap = {}

    role_plan = ROLE_ROADMAP.get(role, {})

    for stage, skills in role_plan.items():
        roadmap[stage] = [skill for skill in skills if skill in missing_skills]

    return roadmap