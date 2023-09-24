""""
class employee():    Class
    pass
em = employee()      Object
print(em)
"""

"Manual Way of creating class and objects"

# class employee():
#     pass
# emp1 = employee()
# emp2 = employee()

# emp1.firstname = "Sivaram"
# emp1.lastname = "thampi"
# emp1.email = "sivaramthampi@example.com"
# emp1.phone = "9123456780"
# emp1.fullname = emp1.firstname + " " + emp1.lastname

# emp2.firstname = "MDS"
# emp2.lastname = "904"
# emp2.email = "mds@example.com"
# emp2.phone = "9123456780"
# emp2.fullname = emp1.firstname + " " + emp1.lastname



# print("First name of employee 1 =",emp1.firstname)
# print("Last name of employee 1 =",emp1.lastname)
# print("Full name of employee 1 =",emp1.fullname)
# print("Email of employee 1 =",emp1.email)
# print("Phone Number of employee 1 =",emp1.phone)
# print()
# print("First name of employee 2 =",emp2.firstname)
# print("Last name of employee 2 =",emp2.lastname)
# print("Full name of employee 2 =",emp2.fullname)
# print("Email of employee 2 =",emp2.email)
# print("Phone Number of employee 2 =",emp2.phone)
".........................................................................................................."
".........................................................................................................."
"Manual Way of creating class and objects"

# class employee():
#     def __init__(self,firstname,lastname,income):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.income = income
#         self.email = str(firstname+lastname+"@gmail.com").lower()

# emp1 = employee('Sivaram','thampi','28000')
# emp2 = employee('MDS','904',None)

# print("First name of employee 1 =",emp1.firstname)
# print("Last name of employee 1 =",emp1.lastname)
# print("Income of employee 1 =",emp1.income)
# print("Email of employee 1 =",emp1.email)
# print()
# print("First name of employee 2 =",emp2.firstname)
# print("Last name of employee 2 =",emp2.lastname)
# print("Income of employee 2 =",emp2.income)
# print("Email of employee 2 =",emp2.email)
".........................................................................................................."
".........................................................................................................."
"To print full details of a employee using a methods in a class"
# class employee():
#     def __init__(self,firstname,lastname,income):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.income = income
#         self.email = str(firstname+lastname+"@gmail.com").lower()
#     def full_details(self):
#         print(f"First name of employee =",self.firstname)
#         print(f"Last name of employee =",self.lastname)
#         print(f"Income of employee =",self.income)
#         print(f"Email of employee =",self.email)
#     def fullname(self):
#         print(f"Fullname ={self.firstname} {self.lastname}")
    
# emp1 = employee('Sivaram','thampi','28000')
# emp2 = employee('MDS','904',None)
# emp1.fullname()
# emp1.full_details()
# print()
# emp2.fullname()
# emp2.full_details()
".........................................................................................................."
".........................................................................................................."
"Another way to fetch details in a class"
# class employee():
#     def __init__(self,firstname,lastname,income):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.income = income
#         self.email = str(firstname+lastname+"@gmail.com").lower()
#     def full_details(self):
#         print(f"First name of employee =",self.firstname)
#         print(f"Last name of employee =",self.lastname)
#         print(f"Income of employee =",self.income)
#         print(f"Email of employee =",self.email)
#     def fullname(self):
#         print(f"Fullname ={self.firstname} {self.lastname}")
    
# emp1 = employee('Sivaram','thampi','28000')
# emp2 = employee('MDS','904',None)
# employee.fullname(emp1)
".........................................................................................................."
".........................................................................................................."
"To print a method of every object"
# class employee():
#     def __init__(self,firstname,lastname,income):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.income = income
#         self.email = str(firstname+lastname+"@gmail.com").lower()
#     def full_details(self):
#         print(f"First name of employee =",self.firstname)
#         print(f"Last name of employee =",self.lastname)
#         print(f"Income of employee =",self.income)
#         print(f"Email of employee =",self.email)
#     def fullname(self):
#         print(f"Fullname ={self.firstname} {self.lastname}")
    
