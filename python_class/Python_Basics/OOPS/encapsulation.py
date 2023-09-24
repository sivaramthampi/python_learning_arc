# class main:
#     def __init__(self,name):
#         self.name = name 
#     def __mail(self):  # Cant call outside because it is private
#         print(self.name + "@gmail.com")
#     def h(self):
#         self.__mail()
# a = main("MDS")
# a.h()
".........................................................................................................."
# class car:
#     __maxspeed = 150
#     def upadtemaxspeed(self,a):
#         self.__maxspeed = a
#     def __drive(self):
#         print("Driving and max speed",self.__maxspeed)
#     def calldrive(self):
#         self.__drive()
# car1 = car()
# car1.calldrive()
# car1.upadtemaxspeed(200)
# car1.calldrive()
".........................................................................................................."
# class vehicle:
#     def __init__(self,name,year):
#         self.name = name
#         self.year = year
#     def display(self):
#         print(f"Name is {self.name} year is {self.year}")
# class car:
#     def __init__(self,brand):
#         self.brand = brand
#     def display_car(self):
#         print("Brand is",self.brand)
# class suv(vehicle,car):
#     def __init__(self, name, year, brand):
#         super().__init__(name, year)
#         car.__init__(self,brand)
#     def display_suv(self):
#         print(f"Name is {self.name} year is {self.year} brand is {self.brand}")

# a = suv("XUV",2012,'Mahindra')
# a.display()
# a.display_car()
# a.display_suv()
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