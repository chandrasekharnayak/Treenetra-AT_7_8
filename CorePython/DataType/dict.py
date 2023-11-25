# Name  Rollno  Sec
# A       1       'A'
# B       2       'B'
# C       3       'C'
# C       4       'C'Ke
#
# dict = {Key:Value}
# key is always unique but may be value is same.
# key always be a immutable data type

# dic = {'Name':'A','Rollno':1,'Sec':'A','Name':'Z'}
# print(type(dic))
# print(dic)

# dic1 = {[1,2,3]:[23,45,67]} #key: list and value : list
# dic2 = {(1,2,3):[23,45,67]}
# dic3 = {1:1}
# dic4 = {'Name':'A'}
# dic5 = {{1,2,3}:{1,2,3}}
# dic6 = {frozenset({1,2,3}):{1,2,3}}

di = {'Name':'Chandra','Sec':'C','Rol':23}
#var['key']
# print(di['Sec'])

# di['Sec']='B'
# print(di)

# print(dir(di))

# {k0:v0,k1:v1}
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
# 'pop', 'popitem', 'setdefault', 'update', 'values']

# di.clear()
# print(di)

# se = {10,20,30,40,40,50}
# print(se)

# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# # print(di['Name'])
# di['Name']='Rajesh'
# print(di)

# di = {immutable:mutable}


#clear

# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# di.clear()
# print(di)

#copy

# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
#
# di2 = di.copy()
# print(di2)


#fromkeys
# sub = ('Math','Science','Social Sc.')
# mark = 82
#
# krishna = dict.fromkeys(sub,mark)
# print(krishna)

#get
#
# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# print(di.get('Name'))
# print(di.get('Age'))

#items

# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# print(di.items())

#keys

# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# print(di.keys())

#values

# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# print(di.values())

#setdeafult

# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# di.setdefault('Pincode',751002)
# print(di)


#update
# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# new_data = {'Post':'Khandagiri','Dict':'Khordha','Pincode':751003}
#
# di.update(new_data)
# print(di)

#pop

# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# di.pop('Salary')
# print(di)

#popitem
# di = {'Name':'Suv','Age':21,'Salary':890000,'Address':'Suv'}
# di.popitem()
# print(di)


#None

# def data():
#     a = 10
#     print()
# print(data())

