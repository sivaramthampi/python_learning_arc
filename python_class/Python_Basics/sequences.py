# LISTS

a = [1, 2, 3, "Main", False, 5 + 2]  # A list is kind of a variable but it holds multiple values of diffrent datatype
# List is mutable (can add/change/replace/remove values) and lists are ordered 
print(a)
print(len(a))   # This function helps to identify length 
print(a[4])     # Every element in the list have an index position and it can change the values
print(a[4:])    # Slicing also works with lists too
print(a[1::2])  # Add steps to print list
print(a[::-1])  # To print the list reverse order using slicing
a.reverse()     # In-built function to reverse a list 
print(a)
a.append("Hello")  # This will add an value/element to the end of the list - {only works with list} 
print(a)
a.append({"Hello",True,8}) # Appending also works with any type of datatypes/sequences
print(a)

# "To input a value to the list by input method"
# b = input("Enter your name to append to the list: ")
# a.append(b)
# print(a)

a.insert(2,"World")  #To insert an element/value into to specific index position 
#NB: It do not replace existing values. it just move the existing values to the next indexes"
print(a.index("World"))

a[2] = "Ramen" # To replace a value from a list
print(a)

a.remove("Ramen") # To remove a value from a list
print(a)
 
a.pop(2) # To remove a value using index position
print(a)

a.clear() # To delete all values from the list
print(a)

a = [1, 2, 3, "Main", False, "Hello", "World"]
del(a[2]) # Another way to delete item from a list
print(a)

a = [1, 2, 3, "Main", False, "Hello", "World", 22, 34]
del(a[2:5]) # Another way to delete item from a list using slice
print(a)

a  = ['Apple','Orange','Banana','apple','orange','banana']
a.sort()  # It will sort the values alpahbatically
# First it will print the capital letter words then the small letter words
print(a)

a = [3, 2, 4, 5, 7, 9, 1, 0, -3, -2]
a.sort() # It will sort the numbers to assending order
print(a) 

a = [6, 7, 8, 9]
b = [1, 2, 3, 4, 5]
b.extend(a)     # This will extend the list with the other list
print(b)

a = [1, 2, 3, 4, 5]
print(set(a))    # To convert a list to set
print(tuple(a))  # To convert a list to tuple

a = ['Hello','World', 1, 2, 3]
b = a.copy() # To copy a list to another list
print(b)

"Diffrence between list.copy() and list assignment"
a = [2, 4, 1, 2, 3]
b = a
b[3] = 25           # List assignment will change values if any of the list (copied/orginal) is altered/changed
print(a)            
print(b)

a = [2, 4, 1, 2, 3]
b = a.copy() 
b[3] = 45           # The list copy function help to store the values of orginal list safe
print(a)            
print(b)

a = [2, 4, 1, 2, 3]
print(max(a)) # To find the largest value
print(min(a)) # To find the smallest value


a = ['Apple', 'Orange', 1, 2, 3, 4, 'End']
for i in a:           # To print the list one by one
    print(i)

a = [ 1, 2, 3, 6, 5, 6, 7, 6, 7, 5]
print(a.count(6)) # It will return how many time the value is present in the list

a = ['a','b','c']
print(max(a))
print(min(a))   # Returns the result according to ASCII table

"Check ASCII table here https://www.rapidtables.com/code/text/ascii-table.html" 

" .................................................................................................................................................................................................................................."
# TUPLES

# a = (1, 2, 3, 4, 5) 
# Tuple is also a kind of a list it holds multiple values of diffrent datatypes but it not mutable (cannot change/add/remove/replace values)

"""
In tuple we cannot change values in tuples
a = [1, 2, 3, "Main", False, 5 + 2]
a[3] = 23 "This code will throw error"
"""

a = [1, 2, 3, "Main", False, 5 + 2]
print(a) # To print a tuple
print(a[2])    # To print a tuple using index
print(len(a))  # This function helps to identify length 

a = [1, 2, 3, 5, 2, 3, 8]
print(max(a))  # To find the largest value
print(min(a))  # To find the smallest value

a = ("Hello world", "abc", "orange", "Apple")
print(max(a, key=len))  # Adding key will help to perform a particular task inside the method

a = (1, 2, 3, 4)
(f, x, y, z) = a
print(f)            # Another way to initialize tuple 
print(x)
print(y)
print(z)

a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
print(a + b) # It will concatenate two tuples

a = (1, 2, 3, 4)
print(a)
del a # To Delete a tuple entirely

a = (1, 2, 3, 4)
b = a + (5, 6, 7)   # It will concatenate the 'a' tuple to the 'b' tuple
print(b)

a = (1, 2, 3, 4)
b = a + tuple([24, 23, 27])   # It will coverts the list to tuple then 'a' tuple concatenate to the 'b' tuple
print(b)

a = (1, 2, 3, 4)
b = a + (1,)  # Another way to concatenate tuple
print(b)
" .................................................................................................................................................................................................................................."
# SET
"""
a = {23, 42, 45, 3, 15}
A Set is also a kind of a list it holds multiple values of diffrent datatypes but it is not ordered or indexed
And set do not accept any duplicate values
"""
a = {23, 42, 45, 3, 15}
print(a)

a = {23, False, 23.5, "Hello"} # Can pass any type of values

a = {23, 42, 45, 3, 15, 23} # Do not count duplicate values
print(a)

a.add("Hello World") # To add item into a set. You cannot able to add multiple values using "add" method
print(a)


"To add multiple values to a set"

a = ["Hello world", 23, 44, 55, 66]
b = {1, 2, 3, 4, 5}
for i in a:
    b.add(i)
