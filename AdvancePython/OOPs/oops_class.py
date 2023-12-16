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

class Student:

    def __init__(self,name,age,salary):
            self.name = name
            self.age = age
            self.salary = salary

    def student_data(self,data):
        self.data = data
        print(self.data)

    def student_mark_list(self,mark):
        self.mark = mark
        print(self.mark)

    def student_history(self,history):
        self.history = history
        print(self.history)
        print(self.name)



obj = Student('Naveen',27,90000)
obj.student_history('old student')
obj.student_data(4567890)
obj.student_mark_list(567)



