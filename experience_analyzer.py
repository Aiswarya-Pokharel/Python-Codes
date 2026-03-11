experience = int(input("Enter your years of experience: "))
if experience < 1:
   print("Fresher")
elif experience <= 3:
   print("Junior Developer")
elif experience <= 7:
   print("Mid Level Developer")
else:
   print("Senior Developer")
