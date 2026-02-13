from career.roadmap import generate_roadmap

missing = ["sql", "statistics", "data visualization", "exploratory data analysis"]

roadmap = generate_roadmap("Data Scientist", missing)

print("📚 Learning Roadmap:")
for stage, skills in roadmap.items():
    print(stage.upper(), "→", skills)