"""
If you are not sure if a block of code going to throw errors. For this kind of senario
we use exception handling to do the job and continues the rest of the code
"""
"There are several types of execptions"
"check out https://docs.python.org/3/tutorial/errors.html"
"""
try and except
syntax ->
try:
    code that might throw an error
except:
    code to run if exception occur
finally:
    it will always prints if or if not the code throw an error
"""
".........................................................................................................."
# val = [1, 2, 3, 4, 5]
# try:
#     print(val[4])
# except:
#     print("Index is not found!!")
# print("Thankyou!!")
".........................................................................................................."
# a = int(input("Enter the first value = "))
# b = int(input("Enter the second value = "))
# try:
#     print(a/b)
# except:
#     print(f'You cant divide {a}/{b}')
".........................................................................................................."
'Method to infinitly asking the use to enter any number but zero'

# Method 1
# flag = 1
# while flag == 1:
#     a = int(input("Enter the first value = "))
#     b = int(input("Enter the second value = "))
#     try:
#         print(a / b)
#         flag = 0
#     except:
#         print("Try Again!!")
".........................................................................................................."
# Method 2
# def div():
#     try:
#         a = int(input("Enter the first value = "))
#         b = int(input("Enter the second value = "))
#         print(a/b)
#     except:
#         print("Tryagain!!!")
#         div()
# div()
".........................................................................................................."
"finally block"
# val = [1, 2, 3, 4, 5]
# try:
#     print(val[5])
# except:
#     print("Index is not found!!")
# finally:
#     print("Thankyou!!")
".........................................................................................................."
"We can specify an error in the except block"
# a = 5
# b = 0
# val = [1, 2, 3, 4, 5]
# try:
#     print(a/b)
#     print(val[5])
# except ZeroDivisionError as zd:
#     print("Error =",zd)
#     print("Cannot able to divide a number by zero")
# except IndexError as ie:
#     print("Error =",ie)
#     print("Index Cannot be found")
#print("Completed")
".........................................................................................................."
"We can also raise an exception"
# a = [1, 2, 3, 4, 'a']
# for i in a:
#     if type(i) is not int:
#         raise Exception      
#     else:
#         print(i)
".........................................................................................................."
# a = int(input("Enter a value = "))
# if a > 5:
#     raise Exception
# else:
#     print("The value is",a)
".........................................................................................................."
# a = int(input("Enter a value = "))
# try:
#     if a > 5:
#         raise Exception
#     else:
#         print("The value is",a)
# except:
#     print("Invalid Data!!")
".........................................................................................................."
# randomlist = ['a',0,2,3]
# res = 0
# for i in randomlist:
#     try:
#         res = 1 / i
#         print(f"1/{i} is",res)
#     except:
#         print(f"{i} cant be divided by 1")
".........................................................................................................."