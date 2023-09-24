# import time 
# def sqr(a):
#     res=[]
#     starting = time.time()
#     for i in a:
#         res.append(i*i)
#     ending = time.time()
#     print(f"Time Diffrence = {(ending-starting)*1000}")

# def cubeing(a):
#     res=[]
#     starting = time.time()
#     for i in a:
#         res.append(i**3)
#     ending = time.time()
#     print(f"Time Diffrence = {(ending-starting)*1000}")

# arr = [i for i in range(1,20001)]
# sqr(arr)
# cubeing(arr)


import time
def current(function):
    def num(n):
        starting = time.time()
        function(n)
        ending = time.time()
        print(f"Time diff is {(ending-starting)*1000}")
    return num
@current
def sqr(number):
    res = []
    for num in number:
        res.append(num*num)
    return res
@current
def cube(number):
    res = []
    for num in number:
        res.append(num**3)
a = [i for i in range(1,20001)]
sqr(a)
cube(a)