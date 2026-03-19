score = 0
experience = input("Do you have your experience(Yes/No): ")
if experience.lower()=='yes':
  years = int(input("How many years of expericence do you have: "))
  if years<2:
    score +=5
  elif years<5:
    score +=10
  else:
    score += 15
skills = input("Do you have skills in flutter(Yes/No): ")
if skills.lower()=='yes':
  score +=10

db = input("Do you know MongoDB(Yes/No): ")
if db.lower()=='yes':
  score +=10

print("Resume Score: ",score)
