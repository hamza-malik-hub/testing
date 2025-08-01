#question 1
name = 'hamza'
age = 21
color = 'black'
script = 'my name is %s , my age is %s and my favorite color is %s.'%(name,age,color)
print(script)
#question 2
lst ={2,3,4,5,6,}
sum = sum(lst)
print(sum)
#question 3
def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("Youth"))

#question 4
def addition(x,y):
    add = x + y
    return add
def subtraction(x,y):
    sub = x - y
    return sub
def multiplication(x,y):
    multiply = x * y
    return multiply
def division(x,y):
    divide = x/y
    return divide

def calculator():
    print('1:select operator:')
    print('2:add(+)')
    print('3:sub(-)')
    print('4:multiply(*)')
    print('5:divide(/)')

    choice = input("enter choice:")
    if choice not in ('1','2','3','4'):
        print("invalid try again")
    try:
        number1=float(input('enter first number: '))
        number2=float(input('enter second number:'))
    except ValueError:
         return('invalid entry')
    if choice == '1':
        return f"Result: {addition(number1, number2)}"
    elif choice == '2':
        return f"Result: {subtraction(number1, number2)}"
    elif choice == '3':
        return f"Result: {multiplication(number1, number2)}"
    elif choice == '4':
        return f"Result: {division(number1, number2)}"
print(calculator())


#question 5
import math
print(math.factorial(19))

#question 6
from datetime import datetime
date1 =  datetime(2025,2,17)
date2 =  datetime(2025,7,18)
difference= date2 - date1
print('number of dates are:',difference)
