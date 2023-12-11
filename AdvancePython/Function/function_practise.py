# st = input('Enter your data:-')
#
# reversed_st = ''
#
# for i in st:
#     reversed_st = i+reversed_st
# print(reversed_st)

# def reverse_str(st):
#     reversed_st = ''
#
#     for i in st:
#         reversed_st = i+reversed_st
#
#     return reversed_st
#
# print(reverse_str('Hi Banglore'))
# print(reverse_str('Ok and Hello'))



# def func_name():
#     print('Hi')
#
# func_name()
# func_name()
# func_name()
# func_name()

#write a program adition of two number

# def add(num1,num2):
#     add = num1+num2
#     return add
#
# print(add(10,20))
# print(add(56,23))


# write a function fetch the all list element?
# write a fucntion find the biggest number among two?

# li1 = [10,20,30,40,50]
#
# def iter_list(li):
#     for i in li:
#         print(i)
#
# iter_list(li1)


# def biggest_one(num1,num2):
#     if num1>num2:
#         print(num1)
#     else:
#         print(num2)
#
# biggest_one(10,20)


# def biggest_one(num1,num2,num3):
#     if num1>num2 and num2
#
# a = [67,56,43,23,90,86]
#
# def list_biggest(li):
#     a.sort()
#     print(a[-1])
#
# list_biggest(a)


#write a program the string is pallidrom or not

# str = 'madam'
#
# def is_pallindrom(str):
#     print(str == str[::-1])
#
# is_pallindrom(str)


#-------------------------------------------------------------------------------
#
# weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
#
# print([[x, weekdays.count(x)] for x in set (weekdays)])

# numberGames = {}
#
# numberGames[(1, 2, 4)] = 8
# numberGames[(4, 2, 1)] = 10
# numberGames[(1, 2)] = 12
#
# sum_val = 0
#
# for k in numberGames:
#     sum_val += numberGames[k]
#
# print(len(numberGames) + sum_val)

#-------------------------------------------------------
# Types of arguments

#positional arg
# def add(a,b):# formal argument --- parameter
#     return a+b
#
# print(add(10,20))  #actual argument  --- arguments


#keyword arguments

# def add(a,b,c):
#     add = a+b
#     sep = add-c
#     return sep
#
# print(add(c= 30,a=10,b=20))

# def add(a,b,c):
#     add = a+b
#     sep = add -c
#     return sep
#
# print(add(10,c = 30,b = 20))


#default arguments

# def temp(cel=37):
#     far = (cel*(9/5))+32
#     return far
#
# print(temp())
# print(temp(40))


#variable length argument - nth arg (*args)

# def addition(*args):
#     print(args)
#     print(type(args))
#
# addition(10,20,30,40,50,60,70,80,90,12,1,2,3,4,4,2,3,3,2)

#
# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum+i
#     return sum
#
# print(addition(10,20,30,76,768,768))


#keyword arguments (**kwargs)

# def kwyord_args(**kwargs):
#     for key,val in kwargs.items():
#         print(key,val)
#
# kwyord_args(Name='Krishna',Age= 26, Address = 'Ghatikia')


#write a nth variable function, what ever end user sent the argument, if argument is duplicate
#please remove the duplicate value, return only the original one.


# def remove_dup_value(*args):
#     original_value = []
#
#     for i in args:
#         if i not in original_value:
#             original_value.append(i)
#     return original_value
#
# print(remove_dup_value(10,20,10,10,20,1,1,1,2,22,3,3,3,4))



#Types of variable

#global variable
#local variable

# c= 10  # global
#
# def add(a,b):
#     result = a+b+c
#     return result
#
# print(add(10,20))
# print(c)
#
# def sub(a,b):
#     result = a-b-c
#     return result
# print(sub(70,20))



#local variable

# def add(a,b):
#     global c
#     c = 10
#     add = a+b+c
#     return add
#
# print(add(20,30))
#
# def sub(a,b):
#     sub = a-b-c
#     return sub
# print(sub(10,20))


#---------------------
#lambda:-

# syntax

# var = lambda parameter:statement/logic
# var(args)
#
# var = lambda a,b:a+b
# print(var(10,20))

#squre

# var = lambda a:a*a
# print(var(10))


# def cal(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#
#     return add,sub,mul,div
#
# print(cal(10,20))


#write lambda expression find the bigesst amoung two.

# var = lambda a:a*a
# print(var(10))


# var = lambda a,b:a if a>b else b
# print(var(10,20))


#Check string is pallindrom or not help of lambda

# pallindrom = lambda a : a == a[::-1]
# print(pallindrom('tyu'))
# print(pallindrom('madam'))

# pallindrom = lambda a: 'pallindrom' if a==a[::-1] else 'Not Pallindrom'
# print(pallindrom('tyu'))
# print(pallindrom('madam'))


