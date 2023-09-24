"""
Global variable: is a type of variable declaration which we can access the variable 
through-out the code 

Local variable: is a type of variable declaration which we can access the variable only inside the
particular function.
"""
".........................................................................................................."
# a = "World" # Global Variable
# def b():
#     print("Hello",a) # Here we are calling the local variable
# print(a)
# b()
".........................................................................................................."
"""
If the global and local variable have same name the priority goes to local variable
"""
# a = "Hello World"   # Global Variable
# def b():
#     a = "Hello Python" # Local Variable
#     print(a)
# print(a)
# b()
".........................................................................................................."
"With the keyword global we can change the scope of variable to global from local"
# def b():
#     global a 
#     a = "Hello world"
# b()
# print(a)
".........................................................................................................."
val = 10
def a():
    val = 5
    print(val)
a()