# emp1 = employee('Sivaram','thampi','28000')
# emp2 = employee('MDS','904',None)
# emp3 = employee('Agent','47','230000')
# listed = [emp1,emp2,emp3]
# for i in listed:
#     i.full_details()
".........................................................................................................."
".........................................................................................................."
# class employee():
#     def __init__(self,fname,lname,pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
# emp1 = employee("Sivaram","thampi",20000)
# emp1.pay += emp1.pay * 1.04
# print(emp1.pay)
".........................................................................................................."
".........................................................................................................."
"To increase a certain amount"
# class employee():
#     def __init__(self,fname,lname,pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#     def payincrese(self,i):
#         return self.pay * i
# emp1 = employee("Sivaram","thampi",20000)
# emp2 = employee("Stephin","Joseph",50000)
# print(f"{emp1.fname} got a pay increased by 4% ("+str(emp1.payincrese(1.04))+")")
# print(f"{emp2.fname} got a pay increased by 4% ("+str(emp2.payincrese(1.04))+")")
".........................................................................................................."
".........................................................................................................."
# class employee():
#     def __init__(self,fname,lname,pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#     def payincrese(self,i):
#         return self.pay * i
# emp1 = employee("Sivaram","thampi",20000)
# emp2 = employee("Stephin","Joseph",50000)
# print(f"{emp1.fname} got a pay increased by 4% ("+str(emp1.payincrese(1.04))+")")
# print(f"{emp2.fname} got a pay increased by 4% ("+str(emp2.payincrese(1.04))+")")
".........................................................................................................."
".........................................................................................................."
# class employee():
#     a = 52
#     def __init__(self,fname,lname,pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
# emp = employee()
# emp.a = 78
# print(employee)
".........................................................................................................."
".........................................................................................................."
# class employee():
#     def __init__(self,first,last,age):
#         self.first = first
#         self.last = last
#         self.age = age
# a = employee("Sivaram", "Thampi", 20)
# print(a.__dict__)
".........................................................................................................."
".........................................................................................................."
# class employee():
#     raised = 1.05
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#     def raiseamount(self):
#         return self.pay*self.raised
# a = employee("Sivaram","thampi",20000)
# b = employee("MDS","904",50000)
# c = employee(None,None,25000)
# a.raised = 1.10
# print(f"Employee {a.first} got a raise from {a.pay} to {a.raiseamount()} about {a.raised}%")
# b.raised = 1.09
# print(f"Employee {b.first} got a raise from {b.pay} to {b.raiseamount()} about {b.raised}%")
# employee.raised = 1.06 
# print(f"Other employees got a raise from {c.pay} to {c.raiseamount()} about {c.raised}%")
".........................................................................................................."
".........................................................................................................."
# class dummy():
#     "This is a dummy class data"
#     a = "Hello"
#     def b():
#         "This is a dummy method data"
#         pass
# a = dummy()
# print(a.__class__) # Return which class the particular object contains
# print(isinstance(a,dummy)) # To check what class instance of this object is
# print(dummy.__doc__)
# print(dummy.b.__doc__)
".........................................................................................................."
".........................................................................................................."
" First class functions "
# def age(a):
#     print(f"Your age is {a}")
# a = age
# a(20)
".........................................................................................................."
# def sqr(a):
#     return a * a
# f = sqr
# print("Square =",f(3))
".........................................................................................................."
# def square(i):
#     return i * i
# def listed(a, b):
#     list1 = []
#     for k in a:
#         list1.append(b(k))
#     return list1
# a = listed([i for i in range(5,41)],square)
# print(a)
".........................................................................................................."
".........................................................................................................."
"""
Closures - Python closure is a nested function that allows us to access 
variables of the outer function even after the outer function is closed.
"""
# def a():
#     msg = "Hello"
#     def b():
#         print(msg," world")
#     return b
# c = a()
# c()
".........................................................................................................."
# def a(x):
#     def b():
#         print("Hello",x)
#     return b
# c = a("MDS")
# c()
".........................................................................................................."
# def htmltag(tag):
#     def wrap(m):
#         print(f"<{tag}> {m} </{tag}>")
#     return wrap
# a = htmltag("p")
# a("Hello beautiful people")
".........................................................................................................."
".........................................................................................................."
# def sum(a,b):
#     print(a+b)
# stephin = sum
# stephin(1,3)
".........................................................................................................."
# def decorarted_function(original_function):
#     def wrapper_function():
#         print(f"Wrapper executed before {original_function.__name__}")
#         return original_function()
#     return wrapper_function

