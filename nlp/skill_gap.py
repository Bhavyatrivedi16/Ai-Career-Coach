# nlp/skill_gap.py

def analyze_skill_gap(resume_skills, role_skills):
    """
    Compare resume skills with role-required skills.
    """

    resume_skills = set([s.lower() for s in resume_skills])
    role_skills = set([s.lower() for s in role_skills])

    matched = resume_skills.intersection(role_skills)
    missing = role_skills.difference(resume_skills)

    match_percentage = round((len(matched) / len(role_skills)) * 100, 2)

    return {
        "match_percentage": match_percentage,
        "matched_skills": sorted(list(matched)),
        "missing_skills": sorted(list(missing))
    }