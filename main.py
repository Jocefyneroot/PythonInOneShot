# print("Hello World")


# Comments, Modules and Pip
# Comments:-
# Single line comment
"""
Multi 
line 
Comment
"""

# Modules
# import random
# print(random.randint(1,10))

# Pip:- pip is the package manager of python
# Installation
# pip install pandas
# Uninstallation
# pip uninstall pandas

# Variables, Datatypes, TypeCasting
# <DataType> <variable_name> = <Value>
# int a = 12; # Other Programming Languages
# in Python
# a = 12
# print(type(a),"Integer Variable: ", a)
# b = 12.43
# print(type(b),"Float Variable: ", b)
# c = "Jocefyneroot"
# print(type(c),"String Variable: ", c)
# d = True
# print(type(d),"Boolean Variable: ", d)
# e = None
# print(type(e),"None Variable: ", e)

# t = '12'
# y = int(t) + 1
# print(y)

# Strings
# """ """, ''' ''', ' ', " "


# myStr = """
# Multi
# Line
# String
# """
# print(myStr)

# demoStr = "Jocefyneroot"
# demoStr = 'Jocef"yneroot'
# demoStr = '''Jocef"yne'root'''

# print(demoStr)
# Indexing of String:-
myStr = "jocefyneroot"
# print(myStr[0])
# print(myStr[0:5])
# print(myStr[0:12:2])
# print(myStr[:])
# print(myStr[0:])

# String Functions
# print(myStr.lower())
# print(myStr.upper())
# print(myStr.capitalize())
# print(myStr.endswith("root"))
# print(myStr.startswith("root"))
# print(myStr.find("y"))

# Python Collection
# List, Tuple, Dictionary and set
var = 23
var = [12, 43, 65, 23, "Jocefyneroot", True]

lst = [1, 4, 2, 5, 6, 3, 6, 7]
# print(lst)
# print(lst[0])
# print(lst[3])
# print(lst.pop())
# lst.insert(1,20)
# lst.append(12)
# print(lst)
# lst[0] = 12
# print(lst)

# Tuple
# tpl = (1,2,34,54,63,2)
# print(tpl)

# print(tpl[2])

# tpl[0] = 12
# print(tpl)

# Dictionary
# myDict = {
#     "name":"Jocefyneroot",
#     "salary":1,
#     "arr":[1,2,3,4,5],
#     "dict":{"a":1, "b":2}
# }

# print(myDict['name'])
# print(myDict['salary'])
# print(myDict['dict'])

# sets
st = {1, 2, 3, 4, 5, 1}
# print(st)

# st[0] = 32 # error
# print(st)

# Conditional Expression
# age = int(input("Enter Your age: "))
# print(age)

# if-else
# if age > 10:
#     print("Age is greater than 10")
# else:
#     print("Age is not greater than 10")

# if-elif-else ladder
# if age > 20:
#     print("Age is greater than 20")
# elif age > 10:
#     print("age is greater than 10")
# else:
#     print("Above conditions not matched")

# Loops --> for, while
# for i in range(0,20):
#     print(i+1)

# for i in range(0,20,2):
#     print(i+1)

# for i in st:
#     print(i)

# while
# i = 0
# while i<10:
#     print(i)
#     i+=1

# for i in range(0,20):
#     if i == 5:
#         continue
#     print(i+1)

# for i in range(0,20):
#     print(i+1)
#     if i == 5:
#         break


# Functions
def sum(a, b):
    # print(a+b)
    return a + b


# s = sum(12,2)
# print(s)

# def factorial(n):
#     if n<=1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# file I/0
# reading
# f = open("text.txt", "r")
# print(f.read())
# f.close()

# writting
# f = open("text.txt", "w")
# f.write("My name is Jocefyneroot")
# f.close()

# appending
# f = open("text.txt", "a")
# f.write("Jocef")
# f.close()

# with open("text.txt", "r") as f:
#     data = f.read()
    
# print(data)


