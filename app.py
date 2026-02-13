import streamlit as st
from nlp.resume_parser import extract_skills
from nlp.role_profiles import ROLE_SKILLS
from nlp.skill_gap import analyze_skill_gap
from career.roadmap import generate_roadmap

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Career Coach",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Career Coach")
st.caption("Resume analysis • Skill gap detection • Career roadmap")

# -----------------------------
# Resume Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "📄 Upload your resume (TXT or PDF)",
    type=["txt", "pdf"]
)

if uploaded_file:
    # Read resume
    if uploaded_file.type == "text/plain":
        resume_text = uploaded_file.read().decode("utf-8")
    else:
        import pdfplumber
        with pdfplumber.open(uploaded_file) as pdf:
            resume_text = "\n".join(
                [page.extract_text() or "" for page in pdf.pages]
            )

    # -----------------------------
    # Extract Skills
    # -----------------------------
    st.subheader("✅ Extracted Skills")
    resume_skills = extract_skills(resume_text)
    st.write(resume_skills)

    st.divider()

    # -----------------------------
    # Role Analysis
    # -----------------------------
    st.subheader("🎯 Career Role Analysis")

    for role, role_skills in ROLE_SKILLS.items():
        result = analyze_skill_gap(resume_skills, role_skills)

        match_pct = result["match_percentage"]
        matched = result["matched_skills"]
        missing = result["missing_skills"]

        # ---------- Role Card ----------
        with st.container():
            st.markdown(f"## {role}")
            st.progress(match_pct / 100)
            st.write(f"**Match Score:** {match_pct}%")

            col1, col2 = st.columns(2)

            with col1:
                st.success("Strong Skills")
                st.write(matched if matched else "—")

            with col2:
                st.error("Missing Skills")
                st.write(missing if missing else "—")

            # ---------- Roadmap ----------
            roadmap = generate_roadmap(role, missing)

            st.markdown("### 📚 Learning Roadmap")
            for stage, skills in roadmap.items():
                if skills:
                    st.info(f"**{stage.upper()}** → {', '.join(skills)}")

            st.divider()

    st.success("🎉 Analysis complete! Follow the roadmap to level up your career.")