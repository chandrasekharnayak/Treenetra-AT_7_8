# class car:
#     def clusth
#     def break
#     def acc
#     def gear
#     def stearing

# method = instance,class,static
# variable = instance,static,local


# class Name: #name always be a Camel Casing
#     '''doc string :- reason written the class'''
#     # functionalies
#
# #class calling :- object reference
#
# var_name = Name

#-------------

# class School:
#
#     def sec_a(self):
#         print('sec_a candidates is scored more the 90%')
#
#     def sec_b(self):
#         print('sec_b candidates is scored more the 80%')
#
#     def sec_c(self):
#         print('sec_c candidates is scored more the 70%')
#
#
# obj = School
# obj.sec_a('self')
# obj.sec_b('self')
# obj.sec_c('self')


#what is consurtor

# class Student:
#
#     def __init__(self,name,age,salary):
#         self.name = name #naveen
#         self.age = age #27
#         self.salary = salary # 90k
#
#     def display(self):
#         print(f'my name is {self.name}, age is {self.age} and salary is {self.salary}')
#
# obj = Student('Naveen',27,90000)
# obj.display()

#Types of method and Variables
#Instance method and Instance variable

# class Student:
#
#     def __init__(self,name,age,salary):
#             self.name = name
#             self.age = age
#             self.salary = salary
#
#     def student_data(self,data):
#         self.data = data
#         print(self.data)
#
#     def student_mark_list(self,mark):
#         self.mark = mark
#         print(self.mark)
#
#     def student_history(self,history):
#         self.history = history
#         print(self.history)
#         print(self.name)
#
#
#
# obj = Student('Naveen',27,90000)
# obj.student_history('old student')
# obj.student_data(4567890)
# obj.student_mark_list(567)


#instance method and variable


# class Bus:
#
#     def __init__(self,capacity,current_passengers=0):
#         self.capacity = capacity
#         self.current_passengers = current_passengers
#
#     def board_passenger(self,num_passenegers):
#         avl_seats = self.capacity - self.current_passengers
#         print(avl_seats)
#
#         if num_passenegers <= avl_seats:
#             self.current_passengers = self.current_passengers+num_passenegers
#             print(f'{num_passenegers} passengers boarded the bus.')
#         else:
#             print(f'Not Enough space for all the passengers')
#         afterbook_seat = avl_seats-num_passenegers
#         print('afterbook_seat:-',afterbook_seat)
#
#
#
#
# obj = Bus(60,15)
# # print(obj.__dict__)
# obj.board_passenger(25)


#self. intance variable
#self instance method
#local variable globally other methods use

#Bus capacity = 60,
# monday- morning--40(book) --- eveng--10(cancel) ,
# tuesday morning- 5(cancel) --- evneg - 8(book)
#how many seat book and how many seat left


# class Bus:
#
#     def __init__(self,capacity=60):
#         self.capacity = capacity
#
#     def monday(self,mon_book,mon_cancel):
#         self.mon_book = mon_book
#         self.mon_cancel = mon_cancel
#         self.capacity = self.capacity-self.mon_book
#         self.capacity = self.capacity+self.mon_cancel
#         # print(f'Monday Report:- Curreent Capaity:- {self.capacity}, Book:- {self.mon_book},Cancel:-{self.mon_cancel}')
#
#     def tuesday(self, tues_book, tues_cancel):
#         self.tues_book = tues_book
#         self.tues_cancel = tues_cancel
#         self.capacity = self.capacity - self.tues_book
#         self.capacity = self.capacity + self.tues_cancel
#         # print(f'Tuesday Report:- Curreent Capaity:- {self.capacity}, Book:- {self.tues_book},Cancel:-{self.tues_cancel}')
#
#     def fina_report(self):
#         print(f'Monday Report:-  Book:- {self.mon_book},Cancel:-{self.mon_cancel}')
#         print(f'Tuesday Report:-  Book:- {self.tues_book},Cancel:-{self.tues_cancel}')
#         print(f'Current Capcity :- {self.capacity}')
#
#
# obj = Bus()
# obj.monday(40,10)
# obj.tuesday(8,5)
# obj.fina_report()

#creat school , name, location,students
#enoroll_students :- addmision students
#tc students
#list_students = []

# class School:
#
#     def __init__(self,name,location):
#         self.name = name
#         self.location = location
#         self.students = []
#
#     def enroll_stidents(self,student_name):
#         self.students.append(student_name)
#         print(f'{student_name} has been enrolled in {self.name} school')
#
#     def issue_tc(self,student_name):
#         if student_name in self.students:
#             self.students.remove(student_name)
#             print(f'{student_name} has been issued a Transfer Certificates from {self.name}')
#         else:
#             print(f'{student_name} is not enrolled in {self.name}')
#
#     def list_of_students(self):
#         for std in self.students:
#             print(std)
#
#
# obj = School('Sri Aurobindo','BBSR')
# obj.enroll_stidents('Rabi')
# obj.enroll_stidents('Maya')
# obj.enroll_stidents('Lucy')
# obj.enroll_stidents('Sankar')
# obj.enroll_stidents('Ganne')
# obj.issue_tc('Sankar')
# obj.list_of_students()


#How to create instance variable
# 1.With help of self parameter inside the constructor
# 2.With help of self parameter inside the instance method
# 3.Outside of the class help of object Reference

# class A:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def aa(self,c):
#         self.c = c
#         #destory
#         del self.c
#
# obj = A(10,20)
# obj.aa(30)
# obj.d = 40
# obj.e = 50
# del obj.b
# print(obj.__dict__)


#Class Method and Static Variables

'''Outside the method but inside of the class, and it's access through whole class know as static variable'''
'''How to access static variable

1.using the class name inside the cons
2.using the class name inside the instance method
3.using the obj reference outside the class.
4.using cls variable inside class method'''
#
# class A:
#
#     a = 10  #Static Variable
#     b = 20  #Static Vriable
#     def int(self):
#         c = 30
#         print(A.a)
#         print(A.b)
#
#
#     @classmethod
#     def clsmethod(cls):
#         return cls.a +cls.b


# obj = A
# # obj.int('s')
# print(obj.clsmethod())

# a = 10
# def int():
#     print(a)
# int()

# class MathOperations:
#
#     factorial_chace = {}
#
#     @classmethod
#     def factorial(cls,n):
#         if n<0:
#             return 'Factorial is not defined for negetive numbers.'
#         elif n ==0 or n==1:
#             return 1
#         elif n in cls.factorial_chace:
#             return cls.factorial_chace[n]
#         else:
#             result = n*cls.factorial(n-1)
#             cls.factorial_chace[n] = result
#             return result
#
# result_5 = MathOperations.factorial(5)
# print(result_5)
# result_3 = MathOperations.factorial(3)
# print(result_3)

#Static Method and Local variable

class A:

    def a(self):
        global c
        c = 20 #local variable

    @staticmethod
    def add(a,b):
        result = a+b
        return result

obj = A
print(obj.add(10,20))

#In a single class using intance,class and static method