# def display():
#     print("This is display function")

# wrapped = decorarted_function(display)
# print(wrapped.__name__)
# wrapped()
".........................................................................................................."
".........................................................................................................."
"Decorators"
# def decorarted_function(original_function):
#     def wrapper_function():
#         print(f"Wrapper executed before {original_function.__name__}")
#         return original_function()
#     return wrapper_function
# @decorarted_function
# def display():
#     print("This is display function")
# display()
".........................................................................................................."
# def main(a):
#     def sub2():
#         print("Hello world")
#         a()
#     return sub2
# @main
# def sub():
#     print("Semi function triggered")
# sub()
".........................................................................................................."
# def main(fun):
#     def vals():
#         a = int(input("Enter 1st number = "))
#         b = int(input("Enter 2nd number = "))
#         return fun(a,b)
#     return vals
# @main
# def sum(x,y):
#     print("Sum = ",str(x+y))
#     return "Completed"
# print(sum())
".........................................................................................................."
# def main(o_function):
#     def ins_main(*a):
#         return o_function(*a)
#     return ins_main
# @main
# def sub(a,b):
#     print(f"a is {a} \nb is {b}")
# sub(22,33)
".........................................................................................................."
# class decorator():
#     def __init__(self,mainfunc):   # Main Function
#         self.mainfunc = mainfunc

