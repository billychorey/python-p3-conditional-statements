#!/usr/bin/env python3
# f the username is "admin" or "ADMIN" and 
# the password is "12345", return "Access granted". 
# Otherwise, return "Access denied".

def admin_login(username, password):
    if username.lower() == 'admin' and password == '12345':
        return 'Access granted'
    else:
        return 'Access denied'


#  If the temperature is below 40, return 
# "It's brisk out there!". If the temperature is 
# between 40 and 65, 
# return "It's a little chilly out there!". 
# If the temperature is above 85, return 
# "It's too dang hot out there!". 
# Otherwise, return "It's perfect out there!"



def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature >= 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    
# For multiples of three, return "Fizz" instead of the number.
# For the multiples of five, return "Buzz".
# For numbers which are multiples of both 
# three and five, return "FizzBuzz". For all other numbers, 
# just return the number itself.

def fizzbuzz(num):
    divisor1 = 3
    divisor2 = 5

    if num % divisor1 == 0 and num % divisor2 == 0:
        return 'FizzBuzz'
    elif num % divisor1 == 0:
        return 'Fizz'
    elif num % divisor2 == 0:
        return 'Buzz'
    else:
        return num

def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print ('Invalid operation!')
        return None
