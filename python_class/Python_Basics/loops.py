# # There are mainly two types of Loops For Loop and While Loops
# # For Loops
".................................................................................................................................................."
# a = "Hello World"
# l = []
# for i in a:
#     l.append(i)  # To store the character in the string to a list using for loop
# print(l)
".................................................................................................................................................."
# a = [1, 3, 4, 5, 5, 7]
# b = []
# for i in a: # Here instead of i we can use any name/letters
#     b.append(i + 10) # Adding +10 to every values in a and storing it into b with the help of for loop
#     print("Done") 
# print(b)
".................................................................................................................................................."
# Print the values in a list using loops and conditional statements

# a = [12, 20, 23, 88, 1, 2, 3, 6, 7, 4, 33, 15, 10, 0]
# for i in a:
#     if i > 20:
#         print(f"{i} is above 20")
#     elif i == 20:
#         print(f"{i} is equal to 20")  # For Loop (Method 1)
#     else:
#         print(f"{i} is below 20")

# for i in range(len(a)):
#     if a[i] > 20:
#         print(f"{a[i]} is above 20")
#     elif a[i] == 20:
#         print(f"{a[i]} is equal to 20") # For Loop (Method 2)
#     else:
#         print(f"{a[i]} is below 20")

".................................................................................................................................................."
".................................................................................................................................................."
# While loop
# While will execute the code till the condition is false

# a = 1
# while a <= 5:
#     print(a)
# print("Completed")
".................................................................................................................................................."
# a = "Sivaram" 
# b = len(a) - 1
# i = 0
# while i <= b:       # To iterate every characters in a string using while
#     print(a[i])
#     i += 1
# print("Completed!")
".................................................................................................................................................."
# a = 8
# i = 0
# sum = 0
# while i <= a:
#     sum += i    # To print the sum of a Number 
#     i += 1
# print(f"Sum of {a} = ",sum)
".................................................................................................................................................."
# 'continue' helps to skip a step 

# val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in val:
#     if i == 4:   # To print values that skips 4
#         continue
#     print(i)
".................................................................................................................................................."
# 'break' will immidiatly stop when the keywords is triggered

# val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in val:
#     if i == 4:
#         break          # Breaks the loop when 'i' reaches 4
#     print(i)
".................................................................................................................................................."

# i = 0
# while i <= 7:             # while method 1
#     if i == 4:
#         i += 1
#         continue        # To print values that skips 4 using while loop
#     else:
#         print(i)
#     i += 1
# print("Thankyou!")
    
# i = 0
# while i <= 7:
#     if i == 4:           # while method 2
#         i += 1
#         continue        
#     print(i)
#     i += 1
# print("Thankyou!")
".................................................................................................................................................."
# nums = [7, 2, 5, 1, 8, 9, 4, 0, 3]
# count = 0
# while count < 9:
#     print(nums[count])
#     count += 1
#     if nums[count] == 4:
#         break
#     print("End")
".................................................................................................................................................."
# list1 = []
# count = int(input("Enter the count = "))
# for i in range(count):
#     a = int(input(f"Enter the {i+1} value = "))   # To get values entered by user and returning sum 
#     list1.append(a) 
# print("Sum = ",sum(list1)) 
".................................................................................................................................................."

# Dict looping operations
# a = {1:2, 2:3, 3:4, 4:5, 5:6}
# for i in a:
#     print(i) # By default it will return the keys of the dict

# a = {1:2, 2:3, 3:4, 4:5, 5:6}
# for i in a.values():
#     print(i) # using values function it will return the values of the dict

# a = {1:2, 2:3, 3:4, 4:5, 5:6}
# for i in a.keys():
#     print(i) # using keys function it will return the keys of the dict

# to print both keys and values
# a = {1:2, 2:3, 3:4, 4:5, 5:6}
# for i, j in a.items():     
#     print(i,j)
".................................................................................................................................................."
