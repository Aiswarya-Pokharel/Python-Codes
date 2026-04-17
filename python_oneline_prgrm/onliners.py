######### SWAPING ###########
a, b = 5, 6
a, b = b, a
print(a, b)                                        

##### IF / ELSE ########
age = 20
print("Adult") if age >= 18 else print("Minor")    

######## LIST COMPREHENSION ##############
squares = [i*i for i in range(1,6)]
print(squares)                                    

###### EVEN ##########
evens = [x for x in range(20) if x%2==0]
print(evens)                                       


########## Read File One-Liner ###########
data = open("file.txt").read()
print(data)

###### Reverse String ###########
print("python"[::-1])                              

######## Reverse a List & String ##########
print([1,2,3,4][::-1])                             

print("python"[::-1])                              

is_palindrome = lambda word: word == word[::-1]
print(is_palindrome("madam"))                      

print(is_palindrome("python"))                     

############Count Vowels#####################
count = sum(c in 'aeiouAEIOU' for c in "python")
print(count)                                       

no_vowels = ''.join(c for c in "python" if c.lower() not in 'aeiou')
print(no_vowels)                                   

############Factorial#####################
from math import prod
fact = lambda n: prod(range(1, n+1))
print(fact(5))                                     

############Prime Number#####################
is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n**0.5)+1))
print(is_prime(7))                                 

print(is_prime(10))                                

############Fibonacci#####################
fib = lambda n: [0,1][:n] if n<=2 else (lambda s: [s.append(s[-1]+s[-2]) or s for _ in range(n-2)] and s)([0,1])
print(fib(7))                                      

############GCD#####################
from math import gcd
result = gcd(12, 8)
print(result)                                      

#####SUM OF SQUARES FROM 1 TO N#######
sum_sq = lambda n: sum(i*i for i in range(1, n+1))
print(sum_sq(5))                                   

#####Ternary Conditional#######
res = "Yes" if 15 > 10 else "No"
print(res)                                         

##### Checks All elements are unique#######
lst = [1,2,3,1,4,2,4,5,6,7,3,4]
unique = len(set(lst)) == len(lst)
print(unique)                                      

##### Check if two lists are anagrams #######
are_anagrams = lambda a, b: sorted(a) == sorted(b)
print(are_anagrams([1,2,3], [3,1,2]))             

##### Check if all elements in the list are true #######
all_true = all(lst)
print(all_true)                                    

######### Check if any element is true #########
any_true = any(lst)
print(any_true)                                    

######### Flatten a 2D list ##########
flat = [i for sub in [[1,2],[3,4],[5,6]] for i in sub]
print(flat)                                        

######### Get even numbers from a list ##########
even_num = [x for x in lst if x%2==0]
print(even_num)                                    

######### Get the most frequent element ##########
most_frequent = max(set(lst), key=lst.count)
print(most_frequent)                               

######## Find duplicates in a list ##########
duplicates = list(set(x for x in lst if lst.count(x) > 1))
print(duplicates)          

######## Remove None Values ##########
cleaned = [x for x in lst if x is not None]
print(cleaned)

######## Read all non-empty lines from file ########
lines = [line.strip() for line in open('file.txt') if line.strip()]
print(lines)

######## Count the number of words in file ########
word_count = sum(len(line.split()) for line in open('file.txt'))
print(word_count)

######## Write a list to a file ########
open('out.txt', 'w').write('\n'.join(map(str, lst)))

######## Get file extension ########
filename = 'file.txt'
ext = filename.split('.')[-1]
print(ext)

######## Get all .py files in a directory ########
import os; 
py_files = [f for f in os.listdir('.') if f.endswith('.py')]
print(py_files)


