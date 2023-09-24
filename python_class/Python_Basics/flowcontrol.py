# Flowcontrols or conditional operation 
"""
There are three types of conditional operations
-> if 
-> elif
-> else
"""


# a = 22
# if a == 22:
#     print("Hello world")                   # Prints 'Hello World' if a is equal to 22


# a = 15
# b = 20
# if a > b:                                   # To find which value is bigger using conditional statements
#     print("'a' is greater that 'b'") 
# else:       
#     print("'b' is greater that 'a'")

"........................................................................................................................."
# if and else

# a = int(input("Enter first value = "))
# b = int(input("Enter second value = "))    # To find which value is bigger using input function
# if a > b:
#     print(f"{a} is greater that {b}")
# else:
#     print(f"{b} is greater that {a}")

"........................................................................................................................."
# if, elif and else

# a = int(input("Enter first value = "))
# b = int(input("Enter second value = "))    # To find which value is bigger using input function
# if a > b:
#     print(f"{a} is greater that {b}")
# elif a==b:
#     print("Both are same")
# else:
#     print(f"{b} is greater that {a}")

"........................................................................................................................."
# Pass - Pass is a keyword that simply helps to skip

# a = int(input("Enter first value = "))
# b = int(input("Enter second value = "))
# if a < b:
#     pass
# elif a > b:
#     print(f"{a} is greater")
# print("Completed")

"........................................................................................................................."
# Nested if - condition inside another condition

# a = 20
# if a > 5:
#     print("a is greater than 5")
#     if a < 10:
#         print("a is less than 10")
#     elif a == 10:
#         print('a is equal to 10')
#     else:
#         pass
# else:
#     print("a is less than 5")
# print("Done!")

"........................................................................................................................."
# a = 100
# if a > 10:
#     print(f"{a} is above 10")
#     b = 100
#     if a > 200:
#         pass
#     elif a == b:``
#         if a < 200:
#             print("200 is big")
# elif a <= 10:
#     print("Hi")
# else:
#     print("Sorry!")

"........................................................................................................................."
# coursework = "English"
# score_theory = 53
# score_practical = 35
  
# if(coursework == "Science" or coursework == "science"):
#     if(score_theory > 50):
#         print("Please check the input score for 'Science: Theory'.")
#     elif(score_practical > 50):
#             print("Please check the input score for 'Science: Practical'.")  
#     else:
#         print("Score validated for Science. Your total is: ",score_theory + score_practical)             
# elif(coursework == "English" or coursework == "english"):
#     if(score_theory > 60):
#         print("Please check the input score for 'English: Theory'.")
#     elif(score_practical > 40):
#             print("Please check the input score for 'English: Practical'.")  
#     else:
#         print("Score validated for English. Your total is: ",score_theory + score_practical)
# else: print("Coursework not recognised. Please enter score for either Science or English.")
