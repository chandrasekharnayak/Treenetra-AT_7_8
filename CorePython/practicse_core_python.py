'''Core Python Practise'''

#1 How many Data types in python?
#2 Difference between list and tuple?
#3 What is dynamically Typed?
#4 dict and set ?
#5 split vs strip?
#6 Terneary Operator
#7 List and Dictionary Comprehension
#8 Shallow and Deep Copy
#9 Garbage Collection

#Comprehension question list
# 1.Find all of the words in a string that are less than 5 char
# 2.Count the number of space in a string]

#dictionary


#String

'''1 Remove all the duplicates word in a string without use any inbuilt function?'''
# string = 'i love india, going india, going to be , i'
#
# words = string.split() # ['i', 'love', 'india,', 'going', 'india,', 'going', 'to', 'be', ',', 'i']
# unique_words = [] # after compare , only add original elements
# seen_words = set()
#
# for i in words:
#     unique_words.append(i)
#     seen_words.add(i)
#
# result_string = ' '.join(seen_words)
# print(result_string)


'''2 Reverse the string all charcter without using inbuilt fucntion?'''

# string = 'i have string'
# op = 'gnirts evah i'
# print(string[::-1]) # using built in method

# reversed_string = ''
#
# for char in string:
#     reversed_string = char+reversed_string
# print(reversed_string)



'''3 Reverse string words without using inbuilt function?'''
# string = 'i have string'
# op = 'string have i'

'''with using inbuilt function'''
# words = string.split()
# reversed_words = words[::-1]
# result_string = ' '.join(reversed_words)
# print(result_string)

'''without using inbuilt function'''
# string = 'i have string'
# words = []
# word_starts = 0
#
# for index,char in enumerate(string):
#     if char == ' ' or index == len(string)-1:
#         word_ends = index if index == len(string)-1 else index-1 # ternary opeartor#0,5,12
#         print('words_end',word_ends)
#         current_word = string[word_starts:word_ends+1]
#         print('current_word',current_word)
#         words.insert(0,current_word)
#         print('words',words)
#         word_starts = index+1
#         print('word_starts',word_starts)
#
#
# result = ' '.join(words)
# print(result)


'''4 Reverse string words of char without using inbuilt function?'''
# string = 'i have string'
# op = 'gnirts evah i'


'''5 write Pllindrom number and string without use inbulit function?'''''
#cac == cac
#121 == 121
#tac != cat
'''with help of inbuilt'''
# str = input('Enter a string:-')
#
# if str == str[::-1]:
#     print("it's Pallindrom")
# else:
#     print("Not a Pallindrom")

'''with out help of inbuilt'''
# str = input('Enter a string:-')
#
# i = 0#2
# j = len(str)-1 #  2
# #radar -
# while i<j:
#     if str[i] != str[j]:
#         print('Not a Pallindrom')
#     i= i+1
#     j = j-1
# print('Pallindrom')



'''6 write the anagram of string without using inbuilt function?'''
#listen == silent

'''with inbult function'''
# str1 = input('Enter a string:-')
# str2 = input('Enter a string:-')
#
# print(sorted(str1)==sorted(str2))

'''without inbuilt function'''

# str1 = input('Enter a string:-')#silents
# str2 = input('Enter a string:-')
#
# if len(str1)!=len(str2):
#     print('Not a Anagram')
#
# count1 = {}
# count2 = {}
#
# for char in str1:
#     count1[char] = count1.get(char,0)+1
#
# for char in str2:
#     count2[char]= count2.get(char,0)+1
#
# # print(count1)
# # print(count2)
#
# if count1 == count2:
#     print('Anagram')


#7 List and Dictionary Comprehension
#8 Shallow and Deep Copy
#9 Garbage Collection

# Garbage Collection:-

# var1 = 10
# var2 = 10
# var2 = 20
#
# print(id(var1))
# print('var2',id(var2))
# print(id(10))


# Shallow and Deep Copy

import copy

# original_list = [1,[2,3],4]
# duplicate_var = copy.copy(original_list)
#
# original_list[1][0] = 'ABC'
#
# print(original_list)
# print(duplicate_var)

#deep

# original_list = [1,[2,3],4]
# duplicate_var = copy.deepcopy(original_list)
#
# original_list[1][0] = 'ABC'
#
# print(original_list)
# print(duplicate_var)


##7 List and Dictionary Comprehension
# even = []
#
# for i in range(1,11):
#     if i%2==0:
#         even.append(i)
# print(even)

#syntax of list com

# var = [result for element in collenetion if condtion else result]

# var = [ele for ele in range(1,10)]
# print(var)

# var = [ele for ele in range(1,11) if ele%2!=0]
# print(var)


#dictionary comprehension

# di = {for and condition}

# original = {'a':2,'b':3}
#
# # for k,v in original.items():
# #     original[k]= v**2
# # print(original)
#
# var = {k:v**2 for k,v in original.items()}
# print(var)

#Comprehension question list
'''1.Find all of the words in a string that are less than 5 char.
# 2.Count the number of space in a string.'''

# str = 'This a very large city in my village surronding'
#
# # var = [each_word for each_word in str.split() if len(each_word)<5]
#
# var = [element for element in str.split() if len(element)<5]
# print(var)

'''2.Count the number of space in a string.'''
# str = 'This a very large city in my village surronding'
#
# var =sum([1 for char in str if char== ' '])
# print(var)


#-----------------------------List Qurstion -----------------------------------------

# 1. Find the duplicate of list and remove it without using any inbuilt function
# 2. Reverse a list  without using any inbuilt function
# 3. fetch the data in nested list and add them
# 4. Swap a list without using any inbuilt function accending to decending
# 5. [2,[4,5],[4,,5,6],9] add this nested list
# 6. In a list if string their remove it without using any inbuilt function.

'''Find the duplicate of list and remove it without using any inbuilt function'''

# li = [1,2,3,4,1,2,3,5,6,7,7,7,8,8]
# unique_list = []

# for i in li:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

#list comprehension
# var = [unique_list.append(i) for i in li if i not in unique_list]
# print(unique_list)


''' 2. Reverse a list  without using any inbuilt function'''

# li = [1,2,3,4,5]
#
# start_index = 0
# end_index = len(li)-1
#
# while start_index<end_index:
#     li[start_index],li[end_index] = li[end_index],li[start_index]
#     start_index = start_index+1
#     end_index = end_index-1
#
# print(li)

'''# 3. fetch the data in nested list and add them'''

# li = [
#     [1,2,3],
#     [3,4,5],
#     [9,8,7]
# ]
#
# for element in li:
#     for i in element:
#         print(i)





'''4. Swap a list without using any inbuilt function accending to decending'''

# li = [3,1,4,2,5] # 3>1, 3>4, 3>2
#
# for i in range(len(li)):#i = 0,1,2,3,
#     for j in range(i+1,len(li)):#j=1,2,3 , j = 2,3  j = 3
#         if li[i]>li[j]:
#             li[i],li[j] = li[j],li[i]
# print(li)


'''# 5. [2,[4,5],[4,5,6],9] add this nested list'''

# li = [2,[4,5],[4,5,[6,8]],9]
#
# def recursive_sum(li):
#     sum = 0
#     for i in li:
#         if isinstance(i,list):
#             sum = sum + recursive_sum(i)
#         else:
#             sum = sum+i
#     return sum
# print(recursive_sum(li))
#

li = [12,13,1,4,'89','uo'] # don's use remove










