"""
In Python, the logging module is used to log events and errors 
An event can be described by a message and can optionally contain data specific to the event
Events also have a level or serverity assigned by the developer.
Logging is very useful for debugging and for tracking any required information.
"""
"""
DEBUG:
INFO:
WARNING:
ERROR:
CRITICAL:
https://docs.python.org/3/library/logging.html# 
"""

"WARNING"
# import logging as l
# def add(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
# def mul(a,b):
#     return a * b
# def div(a,b):
#     return a / b
# a = 10
# b = 2
# res = add(a,b)
# l.warning(f"{a}+{b} = {res}")
# res = sub(a,b)
# l.warning(f"{a}-{b} = {res}")
# res = mul(a,b)
# l.warning(f"{a}*{b} = {res}")
# res = div(a,b)
# l.warning(f"{a}/{b} = {res}")
".........................................................................................................."
"DEBUG"
import logging as l
l.basicConfig(level=l.DEBUG,filename="debug.csv",format="%(filename)s %(message)s %(levelname)s %(asctime)s")
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
a = 10
b = 2
res = add(a,b)
l.debug(f"{a}+{b} = {res}")
res = sub(a,b)
l.debug(f"{a}-{b} = {res}")
res = mul(a,b)
l.debug(f"{a}*{b} = {res}")
res = div(a,b)
l.debug(f"{a}/{b} = {res}")
".........................................................................................................."