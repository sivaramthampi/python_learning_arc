"""
we can handling multiple files like csv, text, json, images, xml etc with python

x = for create a new file
r = to read a file
w = for write a file  --> It will create a file if the file is not exists
a = for append a file
b = for binary mode

# Steps to follow
1) --> Open the file
2) --> Do the operation
3) --> Close the file
"""
".........................................................................................................."
"Creating and writing a file"
# try:
#     f = open("text1.txt",'x')   # To create a file 
# except:
#     print('Already exists')
# f = open("text1.txt",'w')       # Setting to write mode
# f.write("Line 1\nLine 2\nLine 3") 
# f.close()
"NB:- if you are creating a file by default it will create a file on the same directory/folder"
"add path and name to the argument to open/write/create/read the file "
"""f = open("E:\\Sivaram",'w') """
".........................................................................................................."
"To read a file"
# f = open('sample_read.txt','r') # Setting to read 
# print(f.read())
# f.close()
".........................................................................................................."
"To append a text to file (it will not replace any content of the file it will append to it)"
# file = open('sample_append.txt','a')
# b =str(input("Enter something to append = "))
# file.write(f"Appended = {b} \n")
# file.close()
".........................................................................................................."
"To read lines in a text file"
# file = open("line_read.txt",'r')
# print(file.readline())  # 'readline()' only prints the first line
# print(file.tell())      # To identify where the cursor/pointer is
# file.seek(0)            # To reset the cursor tto the given index position
# print(file.readline(4)) # It will take index of the text
# file.seek(0)
# a = file.readlines()    # 'readlines()' will return every lines of a text file and stores in as a list
# print(a)   
# file.close()
".........................................................................................................."
# "there is a method called 'with open' it will automatically close the file"
# with open("line_read.txt",'r') as f:
#     a = f.readlines()
#     for i in a:  # To print line by line
#         print(i)
".........................................................................................................."
"to delete a file using os function"
# import os 
# with open('deleting_file.txt','w') as file:
#     file.write("hello")
# with open('deleting_file.txt','r') as file:
#     print(file.read())
# os.remove('deleting_file.txt')
"you cant see the file beacause it is instantly deleting the file"
".........................................................................................................."
"to create and read a csv file"
# with open('sample_csv.csv','w') as file:
#     file.write("Hello world")
# with open('sample_csv.csv','r') as file:
#     print(file.read())
".........................................................................................................."
"to read a csv file using pandas"
"NB: install python module (pip install pandas)"
# import pandas as pd
# f = pd.read_csv('sample_csv.csv')
# print(f)
".........................................................................................................."