# 1. Write a program that asks the user for their name, age, and city, then prints a sentence using all three.

# name = input('Enter your name: ')
# age  = input('Enter your age: ')
# city = input('Enter your city: ')

# print("Hello! I am " + name + ", " + age + " years old, from " + city + ".")

# output:
# Enter your name: praveen
# Enter your age: 23
# Enter your city: nandyal
# Hello! I am praveen, 23 years old, from nandyal.


# 2.Create five variables with different data types. Print the value AND type of each one using type().

# a = 42
# b = 3.14
# c = 'Python'
# d = True
# e = 0

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))   
# print(d, type(d))   
# print(e, type(e))   

# output:
# 42 <class 'int'>
# 3.14 <class 'float'>
# Python <class 'str'>
# True <class 'bool'>
# 0 <class 'int'>


#  3. Perform the following conversions and print the result and its data type after each step.

# age_str = '25'
# print(int(age_str), type(int(age_str)))

# price = 199.99
# print(int(price), type(int(price)))

# score = 1 
# print(bool(score), type(bool(score)))

# flag = True 
# print(int(flag), type(int(flag)))

#  output:

# 25 <class 'int'>
# 199 <class 'int'>
# True <class 'bool'>
# 1 <class 'int'>



# 4.Ask the user to enter a number. Try to convert it to an integer. If the user types a word (like 'hello'), print a friendly error message instead of crashing.

# a = input("Enter a number: ")

# try:
#     num = int(a)
#     print("You entered the number:", num)

# except ValueError:
#     print("That is not a valid number!")

# output:
# Enter a number: hello     
# That is not a valid number!


# 5. Ask the user for a principal amount, interest rate (%), and number of years. Calculate and print the simple interest and the total amount.
# Formula: Simple Interest = (P × R × T) / 100

# P=int(input("Enter the principal amount: "))
# t=int(input("Enter the number of years: "))
# r=float(input("Enter the interest rate: "))
# si=(P * r * t) / 100
# total_amount = P + si

# print("Simple Interest:", si)
# print("Total Amount:", total_amount)

# output:
# Enter the principal amount: 10000
# Enter the number of years: 5
# Enter the interest rate: 5
# Simple Interest: 2500.0
# Total Amount: 12500.0


#  5. Without using the type() function, write a program that determines whether a given variable is an integer, float, string, or boolean — and prints the result.

# def check_type(value):

#     if isinstance(value, bool):
#         return "boolean"

#     elif isinstance(value, int):
#         return "integer"

#     elif isinstance(value, float):
#         return "float"

#     elif isinstance(value, str):
#         return "string"

#     else:
#         return "unknown type"


# print(check_type(42))        
# print(check_type(3.14))      
# print(check_type('hello'))   
# print(check_type(True))      

# output:
# integer
# float
# string
# boolean
