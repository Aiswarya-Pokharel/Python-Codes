def check_marks():
  marks = int(input("Enter your marks: "))
  if marks < 0 or marks > 100:
      print("Invalid marks")
  elif marks >=90 and marks<=100:
    print("You got A+")
  elif marks>=80 and marks<90:
    print("You got A")
  elif marks>=70 and marks<80:
    print("You got B+")
  elif marks>=60 and marks<70:
    print("You got B")
  elif marks>=50 and marks<60:
    print("You got C+")
  elif marks>=40 and marks<50:
    print("You got C")
  else: 
    print("Fail")

check_marks()


for i in range (1,6):
  print(i)



