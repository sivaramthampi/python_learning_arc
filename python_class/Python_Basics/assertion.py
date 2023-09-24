"""
Assertion is a method of condition checking
If the assertion is True the code will continue executing
If the assertion is False the code will Stop executing
"""
"Syntax:"
"assert<condition>"
"assert<condition><message>"
".........................................................................................................."
# assert True
# print("Hello World") 
".........................................................................................................."
# Also we can pass a message to the assertion method
# If the assertion is false it will print the message along with the error message

# assert False, "Assertion is False" 
# print("Hello World")                
".........................................................................................................."
# a, b = 12, 13
# assert a==b, "a is not equal to b"
# print("a is equal to b")
".........................................................................................................."
# a = "Hello"
# b = "Hello"
# assert a==b, "sorry a is not equal to b" 
# print("a is equal to b")
".........................................................................................................."
# assert 'Hello' in "hello world"
# print("Hello Friend!")
".........................................................................................................."
# def age(a):
#     assert a > 0, "Age is 0 or negative"
#     return f"Age is {a}"
# b = int(input("Enter your age = "))
# print(age(b))
".........................................................................................................."
# def isEmpty(a):
#     assert a != [], "List is empty"
#     print(f"Mean = {sum(a)/len(a)}")
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# isEmpty(list1)
".........................................................................................................."