# AI Career Coach 🚀

AI Career Coach is an end-to-end NLP project that evaluates resumes and determines how well a candidate fits roles such as Data Scientist, Machine Learning Engineer, NLP Engineer, and Data Analyst.
The system extracts skills from resumes, performs structured skill gap analysis, calculates realistic match scores, and generates a stage-wise learning roadmap (Foundations → Core → Advanced) to guide users toward job readiness.

## Table of Contents
- Project Overview  
- Features  
- Architecture  
- Installation  
- Usage  
- Model & Logic  
- Results  
- Contributing  
- License  

## Project Overview
Choosing the right career path and identifying missing skills can be challenging for aspiring professionals. AI Career Coach helps bridge this gap by analyzing resumes and comparing them against predefined role skill profiles.
Instead of simple keyword matching, the system uses NLP-based skill extraction and embedding logic to provide explainable, structured career insights.

## Features

- Resume upload (TXT / PDF)
- Automatic skill extraction using NLP
- Role-based skill gap analysis
- Match percentage scoring
- Personalized learning roadmap generation
- Interactive Streamlit dashboard
- Modular and extensible architecture

## Architecture

The project follows a modular design:

- Resume Parsing Module (spaCy + embeddings)
- Role Profile Definition
- Skill Gap Analysis Engine
- Learning Roadmap Generator
- Streamlit UI Layer

This structure allows easy expansion to new job roles without modifying the core logic.

## Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd ai_career_coach