print(b)

a = {1, 2, 4, 5, 6}
for i in range(20, 27):
    a.add(i)
print(a)

"To print the values one by one in a set"
a = {1, 2, 4, 5, 6}
for i in a:
    print(i)

"""
Frozen Set 
Once we make a frozen set we cant add/remove/change any values into that set
"""
a = frozenset({1, 2, 4, 5, 6})
print(type(a))
# a.add(23) # This will throw an error because a frozenset cannot accepts values 

a = {1, 2, 4, 5, 6}
b = a.copy() # Will copy the set to another variable

a = {1, 2, 4, 5, 6}
b = {7, 8, 9, 10, 11}
c = a.union(b)  # To join sets into one  NB: Do not accepts duplicate values
print(c)

"To initialize a empty set"
a = {} 
print(type(a))   # This will print "dict" because we also use {} brackets on "dict" too
a = set()
print(type(a))

a = {1, 2, 4, 5, 6}
print(len(a))    # will print the length of the set NB: Do not count duplicate values

a = {1}
a.update({2, 3, 4, 5, 6}) # Another way to add multiple values into a set
print(a)

a = {1, 2, 3, 4, 5, 6}
a.remove(2) # To remove a value from the set
print(a)

a = {1, 2, 3, 4, 5, 6}
a.pop() # To remove a first value/random value from the set
print(a)

a = {1, 2, 3,  4, 5, 6}
a.discard(5) # Another way to delete a value in a set
print(a)

a = {1, 2, 4, 5, 6}
b = {7, 8, 9, 10, 11}
c = {12, 13}
c = a | b | c # To join sets into one using '|' symbol
print(c)

a = {1, 2, 3, 4}
b = {7, 8 ,3, 9} 
print(a.intersection(b)) # To know whats common in these sets
print(a & b) # To know whats common in these sets using '&' symbol

a = {1, 2, 3, 4}
b = {1, 2, 5, 6} 
print(a.difference(b)) # To find difference of sets
print(a - b) # Another way to find difference of sets

" .................................................................................................................................................................................................................................."
# DICTIONARY - DICT
"""
Dict is also a considered as sequence variable 
Every value have its own keyword to call the value

dict = {
    "name1" : "Hello",
    "name2" : "World" 
}
print(dict["name1"])
The values of dict is mutable but the keywords are stagnant
"""

a = {"FirstName":"Hello",
    "LastName": "World"}
print(a["FirstName"] + a["LastName"] ) 

a = {1:"Apple",
    2:200,
    3:True,            # Accepts all type of data
    4:23.2,
    5:"Hello"}
print(a)

a = {1:"Hello",
    1:"World"
    }
print(a[1]) # If the keywords are same in a dict it will take the last same key-value pair (Kind of updation happening there)

a = {1:"Apple",
    2:200,
    3:True,            
    4:23.2,
    5:"Hello"}
print(a.get(5))   # Another way to call a dict value 'a.get(<keyword>)'
print(a.get(6,"Not Found")) # If the keyword is not found in the dictionary it will return 2nd argument the message (default it will be 'None')


"To covert other data structures to dict"
key = ['Word', 'Fruit',' Age']
val = ['Hello', 'Apple', 20]
a = dict(zip(key, val))  # Ziping == compressing - Zipping helps to convert to dict
print(a)

list1 = [['Word','Hello'],['Age',20],['Fruit','Apple']] 
"""
By using 2D list of 2 elements.
When it converts to dict the first value will be the key and second will be the value 
"""
a = dict(list1)
print(a)

list1 = [('Word','Hello'),('Age',20),('Fruit','Apple')]
a = dict(list1)     # Tuple to a list
print(a)

list1 = zip(['Word','Hello','Age'],[20,'Fruit','Apple'])
a = dict(list1)     # Another way to convert using zip method
print(a)

a = {}
a.setdefault('word','hello') # To input a keyword pair to an empty dict
print(a)

a = {1:'Hello',2:'World'}
b = {3:'Python'}
a.update(b) # To update another dict to a particular dict
print(a)


a = [[1,'Hello'],['World','dev']]
b = {3:'Python'}
b.update(a) # To update list to a particular dict
print(b)

a = {1:'Apple',2:3,'l':'python'}
a.update(main=23,hello='World')  # Another method of updating to a dict
print(a)

a = {1:'Apple',2:3,'l':'python'}
a.pop('l')      # Deletes the mentioned value from the dictionary
print(a)

a = {1:'Apple',2:3,'l':'python',5:'Orange'}
a.popitem()     # Deletes the last value from the dictionary
print(a)

a = {1:'Apple',2:3,'l':'python',5:'Orange'}
a.clear()       # Deletes all values from the dictionary
print(a)

a = {1:'Apple',2:3,'l':'python',5:'Orange'}
f = f"{a[2]}"
print(f)

a = {1:{2:{3:4}}}
print(a[1][2][3]) # To fetch the values if the dict is multi-dimensional 


a = {1:{1:{2:'b',3:'c'},
    2:{4:'d',5:'e'}   
    }
}
print(a[1][2][5]) # To print 'e' 


a = {1:{2:{3:4}}}
print(a[1][2].values()) # To Fetch the values contains on the particular dict
print(a[1][2].keys()) # To Fetch the keys contains on the particular dict

a = {'sunday':36,'tuesday':26,'wednesday':30}
inp = input("Enter a day (sunday,monday,tuesday): ").lower() # Using lower() is optional
print(f"The temprature of {inp} is {a[inp]}")