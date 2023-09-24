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
# class dev(employee):
#     raise_am = 1.10

# part1 = dev("Sivaram","Thampi",32000)
# print(part1.first)
# print(part1.raiseamt())
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
# class dev(employee):
#     def __init__(self, first, last, pay, lang):
#         super().__init__(first, last, pay)
#         self.lang = lang

# part1 = dev("Sivaram","Thampi",32000, "Kalaam")
# print(part1.first)
# print(part1.lang)
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
# class dev(employee):
#     def __init__(self, first, last, pay, lang):
#         super().__init__(first, last, pay)
#         self.lang = lang
# class manager(employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             employees = []
#         else:
#             self.employees = employees
#     def empadd(self,emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#     def printdev(self):
#         for i in self.employees:
#             print("-->> "+i.first,i.last)
#     def removedev(self,emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#         else:
#             print("Developer not found!!")
# dev1 = dev("Sivaram","Thampi",40000,'C++')
# dev2 = dev("Joel","McAdams",70000,"Swift")
# man = manager("MDS","904",None,[dev1,dev2])
# dev3 = dev("Stephin","Joseph",70000,"Swift")
# man.empadd(dev3)
# man.printdev()
# man.removedev(dev1)
# print()
# man.printdev()
".........................................................................................................."
# class vehicle():
#     def __init__(self,name,max_speed,mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# class bus(vehicle):
#     def __init__(self, name, max_speed, mileage, clr):
#         vehicle.__init__(self, name, max_speed, mileage)
#         self.clr = clr
#     def print(self):
#         print("Name = ",self.name)
#         print("Max Speed = ",self.max_speed)
#         print("Mileage = ",self.mileage)
#         print("Color = ",self.clr)
# bus1 = bus("Benz",120,22,'Orange')
# bus1.print()
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
# class dev(employee):
#     def __init__(self, first, last, pay, lang):
#         super().__init__(first, last, pay)
#         self.lang = lang
# class manager(employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             employees = []
#         else:
#             self.employees = employees
#     def empadd(self,emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#     def printdev(self):
#         for i in self.employees:
#             print("-->> "+i.first,i.last)
#     def removedev(self,emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#         else:
#             print("Developer not found!!")
# dev1 = dev("Sivaram","Thampi",40000,'C++')
# dev2 = dev("Joel","McAdams",70000,"Swift")
# man = manager("MDS","904",None,[dev1,dev2])
# dev3 = dev("Stephin","Joseph",70000,"Swift")
# man.empadd(dev3)
# print(isinstance(man,dev))
# print(isinstance(man,manager))
# print(isinstance(dev1,dev))
# print()
# print(issubclass(manager,employee))
# print(issubclass(dev,employee))
# print(issubclass(employee,manager))
# print()
# print(isinstance(dev1,employee))
# print(isinstance(man,employee))
".........................................................................................................."
"Multi-level inheritance"
# class name1:
#     def stephin():
#         return("Stephin")
# class name2(name1):
#     def anandu():
#         return("Anandu")
# class name3(name2):
#     def sivaram():
#         return("Sivaram")      
# class admin(name3):
#     pass
# a = admin
# print(f"Our class have {a.stephin()}, {a.anandu()}, {a.sivaram()}")
".........................................................................................................."
# class name1:
#     def stephin():
#         return("Stephin")
# class name2():
#     def anandu():
#         return("Anandu")
# class name3():
#     def sivaram():
#         return("Sivaram")      
# class admin(name1,name3):
#     pass
# a = admin
# print(f"Our class have {a.sivaram()} {a.stephin()}")
".........................................................................................................."