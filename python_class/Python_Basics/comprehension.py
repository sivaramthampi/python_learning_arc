# "provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined."

# list1 = []
# for i in range(1, 8):
#     list1.append(i**2)      # printing power of a number
# print(list1)

# list1 = [i**2 for i in range(1, 8)] # printing power of a number using comprehension
# print(list1)
".................................................................................................................................................."

# import math     # This is in-built module by python helps to solve various maths calculations
# print(math.sqrt(2)) # To find squareroot of a number
".................................................................................................................................................."

# import math 
# a = {math.sqrt(i) for i in range(1, 10)}
# print(a)
".................................................................................................................................................."

# import math 
# a = {math.sqrt(i) for i in range(1, 10) if i % 2 == 0} # In this comprehension method we are also using an if condition
# print(a)
".................................................................................................................................................."

# a = [i for i in range(1, 11)] # Geting values from 1 to 10 to a list using comprehension method
# print(a)
".................................................................................................................................................."
# a = ['apple', 'orange', 'grapes']
# b = ['carrot', 'beets', 'radish']  # Creating two lists into another list to tuple
# c = [(x, y)for x in a for y in b]
# print(c)
".................................................................................................................................................."
# a = 'Hello world'
# b = {i for i in a } # Comprehension
# print(b)
".................................................................................................................................................."
# a = [1, 2, 3, 4, 5, 6]
# b = dict()
# for i in a:
#     b[i] = i**2    # it will store into the dictionary as a key value pair
# print(b)
".................................................................................................................................................."
# a = [1, 2, 3, 4, 5, 6]
# b = {i:i**2 for i in a}    # it will store into the dictionary as a key value pair (using comprehension)
# print(b)
".................................................................................................................................................."

# To create 2 list into key value pairs using comprehension

# key = ['devin', 'dainty','david']
# value = ['python','cyber','analyst']      # Method 1
# d = {k:v for k,v in zip(key,value)}
# print(d)

# key = ['devin', 'dainty','david']
# value = ['python','cyber','analyst']      # Method 2
# d = {key[i]:value[i] for i in range(3)}
# print(d)
".................................................................................................................................................."

# General Comprehension aka tuple comprehension
"""
while we are using general comprehension the values will be stored in generator object 
so in order to fetch the data either use a loop or use next method
"""

# val = [1, 2, 3, 4, 5, 6, 7]
# a = (i for i in val if i % 2 == 0)   
# print("Output is = ",end="") # By using 'end' it will not change the cursor to the next line
# for i in a:
#     print(i,end=' ')
".................................................................................................................................................."
# a = [i for i in range(100) if i % 3 == 0  ] # Nested if in comprehension
# print(a)
".................................................................................................................................................."
# a = [1,2,3,4]
# b = [10,1,6]
# c = [i+j for i in a for j in b ]
# print(c)
".................................................................................................................................................."
# a = [1, 2, 3, 4]
# b = [1, 2, 3, 4]
# c = [a[i] + b[i] for i in range(len(a))]
# print(c)
".................................................................................................................................................."
# m = [[1, 2],[3, 4],[5, 6],[7, 8]]
# a = [[j[i] for j in m]for i in range(len(m[0]))]
# print(a)
".................................................................................................................................................."
