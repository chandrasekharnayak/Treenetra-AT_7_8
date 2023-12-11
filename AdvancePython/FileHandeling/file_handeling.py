#through backend help of some inbuilt function , we handel the all types of file in local,server syetem

#syntax
# open('file_path','mode')
#mode = read-r , write - w,  append - a

# var = open("D:\\TREENETRA\\repitation_class_4.txt","r") #read, read(n), readline, readlines
# data = var.read()
# print(data)

#read :- with help of open function , open a file with read have to only read the data, if the file is not
# avilable then it's showing FileNotFoundError

#read(n)

# var = open("D:\\TREENETRA\\repitation_class_4.txt","r")
# data = var.read(1000)
# print(data)

#readline

# var = open("D:\\TREENETRA\\repitation_class_4.txt","r")
# line1 = var.readline()
# print(line1)
#
# line2 = var.readline()
# print(line2)
#
# line3 = var.readline()
# print(line3)


#readlines

# var = open("D:\\TREENETRA\\repitation_class_4.txt","r")
# data = var.readlines()
# for index,char in enumerate(data):
#     print(index)

#text file-- text, excel,csv
#binary -- imag,video,audio

#write :- override -- write something in a perticular file, if something is already thier then override neither write properly
                    #if the file avialable in the same create a same file
#
# var = open('D:\\TREENETRA\\Treenetra_class_notes\\new_7.txt','w') #write, writelines
# var.write('ertgyuhk;lghbjnklm,trbjkndrtybjhknrdtyivjhbknr6yctvjh')

#append - not obverride

# var = open('D:\\TREENETRA\\Treenetra_class_notes\\new_7.txt','a')
# var.write('jkcnwe\njcedbnwjk\ncbewjk\ngvtyfcdtrj\ndtrfcvtykgvyuhb\n')


#----------------------------------6/12/23-------------

# var = open('D:\\TREENETRA\\Treenetra_class_notes\\new_7.txt','r')
# # print(var.read())
# var.close()
# print(var.closed)


#with statement :-
# with open('D:\\TREENETRA\\Treenetra_class_notes\\new_7.txt','r') as f1:
#     data = f1.read()
#     print(data)
#     # print(f1.closed)
# print(f1.closed)


#tablular format :- csv(comma separate value) ,excel


# data_to_write = [
#     ['Sudeep',32,'SDET',56279,'Jajpur'],
#     ['Sagar',25,'SET',56279,'Konarka'],
#     ['Suraj',28,'SAT',56279,'Puri'],
#     ['Balay',27,'SE',56279,'BBSR'],
# ]


import csv


'''with open('example.txt','r') as read_file1:
    data = read_file1.read()
    data = eval(data)'''

#CSV file write
'''with open('text1.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Age','Occupation','Salary','Address','Pincode'])
    # print(help(writer.writerow))
    writer.writerows(data)
'''

#csv file read

'''with open('text1.csv','r')as file:
    reader  = csv.reader(file)
    for i in reader:
        print(i)'''

#Handel excel sheet help of pandas

import pandas as pd


#data write in excel
'''
data = {
    'Name':['Sudeep','Suraj','Balay'],
    'Age':[29,27,27]
}
data_to_write =pd.DataFrame(data)

data_to_write.to_excel('exmaple.xlsx',index=False)'''


# data for read
'''df = pd.read_excel('exmaple.xlsx')
print(df)'''

#binary file handel

# with open('C:\\Users\\chand\\OneDrive\\Pictures\\Capture.PNG','rb')as file:
#     data = file.read()
#     print(data)



exception handeling
regular
oops





