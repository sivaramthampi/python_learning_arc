# Arithematic Operator
a = 1 + 2 #Addition
a = 2 - 1 #Subtraction
a = 10 / 2 #Division
a = 10 * 2 #Multiplication 
a = 10 % 2 #Modulus 
a = 12 // 2 #Floor Division
a = 12 ** 3 #Power Multiplication

# Comparison Operators
a = 12 > 3  # Return True if 12 is greater than 3 / else False
a = 12 < 3  # Return True if 12 is less than 3 / else False
a = 12 >= 3 # Return True if 12 is greater or equal to 3 / else False
a = 12 <= 3 # Return True if 12 is less than or equal to 3 / else False
a = 12 == 3 # Return True if 12 is equal to 3 / else False
a = 12 != 3 # Return True if 12 not equal to 3 / else False

#Logical Operators
a = 12
b = 3               # "and" Operator
res = a and b == 12 # Return True if both variables are 12

a = 12
b = 3              # "or" operator 
res = a or b == 12 # Return True if any variable is 12

a = 12
b = 3              # "not operator"
print(not a)       

#Identity Operators
x = 12
y = 12
res = x is y       # "is" operator / Return true if both variable have same value
res = x is not y   # "is not" operator / Return true if both variable not have same value

# Membership Operators 
x1 = "Hello world"
print("H" in x1)       # "in" operator / Return True if "H" included in x1 variable
print("H" not in x1)   # "not in" operator /  Return True if "H" is not included in the variable

#Assignment Operators
a = 5
a += 1    # "a" being add to "a" by 1
a -= 1    # "a" being subtracted to "a" by 1
a *= 3    # "a" being multiplied to "a" by 3
a //= 2   # "a" being floor divided to "a" by 2
a **= 2   # "a" being power multiplied to "a" by 2 
a /= 2    # "a" being divide to "a" by 2

#Bitwise Operators
"""
and == &
or  == |
not == ~
xor == ^
right shift == >>
left shift  == <<
"""
# Binary of a is 1010 and Binary of b is 1111 
a = 10
b = 15 
print(a & b)   # "& gate operation" the binary = 1010 so its "10"
print(a | b)   # "| gate operation" the binary = 1111 so its "15"
print(a ^ b)   # "^ gate operation" the binary = 0101 so its "5"
print(~a)      # "~ gate operation"
print(a << 2)  # "<< shift operation" shift 2 binary steps to the left "a" will be 40
print(b >> 2)  # ">> shift operation" shift 2 binary steps to the right "b" will be 1
