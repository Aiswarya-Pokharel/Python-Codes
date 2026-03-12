# ________________sum of 2 numbers using function______________________
def add(a,b):
  return a+b

sum = add(4,5)
print(sum)


# ________________write operation______________________
def saveData():
  file = open('day3.py',"w")
  file.write("Details of Students: \n")
  for i in range(3):
    name = input("Enter your name: ")
    file.write(f"Name: {name}\n")
  file.close()
saveData()


# ________________read operation______________________
def readData():
  file = open("day3.py","r")
  data = file.read()
  print("***********User Data:*************\n",data)
  file.close()
readData()

