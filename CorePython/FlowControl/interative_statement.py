# for statement :- normal interation it's applicable in collections ony like list,tuple,set,range,dict,string
# while statement :- conditional iteration, like if condition statisfy then iteration is going on.

# for syntax

# for var in collection_name:
#     statement
#

# li = [10,89.90,'qwerty']
#
# for var in li:
#     print(var)

#find all the even number in a list and add in another list

# li = [11,90,23,45,67,89,76,54,31,25,65]
#
# even_li = []
# odd_li = []

# for var in li:
#     if var%2==0:
#         even_li.append(var)
#     else:
#         odd_li.append(var)
#         # print(var)
# print(even_li)
# print(odd_li)

# in a collection check the type data and print , and add all the non-collection object in a another collection

# li = [10,20,30.89,90.89,True,'String',[678,90],(68,90),{56,90}]
#
# non_collection = []
#
# for var in li:
#     print(var,type(var))
#
#     if type(var)== int or type(var)== float or type(var)==bool:
#         non_collection.append(var)
# print(non_collection)

#range :- generate the sequence of number based on loop
# range(start,end+1,step)

# for i in range(1,11):
#     if i%2 !=0:
#         print(i)
    # print(i)

# for i in range(1,11,2):
#     print(i)


# how use for loop in dictionary

# di = {'Math':82,'Science':89,'History':78}
#
# for key,value in di.items():
#     print(key,value)


# li = [102,203,303,40,407]
#
# sum = 0 #1055
# for i in li:
#     sum = sum +i #sum+=i
# print(sum)

# 1
#li = [10,20,,78.89,67.56,'78',[90,90,89],(68,90)]
#add those itmes , those data type only int and float

# 2
#di = {'Math':82,'Science':89,'History':78}
# li = [10,20]

#output = li [10,20,82,89,78] sum all the items in the list



# li = [10,20,30]
#
# sum = 0
# for var in li:
#     sum = sum+var
# print(sum)

#1

# li = [10,20,78.89,67.56,'78',[90,90,89],(68,90)]
#
# sum = 0
# for i in li:
#     if type(i) == int or type(i)== float:
#         sum = sum +i
#
# print(sum)


# 2

# di = {'Math':82,'Science':89,'History':78}
# li = [10,20]
#
# for k,v in di.items():
#     li.append(v)
#
# sum = 0
#
# for i in li:
#     sum = sum+i
# print(sum)
# print(li)

# Star Programming

'''
*
*
*
*
*
'''

# star = int(input('Enter a your star number:-'))
#
# for i in range(star):# 0,1,2,3,4
#     print('*')

#2 ''' ******'''

# star = int(input('Enter a your star number:-'))
#
# for i in range(star):
#     print('*',end=' ') # end seprator


'''
*
**
***
****
*****
'''
#nested for:- when a interation under a another iteration it's know as nested for

# star = int(input('Enter a your star number:-'))

# for i in range(star):#i = 0 1 2 3 4
#     for j in range(i+1):# j = 1,2,3,4 5
#         print('*',end='')
#     print() # v to h

# first for :- is only the reason of iteration  # horizental
# sec for :- how many star you want to your each iteration

# for i in range(star):#i = 0 1 2 3 4
#     for j in range(i+1):# j = 1,2,3,4 5
#         print('*',end = '')
#     print()


'''
*****
****
***
**
*

'''

# for i in range(star):
#     for j in range(star-i):
#         print('*',end='')
#     print()

# li = [
#     [10,20,30], [30,40,50],[60,70,80]
# ]
#
# for i in li:
#     for j in i:
#         print(j)


#1
#Find all subject name of the canidtate
# di = {'Name':'Ajay','Salary':78000,'Subject':['Python','Java','SQL']}

# 2

candidate_li = [
{'Name':'Ajay','Salary':78000,'Subject':['Python','Java','SQL']},
{'Name':'Atul','Salary':67000,'Subject':['C','Perl']},
{'Name':'Rahul','Salary':56000,'Subject':['Python','dotnet']},
{'Name':'Sagar','Salary':23000,'Subject':['Perl','Java','SQL']},
{'Name':'Sudharshan','Salary':34000,'Subject':['Kibana','Grafana','SAP']},
{'Name':'Santosh','Salary':26000,'Subject':['Python','PlSql','SQL']}
]

# find out the candidate who have LESS then 30,000 salary
# find the candidate details , who have Python on his subjcet

# di = {'Name':'Ajay','Salary':78000,'Subject':['Python','Java','SQL']}
# print(di['Subject'])

# for k,v in di.items():
#     if k=='Subject':
#         print(v)


# #find out the candidate who have LESS then 30,000 salary


# for i in candidate_li:
#     if i.get('Salary')<=30000:
#         print(i)

# for i in candidate_li: # i = dict
#     for k,v in i.items(): # key and value
#         if k=='Salary':
#             if v<=30000:
#                 print(i)


# find the candidate details , who have Python on his subjcet

# for i in candidate_li:# i = dict
#     for k,v in i.items():
#         if k == 'Subject':
#             for j in v:
#                 if j == 'Python':
#                     print(i)


#while loop:- conditional iteration
#if the conditon is satatisfy then the loop is execute nor it failed.

'''
syntax:-

while condition:
    Statement

'''

#print 1 to 10 help of while loop

# n = 1
# while n<=10:
#     print(n)
#     n = n+1

# while True:
#     print('#')



#Fibonacy series in for and while
#Prime Number in for and while
#Palliondrom Number in for and while

# 0 1 1 2 3 5 8 13 21 34 55 89  =

# n = int(input('Enter your fibo series:-'))
#
# a = 0
# b = 1
# count = 0
#
# # a,b,count = 0,1,0
#
# while count < n:
#     print(a)
#     temp = a+b # 1
#     a = b
#     b = temp
#     count = count+1

#for fibo

#
# n = int(input('Enter your fibo series:-'))#10
#
# a,b = 0,1
#
# for i in range(n): # 4
#     print(a) #0,1,1,2,3
#     a,b = b,a+b


#Prime number help of while

# num = int(input('Enter your number:-'))
# def is_prime(num):
#     if num <2:
#         print('Not Prime')
#
#     i = 2
#     while i*i <= num:
#         if num%i == 0:
#             print('Not Prime')
#         i+=1
#     return 'Prime'


# def is_prime(num):
#
#     if num<2:
#         print('Not Prime')
#
#     for i in range(2,int(num**0.5)+1):
#         if num %i == 0:
#             print('Not Number')
#     return 'Prime'
#
# print(is_prime(11))



# 1 to 10

# num = 1
#
# while num<=10:
#     print(num)
#     num = num+1