# var = lambda parameter:statemenet
# var(args)
#---------------------------------------------------------

#filter, map, reduce

#filter :- do the filterization in a collection based upon functional condition.

# syntax

# var = filter(function,collection)

li = [11,78,98,67,65,64,32,31,90,96]

#with function
'''def even(a):
    if a%2==0:
        return True

var = list(filter(even,li))
print(var)'''

#without function
'''var = list(filter(lambda a:a%2==0,li))

print(var)'''

#map

# li = [11,78,98,67,65,64,32,31,90,96]
#
# var = list(map(lambda a:a+100,li))
# print(var)


# name_li = ['balay','ragav','sachin','ritu','mahi']
#
# var = list(map(lambda a:str(a).capitalize(),name_li))
# print(var)


#reduce
from functools import reduce

# li = [10,20,30,40,50]
# var = reduce(lambda a,b:a+b,li)
# print(var)

# function
'''sorted()
enumarate()
zip()
help()'''

#module

'''Math
os
sys
random'''

#Nested Func

# def outer():
#     print('Outer function  excute')
#     def inner():
#         print('Inner function  excute')
#     inner()
#     print('Inner function end')
#     print('Outer function end')
#
# outer()


#WAP add two number, what ever result will get squre this number?

# def add(a,b):
#     result = a+b # 30
#     def squre(sqr):
#         squre_result = result*result
#         return squre_result
#     return result,squre(result)
#
# print(add(10,20))
# print(add('qwer',90))

#WAP multiple two number and check the number even or odd help nested function?

# def mul(a,b):
#     result = a*b
#     def inner(re):
#         if re%2==0:
#             return 'Even'
#         else:
#             return 'Odd'
#     return result,inner(result)
#
# print(mul(10,20))


# def mul(a,b):
#     result=10*20
#     def even_or_odd(re):
#         var = 'Even' if re%2==0 else 'Odd'
#         return var
#     return result,even_or_odd(result)
# print(mul(10,20))

#Remove the string element in the list and sort it in nested function?


# li = [12,'ui',90,'67',34,'qwerty','23',45,49,11,'yuo',42]
# def str_remove(list):
#     li1= []
#     for i,char in enumerate(list):
#         if type(char)==str:
#
#
# print(str_remove(li))
# print(li)


#Recusion:-

# def add(a,b):
#     add(a,b)
#
# add(a,b)

#factorial :- 5 = 5*4*3*2*1

# def factorial(num):
#     if num ==1:
#         return 1
#     else:
#         return (num* factorial(num-1))
#
# print(factorial(5))


#Decorator

# def decore(cal):
#     def mul(a,b):
#         result_mul = a*b
#         return result_mul,cal(a,b)
#     return mul
#
# @decore
# def cal(a,b):
#     result = a+b
#     return result
#
# print(cal(10,20))



#write decorator for check number is even or odd and check pallimdrom or not without using any function

# def decore(even_odd):
#     def pallindrom(num):
#         if str(num)==str(num)[::-1]:
#             return 'Pallindrom',even_odd(num)
#         else:
#             return 'Not a Pallindrom',even_odd(num)
#     return pallindrom
#
# @decore
# def even_odd(num):
#     if num%2==0:
#         return True
#     else:
#         return False
#
# print(even_odd(121))



#chain of decorator

# def decore2(cal):
#     def div(a,b):
#         result_div = a/b
#         return result_div,cal(a,b)
#     return div
#
# def decore1(cal):
#     def sub(a,b):
#         result_sub = a-b
#         return result_sub,cal(a,b)
#     return sub
#
# def decore(cal):# 2023 aug 17
#     def mul(a,b):
#         result_mul = a*b
#         return result_mul,cal(a,b)
#     return mul
#
# @decore2
# @decore1
# @decore
# def cal(a,b): # 2023 july 2020
#     result = a+b
#     return result
#
# print(cal(10,20))


#----------------------------------------

# def decore(func1):
#     def how_are_you(name):
#         print('How are you?',name)
#         func1(name)
#     return how_are_you
#
# @decore
# def func1(name):
#     print('Hi',name,'Good morning')
#
# func1('Sital')

# decorator is a function, it's take parameter as a another function name,modify and adding the new function
# and return a extensive function.


#Generator

#generator is also be a normal function, it's using the yield keyword for returning the object.
#it's return the object one by one help of next()

# def iter():
#     for i in range(1,11):
#         yield i
#
# #for generator we create a object
#
# obj = iter()
#
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

#What is function
#User Define function
#parameter
#Types of arguments
#Types of variables
#Lambda :- flitet map reduce
#Nested function
#recursion
#decorator
#generator


