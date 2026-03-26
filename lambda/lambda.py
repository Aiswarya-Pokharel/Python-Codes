add = lambda a,b : a+b
print(add(10,20))

square = lambda x : x*x
print(square(5))

check = lambda x: "Even" if x%2==0 else "Odd"
print(check(5))

calc = lambda x: (x, x**2, x**3)
print(calc(3))

multiply = lambda x: lambda y: x * y
result = multiply(5)(3)
print(result)

numbers = [1,2,4,5]
for i, num in enumerate(numbers):  #enumerate gives index & values
    print(i,num)

student = {"Name": "Ram", "Age": 20}
for key, value in student.items():
    print(key,":",value),

#**********Sorting*******************#
num = [5,2,8,7]
print(sorted(num))  #ascending order
print(sorted(num,reverse=True)) #descending order

#Sort by key
students = [("Ram", 20), ("Shyam", 18), ("Hari", 22)]
sorted_std = sorted(students, key=lambda x: x[1])
print(sorted_std)  #sort by age

#******************FILTER*****************#
num = [1,2,3,4,5,6]
even_num = list(filter(lambda x: x%2==0,num))
print("Even Numbers:",even_num)

num = [3,6,12,18,26,30]
factors = list(filter(lambda x: x%6==0,num))
print("Factors of 6:",factors)

students = [
    {"name": "Ram", "marks": 80},
    {"name": "Shyam", "marks": 30}
]
passed = list(filter(lambda s:s["marks"]>=40,students ))
print("Passed Students:",passed)

#************************MAP*******************#
num=[1,2,3,4]
squared = list(map(lambda x:x**2,num))
print(squared)

num=[1,2,3,4]
squared = list(map(lambda x:x**5,num))
print(squared)

a=[1,2,3]
b=[5,6,7]
result = list(map(lambda x,y:x + y,a,b))
print(result)

a= [4,5,6]
res = list(map(lambda x:x*2,a))
print(res)