#     def __call__(self,*a,**b):
#         return self.mainfunc(*a,**b)   # Sub Function
# @decorator
# def sub(name,age):
#     print(f"Hello {name} and your age is {age}")
# sub("MDS",22) # This will pass to *a
# sub(name="MDS",age=22) # This will pass **b 
".........................................................................................................."
# import time
# def current(function):
#     def num(n):
#         starting = time.time()
#         function(n)
#         ending = time.time()
#         print(f"Time diff is {(ending-starting)*1000}")
#     return num
# @current
# def sqr(number):
#     res = []
#     for num in number:
#         res.append(num*num)
#     return res
# @current
# def cube(number):
#     res = []
#     for num in number:
#         res.append(num**3)
# a = [i for i in range(1,20001)]
# sqr(a)
# cube(a)
".........................................................................................................."
# class sample():
#     value = "Hello world"
#     def __init__(self):
#         print("Welcome!")
#     def getvalue(self):
#         value = "Hello Universe"
#         print("OP:",self.value)
# s = sample()
# a = sample()
# s.getvalue()
# s.value = "Hello Python"
# print(s.value)
# sample.value = "Hello MDS"
# print(sample.value)
# print(a.value)
".........................................................................................................."
# "To del an object"
# class main():
#     def printing(self):
#         print("Hello world")
# a = main()
# b = main()
# a.printing()
# b.printing() 
# del b      # To delete an object
".........................................................................................................."
# class employee():
#     raise_am = 1.04
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.mail = first+'.'+last+'@gmail.com'
#     def fulldet(self):
#         return f"{self.first}\n{self.last}\n{self.mail}\n{self.pay}"
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     def raiseamt(self):
#         return self.pay*self.raise_am
#     @classmethod
#     def setraise_amt(cls,am):
#         cls.raise_am = am
# emp1 = employee("Sivaram","Thampi",60000)
# emp2 = employee("MDS","904",40000)
# print(emp1.raiseamt())
# employee.setraise_amt(1.10)
# print(emp1.raiseamt())
# a = "dev-hel-320000"
# first,last,pay = a.split('-')
# emp3 = employee(first, last, pay)
# print(emp3.pay)
".........................................................................................................."
# class employee():
#     raise_am = 1.04
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = int(pay)
#         self.mail = first+'.'+last+'@gmail.com'
#     def fulldet(self):
#         return f"{self.first}\n{self.last}\n{self.mail}\n{self.pay}"
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     def raiseamt(self):
#         return self.pay*self.raise_am
#     @classmethod
#     def setraise_amt(cls,am):
#         cls.raise_am = am
#     @classmethod
#     def get_details(cls,val):
#         first, last, pay = val.split('-')
#         return cls(first,last,pay)
# emp1 = employee("Sivaram","Thampi",60000)
# emp2 = employee("MDS","904",40000)
# print(emp1.raiseamt())
# employee.setraise_amt(1.10)
# print(emp1.raiseamt())
# a = "Sivaram-Thampi-40000"
# emp3 = employee.get_details(a)
# print(emp3.pay)
# b = "Stephin-Joseph-50000"
# emp4 = employee.get_details(b)
# print(emp4.first,emp4.last)
".........................................................................................................."
# class employee():
#     raise_am = 1.04
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.mail = first+'.'+last+'@gmail.com'
#     def fulldet(self):
#         return f"{self.first}\n{self.last}\n{self.mail}\n{self.pay}"
#     def raiseamt(self):
#         return self.pay*self.raise_am
#     @staticmethod
#     def getweek(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return "A weekend"
#         return "Work day" 
# part1 = employee("Sivaram","Thampi",32000)
# import datetime
# date1 = datetime.date(2023,1,28)
# date2 = datetime.date(2023,2,3)
#  
# print(part1.getweek(date2))
".........................................................................................................."
# class employee:
#     def __init__(self, name, salary,project_name):
#         self.name = name
#         self.salary = salary
#         self.project_name = project_name
#     @staticmethod
#     def gather_requirment(project_name):
#         if project_name == 'ABC project':
#             requirment = ['task_1','task_2','task_3']
#         else:
#             requirment = ['task_1'] 
#         return requirment
#     def work(self):
#         requirment = self.gather_requirment(self.project_name)
#         for task in requirment:
#             print('completed',task)

# emp = employee('kelly',12000,'project')
# emp.work()
".........................................................................................................."
"__repr__"
# class main():
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     def __repr__(self):
#         return self.first
# a = main("Sivaram","Thampi")
# print(a)
".........................................................................................................."
"__str__"
# class main():
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     def __str__(self):
#         return self.fullname()
# a = main("Sivaram","Thampi")
# print(a)
".........................................................................................................."
# import datetime
# today = datetime.date.today()
# print(today)
# print(str(today))
# print(repr(today))
".........................................................................................................."
# print(int.__add__(20,10))
# print(str.__add__('a','b'))
".........................................................................................................."
"Operator Overloading"
# class main():
#     def __init__(self,val):
#         self.val = val
#     def value(self):
#         return self.val
#     def __add__(self,val):
#         return self.value() + val.value()
#     def __sub__(self,val):
#         return self.value() - val.value()
#     def __len__(self):
#         return len("Sivaram Thampi")
# a = main(23)
# b = main(33)
# print(a + b)
# print(a - b)
# print(len(a))
".........................................................................................................."
# class main():
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     def fullname(self):
#         return self.first,self.last
#     def mail(self):
#         return (self.first + self.last + "@gmail.com").lower()
    
