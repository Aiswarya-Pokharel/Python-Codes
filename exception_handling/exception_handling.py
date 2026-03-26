#*********************Exception Handling*********************#
try:
    print('This is a try block')
    num = int(input("Enter a number: "))
    print(10/num)

except ValueError:
    print("Invalid input.Please enter a number")

except ZeroDivisionError:
    print("You can't divide by zero")


#*********************Else & Finally*********************#
try:
    x = 10/2

except ZeroDivisionError:
    print("You can't divide by zero")

else:
    print("Success!", x)

finally:
    print("This always runs & works")


#*********************Raising Exception*********************#
def withdraw(balance, amt):
    if amt > balance:
        raise Exception("Not enough funds or insufficient balance")
    return balance - amt

try:
    result = withdraw(100, 100987)
    print(result)
except Exception as e:
    print(e)


#*********************Custom Exception*********************#
class InsufficientBalanceError(Exception):
    pass

def withdraw(blc, amt):
    if amt > blc:
        raise InsufficientBalanceError("Insufficient balance")
    return blc - amt

try:
    result = withdraw(100, 100987)
    print(result)
except InsufficientBalanceError as e:
    print(e)


#*********************Real life example*********************#
def login(username, password):
    if username != "admin":
        raise ValueError("User not found")
    if password != "1234":
        raise ValueError("Incorrect password")
    return "Into login"

try:
    print(login("admin", "1234"))
except ValueError as e:
    print(e)