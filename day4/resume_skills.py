skills=["Python", "Java", "AWS"]

resume = input("Enter resume text: ")
for skill in skills:
  if skill in resume.lower():
    print("Skills found")