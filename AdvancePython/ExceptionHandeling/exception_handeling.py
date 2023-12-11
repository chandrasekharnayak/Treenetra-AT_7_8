#error :-

'''
SyntaxError
RunTimeError
'''
# Exception :- when a flow of program break due to some logical issue,this is know as Exception

# Resolve and Handel

# ---
# ---
# ---
# ---
# ------
# ---- exception ---- time

# Exception Handleing :- when some thread is occure is the flow of program, some process we will take this know as exception handleing

#
# a = eval(input('Enter a  number:-'))
# b = eval(input('Enter a number:-'))
#
# result = a/b
# print(result)
#
# print(10)\

#How to handel the exceptions

# try:
#     Risky Code
# except ErrorName:
#     Handel
# finally: # not a mandatory
#     Non Rsiky Code
#

# a = eval(input('Enter first number:-'))
# b = eval(input('Enter second number:-'))
# result = a/b
# print(result)

#st -1
# try:
#     a = eval(input('Enter first number:-'))
#     b = eval(input('Enter second number:-'))
#     result = a/b
#     print(result)
#
# except ZeroDivisionError:
#     print('We can divide a number with Zero')

# #st-2
#
# try:
#     a = eval(input('Enter first number:-'))
#     b = eval(input('Enter second number:-'))
#     result = a/b
#     print(result)
#
# except ZeroDivisionError:
#     print('We can divide a number with Zero')
#
# except TypeError as msg:
#     print(msg)

#st-3


# try:
#     a = eval(input('Enter first number:-'))
#     b = eval(input('Enter second number:-'))
#     result = a/b
#     print(result)
#
# except (ZeroDivisionError,TypeError) as msg:
#     print(msg)

#st-4
#
# try:
#     a = eval(input('Enter first number:-'))
#     b = eval(input('Enter second number:-'))
#     result = a/b
#     print(result)
#
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg, 'due to this reason failed')
#     b = eval(input('Enter second number:-'))
#     result  = a/b
#     print(result)
#
# except Exception as msg:
#     print(msg)

#ValueError, AttributeError, TypeError ---- code
#Every Error :-


# try:
#     a = eval(input('Enter first number:-'))
#     b = eval(input('Enter second number:-'))
#     result = a/b
#     print(result)
#
# except (ZeroDivisionError,TypeError) as sagar:
#     print(sagar)