# a = main("Sivaram","Thampi")
# print("Mail before changing {",a.mail(),'}')
# a.first = "MDS"
# a.last = "904"
# print(a.mail())
".........................................................................................................."
"Property Deorator (Getters)"
# class add():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     @property
#     def add(self):
#         return self.a + self.b  
#     @property
#     def sub(self):                                   # Getter
#         return self.a - self.b
# b = add(55,20)
# print(b.add)
# print(b.sub)    
".........................................................................................................."
"Setters"
# class main():
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     @property
#     def fullname(self):
#         return self.first,self.last
#     def mail(self):
#         return (self.first + self.last + "@gmail.com").lower()
#     @fullname.setter
#     def fullname(self,name):
#         first,last = name.split()
#         self.first = first
#         self.last = last
# a = main("Sivaram","Thampi")
# print(a.fullname)
# a.fullname = "MDS 904"
# print(a.fullname)
".........................................................................................................."
"Deleters"
# class main():
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     @property
#     def fullname(self):
#         return self.first,self.last
#     @fullname.deleter
#     def fullname(self):
#         self.first = None
#         self.last = None
# a = main("Sivaram","Thampi")
# print(a.fullname)
# del a.fullname
# print(a.fullname)
".........................................................................................................."
# ls = [1,2,3,4,5,6,7]
# for i in ls: # Itreble
#     print(i)

# ls = [1,2,3,4,5,6,7]
# print(dir(ls))  # If the list contains only __iter__ it is an Itreble
# val = iter(ls)
# print(dir(val)) # If the list contains __iter__ and __next__ it is an iterator

# ls = [1,2,3,4,5,6]
# ls1 = iter(ls)
# print(next(ls1))
# print(next(ls1))
# print(next(ls1))
# print(next(ls1))
# print(next(ls1))
# print(next(ls1))

# ls = [1,2,3,4,5,6]
# ls1 = iter(ls)
# print(next(ls1))
# print(next(ls1))
# for i in ls1:    # It will continue from the last (next) point
#     print(i)

"Using Execption handling"
# ls = [i for i in range(0,21)]
# val = iter(ls)
# while True:
#     try:i = next(val);print(i)
#     except StopIteration:break
# print("Stopped")
".........................................................................................................."
# class localrange():
#     def __init__(self,start,stop):
#         self.start = start
#         self.stop = stop
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration
#         i = self.start
#         self.start += 1
#         print(i) 

# n = localrange(1,21)
# while True:
#     try:next(n)
#     except:print("Finished");break
".........................................................................................................."
# def localrange(start):
#     i = start
#     while True:
#         yield i  # Used instead of return - The method is known as Generators
#         i += 1
# a = localrange(1)
# print(next(a))
# print(next(a))
# print(next(a))
".........................................................................................................."
# def a():
#     yield 1
#     yield 2
#     yield 3
#     yield "Hello"
# b = a()
# for i in b:
#     print(i)
".........................................................................................................."
"Pass a sentence to a function/class and print every words in it using next()"
# a = "Hello my name is sivaram"
# def main(b):
#     c = b.split()                                      # Using Function
#     d = iter(c)
#     return d
# r = main(a)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

# a = "Hello my name is sivaram"
# class words():
#     def __init__(self,sen):                           # Using class
#         self.sen = sen
#         self.word = sen.split()
#         self.index = 0
#     def __next__(self):
#         if self.index >= len(self.word):
#             raise StopIteration
#         i = self.index
#         self.index += 1
#         return self.word[i]
# word = words(a)
# print(next(word))
# print(next(word))
# print(next(word))
# print(next(word))
# print(next(word))
".........................................................................................................."
# a = "Hello my name is sivaram"
# def main(a):
#     b = a.split()
#     c = iter(b)
#     for i in range(0,len(b)):
#         yield next(c)
# b = main(a)
# for i in b:
#     print(i)

# a = "Hello my name is sivaram"
# def main(a):
#     for i in a.split():
#         yield i
# b = main(a)
# for i in range(0,5):
#     print(next(b))
".........................................................................................................."
# a = [i for i in range(10,21)]
# print(a)
# def main(a):
#     for i in a:
#         yield i*i
# b = main(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
".........................................................................................................."
# a = (i for i in range(10,21)) # Tuple comprehension is generator by default
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))