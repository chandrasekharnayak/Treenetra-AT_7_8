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


#Attribute Error:-when you try to access an attribute or method of an object that does not exsits
'''
li = [10,20,30,40]
li.append(50)
li.add(50)
AttributeError: 'list' object has no attribute 'add'
'''

#ZeroDivisionError:- When you try divied something in zero, then it's showing ZeroDivisionError
'''print(10/0)
ZeroDivisionError: division by zero'''

#FloatingPoint Error:- Due to the inherent limitation of representing real number using the floting-point data type
'''
a = 0.1
b = 0.2

sum = a+b
# print(sum)
# assert excepted_result == outcome_result/actual

# if excepted_result==outcome_result
print(sum == 0.3)
# if sum == 0.3:
#     print('sum is equal to 0.3')
# else:
#     print('sum is not equal to 0.3')
'''


#Overflow Error:- When a numerical operation result in a value that excceds the representetional limits of the data type used.
'''
# larger_interger = 2**63
# overflow_result = larger_interger*2
# print(larger_interger)
# print(overflow_result)

# larger_float = 1e308
# overflow_result = larger_float*2
# print(larger_float)
# print(overflow_result)'''

#EOF Error :- End Of File Error, when a built-in function that reads data from a file , input(),
# and encounter the end of file input during an interactive user session.

# user_input = input('Enetr something  ')
# print(f'{user_input}')

#NameError:-When a name or variable is used before it is defined .

'''c = 10
print(d)
NameError: name 'd' is not defined. Did you mean: 'id'?'''


#IndexError:- When you try tu access an index of a sequence that is outside the valid range of indicaes

'''li = [10,20,30,40]
print(li[0])
print(li[4])
IndexError: list index out of range'''

#KeyError

'''di = {'Name':'A','age':26}
print(di['Name'])
print(di['Salary'])
KeyError: 'Salary'''

#FileNotFoundError:- When you try to access file that does not exist.

'''var = open('qwerty.txt','r')
FileNotFoundError: [Errno 2] No such file or directory: 'qwerty.txt'''


# InterruptedError

'''import time  # SIGINT,ENTRI

print('Start')
time.sleep(20)
print('finsih')'''

# PermissionError:- When an operation that required certain permisiiom or access right encounters issue
#related to indaqute permissions.

'''var = open('D:\\UbuntuSetup\\treenetra_batch_list_with_candidates.xlsx','w')
PermissionError: [Errno 13] Permission denied: 'D:\\UbuntuSetup\\treenetra_batch_list_with_candidates.xlsx''''' \


#Timeout Error

# from timeout_decorator import timeout
#
# @timeout(5)
# def long_running_task():
#     while True:
#         pass
# long_running_task()

# TypeError:-when an operation is p[erformed on an object of an inapprotite Type.

#1
'''
'tfgjh'+90
TypeError: can only concatenate str (not "int") to str'''

#2
'''li = [10,20]
int(li)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'''''



#ValueError:-When a function recives an arguments of the correct type but with an invalud value.

'''number = int('abc')
ValueError: invalid literal for int() with base 10: 'abc''''