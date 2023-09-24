"""
Function are a block of code which only execute when we call the function
Function can be reuse any time
"""
".........................................................................................................."
# def hello():               # This is a user-defined functions
#     print("Hello world")   # Declaring a function

# hello()                    # Calling Function
".........................................................................................................."
# def sample():
#     a = 5
#     b = 6
#     sum = a + b           # To find sum of a two numbers using function
#     print(sum)

# sample()
".........................................................................................................."
# def sample():
#     val = 8
#     sum = 0
#     i = 0
#     while i <= val:       # To find sum of a numbers using function
#         sum = sum + i
#         i += 1
#     print(sum)

# sample()
".........................................................................................................."
# def sample(a): # Parameters
#     val = a
#     sum = 0
#     i = 0
#     while i <= val:       # To find sum of a numbers using function
#         sum = sum + i
#         i += 1
#     print(sum)
# sample(10)     # Arguments
# sample(100)
# sample(50)
".........................................................................................................."
# def add(a, b):
#     sum = a + b
#     print(sum)

# add(10, 20) 
"""
This is a positional argument passing 
It assign to the parameters based on position
"""
".........................................................................................................."
# def Diff(a,b):
#     diff = a - b
#     print(diff)
# Diff(b=4,a=3)
"""
This is a keyword argument passing 
It assign to the parameters based on the keywords
"""
".........................................................................................................."
""
# Arbitrary argument passing
# we can pass multiple values in a single parameter - use an asterisk before the keyword
# def val(*a):       
#     ls = []
#     for i in a:
#         ls.append(i)
#     print(ls)
# val(1, 2, 3, 4, 5, 6)
".........................................................................................................."
# def val(val1,val2,*a):
#     ls = []
#     for i in a:
#         ls.append(i)
#     print(ls)
# val(1, 2, 3, 4, 5, 6)
".........................................................................................................."
# Keyword Arbitrary argument passing
# def vals(**a):
#     print(a)
# vals(a = "Hello", b = "World", c = "Python", d = "Welcome")  # It will store as a dict
".........................................................................................................."
# def vals(**a):
#     ls = []
#     for i, j in a.items():
#         ls.append(i)
#         ls.append(j)
#     print(ls)
# vals(a = "Hello", b = "World", c = "Python", d = "Welcome")
".........................................................................................................."
# To find factorial using for loop
# def fact(a):
#     res = 1
#     for i in range(1, a + 1):
#         res += i
#     print(f"Factorial of {a} is {res}")
# inp = int(input("Enter a number = ")) 
# if inp < 0:
#     print("No factorial. Enter a positive value!")
# else:
#     fact(inp)
".........................................................................................................."
# To find factorial using while loop
# def fact(n):
#     t = n
#     f = 1
#     if n<0:
#         print("No Factorial")
#     else:
#         while n>0:
#             f *= n
#             n-=1
#         print(f"Fact of {t} is",f)
# a = int(input("Enter a number = "))
# fact(a)
".........................................................................................................."
# To find factorial using return function
# def fact(n):
#     t = n
#     f = 1
#     if n<0:
#         print("No Factorial")
#     else:
#         while n>0:
#             f *= n
#             n-=1
#         return f
# a = int(input("Enter a number = "))
# b = fact(a)
# print(b)
".........................................................................................................."
# Multiple function integration 
# def fact(n):
#     t = n
#     f = 1
#     if n<0:
#         print("No Factorial")
#     else:
#         while n>0:
#             f *= n
#             n-=1
#         return f
# def out(va):
#     print(f"The output is = {fact(va)}")
# a = int(input("Enter a number = "))
# out(a)
".........................................................................................................."
# To check odd or even using function and return statements
# def Iseven(a):
#     if a % 2 == 0:
#         return True
#     return False

