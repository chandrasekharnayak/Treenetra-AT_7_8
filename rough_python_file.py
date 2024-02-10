# '''Ternaray Operator'''
# '''Ternaray operator is not allowed multi condition'''
# a = 10
# b = 12
#
# if a>b:
#     print(a)
# else:
#     print(b)
#
# #ternaray operator
# # result if condtion else result
#
# var = a if a>b else b
# print(var)
#
# if 1==1:
#     pass

s= 'i love my india'

count_st = {}

for i in s:
    if i in count_st:
        count_st[i]+=1
    else:
        count_st[i]=1
print(count_st)