# print(Iseven(5))
".........................................................................................................."
# def Iseven(e):
#     c = []
#     for i in e:
#         if i % 2 == 0:
#             c.append(i)
#     return c
# b = [23, 3, 45, 67, 66, 89, 88, 24]
# print("Even numbers are \n",Iseven(b)) 
".........................................................................................................."
# Anonymus Function in python is called lambda
"It doesnt need any name but there are some limitations"
# a = lambda a,b: a + b
# import math
# b = lambda a: math.sqrt(a)
# print(a(23,24))
# print(b(25))
".........................................................................................................."
# print((lambda a, b, c, d:a + b + c + d)(20, 20, 20, 20)) # Another lambda function
".........................................................................................................."
# a = lambda a,b: a if a>b else b # Return greatest value using lambda
# print(a(12, 10))
".........................................................................................................."
# a = [2, 3, 4, 5, 6]
# b = []
# sqr = lambda a : a ** 2
# for i in a:
#     b.append(sqr(i))        # Squaring a number using lambda 
# print(b)
".........................................................................................................."
# def func(v=2):
#     c = v * 2
#     return c
# x = 2
# high = lambda x, func:x + func
# print(high(3,func()))
".........................................................................................................."
# Composision Functions
"passing a function to another function's argument"
# def add(a):
#     return a + 2
# def mul(b):
#     return b * 2
# print("Result = ",mul(add(5)))
".........................................................................................................."
# a = lambda x, y:f"{x} is smaller than {y}" if x<y \
#     else f"{x} is greater than {y}" if x>y \         # Checking greatest value among two numbers using lambda
#     else f"{x} is smaller than {y}"
# print(a(22, 32))
".........................................................................................................."
# Checking greatest value among three numbers using lambda
# gr = lambda x,y,z : f"{x} is greater than {y} and {z}" if x>y and x>z \
#     else f"{y} is greater than {x} and {z}" if y>z \
#     else f"{z} is greater than {x} and {y}" 
# a = int(input("Enter 1st number = "))
# b = int(input("Enter 2nd number = "))
# c = int(input("Enter 3rd number = "))
# print(gr(a,b,c))
".........................................................................................................."
# Factorial of a number using recursive function
# def fact(a):
#     if a == 1:
#         return a
#     else:
#         return a * fact(a - 1)
# inp = int(input("Enter a value = "))
# if inp < 0:
#     print("No Factorial!")
# elif inp == 0:
#     print(f"Factorial of {inp} is 1")
# else:
#     print(f"Factorial of {inp}! is {fact(inp)}")
".........................................................................................................."
# To find sum of a list using recursion
# a = [2, 3, 4, 5]
# def ls_sum(num):
#     if len(num) == 1:
#         return num[0]
#     else:
#         return num[0] + ls_sum(num[1:])
# print(ls_sum(a))
".........................................................................................................."
# To find sum of a mixed dimentional list using recursion
# def is_sum(a):
#     f = 0
#     for i in a:
#         if type(i) == type([]):
#             f = f + is_sum(i)
#         else:
#             f = f + i
#     return f
# b = [1,2,[3,4],[5,6]]
# print(is_sum(b))
".........................................................................................................."
".........................................................................................................."
# Enumeration Function 
"""converts a data collection object into an enumerate object. 
Enumerate returns an object that contains a counter as a key for 
each value within an object"""

# a = ['Apple', 'Orange', 'Grapes', 1, 2, 3, True]   # List Enumeration
# for i,j in enumerate(a):
#     print(f"index Position = {i} || Value = {j} ")
".........................................................................................................."
# a = {'Apple', 'Orange', 'Grapes', 1, 2, 3, True}   # Set Enumeration
# for i,j in enumerate(a):
#     print(f"index Position = {i} || Value = {j} ")
".........................................................................................................."
# a = ('Apple', 'Orange', 'Grapes', 1, 2, 3, True)   # Tuple Enumeration
# for i,j in enumerate(a):
#     print(f"index Position = {i} || Value = {j} ")
".........................................................................................................."
# a = {1:'Apple', 2:'Orange', 3:'Grapes', 4:1, 5:2, 6:3, 7:True}   # Dict Enumeration
# for i,j in enumerate(a):        
#     print(f"index Position = {i} || Value = {j} ")    # In the dict enumeration the value will be the key
".........................................................................................................."
".........................................................................................................."
# Map, Reduce and Filter 

# Map
"Map function help to repeat a single operating function for a sequance - map(function <without brackets>, sequence)"
# def Sqr(a):                 # To find square of a number
#     return a * a 
# val = [2, 3, 4]
# print(list(map(Sqr, val)))  # Must convert to data sequence else it will return as an object
".........................................................................................................."
# print(tuple(map(lambda i:i * i, [2,3,4])))  # Same Program much simpler and in tuple
".........................................................................................................."
# a = [2, 3, 4]
# b = [5, 6, 7] # It will print the sum of indices of every variable 
# c = [1, 8, 7]
# print(list(map(lambda i, j, k : i + j + k, a, b, c))) 
".........................................................................................................."
# Filter Function
"It help to filter value - filter(function, sequence)"
# print(list(filter(lambda i:i % 2 == 0,range(1, 11))))
# def main(a):
#     if a % 2 == 0:
#         print("True")
# print(list(filter(main,(2, 3, 4, 5, 6)))) 
".........................................................................................................."
# Reduce Function

"To use reduce function we must import function tools aka functools"
# import functools
# num = [1, 2, 3, 4, 5]
# b = functools.reduce(lambda x,y:x+y,num)
# print(b)
".........................................................................................................."
# import functools
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(functools.reduce(min,nums))
".........................................................................................................."
# import functools
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(functools.reduce(max,nums))
".........................................................................................................."
# import functools
# def main(a, b):
#     return a if a < b else b
# a = [1, 2, 4, 5, 6, 7, 8]      # To find minumum value of a list using reduce
# print(functools.reduce(main,a))
".........................................................................................................."
# import functools
# def main(a, b):
#     return a if a > b else b
# a = [1, 2, 4, 5, 6, 7, 8]      # To find max value of a list using reduce
# print(functools.reduce(main,a))
".........................................................................................................."
# reduce(function, sequence, initial) # We can set an initial value
# import functools
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(functools.reduce(lambda i, j:i + j, a, 100)) # We can set a value
".........................................................................................................."