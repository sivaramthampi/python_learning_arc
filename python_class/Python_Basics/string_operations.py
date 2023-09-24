a = "Hello world"
print("world" in a)   # To check a word/character is present in a particular string - Returns True if it contain
print(a.upper()) # To covert to upper case / capital letters
print(a.lower()) # To covert to lower case / small letters

a = "HELLO WORLD"
print(a.islower()) # to check the string is in lower case
print(a.isupper()) # to check the string is in upper case

a = "hello world"
print(a.title()) # will capitalize every first word of the string
print(a.capitalize()) # will capitalize the first word of the string
print(a.count('l')) # To check how many times a particular character/word contains in a string 
print(a.count('world'))  
print(a.index('w')) # to check the index position of a string
print(a.index('l')) # if multiple character / world present in a string the index function will return the characters first index position

a = "helloworld"
print(a.isalpha()) # To check a string is in alphabetic order

a = "Hello World"
print(a.replace("World","Python")) # will replace the particular character/word from the string to the given character/word
print(a.find('o')) # To find index of a particular character or world contains in a string 
print(a.find('o',2,8)) # a.find("character","checking index") - a.find("character","stating index","ending position") 

a = "hellow23"
print(a.isnumeric()) # to check the string is a numeric string or not

a = "22222"
print(a.isdecimal())  # to check the string is a decimal number or not

a = "22222"
print(a.isdigit())  # to check the string is all digits 

"The diffrence between isdigit, isnumric, isdecimal!! Check out stack overflow"
"https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth"

a = "hello123"
print(a.isalnum()) # To check a string is alpha-numeric or not
print(a.startswith('h')) # Will check a string starts with the particular word/character 
print(a.endswith('e')) # Will check a string ends with the particular word/character 

a = "Hello to the world of python"
b = a.split(' ') # Split the string to a list (Doesnt work for numbers)
print(b) 
print(' '.join(b)) # Join's a list of string together

a = "   hello world   "
print(a.strip()) # Removes unwanted space from the begining and ending of a string
print(a.lstrip()) # Removes unwanted space from the left side of a string
print(a.rstrip()) # Removes unwanted space from the right side of a string


# String sliceing
a = "Hello World"
print(a[0])      # Prints the first charcter from the string
print(a[-1])     # Prints the last charcter from the string
print(a[:4])     # Prints the first 4 charcters in the string
print(a[2:9])    # Prints the character from index 2 to index 9
print(a[6:])     # Prints the character from index 6 to all
print(a[::2])    # Adding steps will print characters after two steps
print(a[::-1])   # Print the string reversed
print(a[5:-2])   # Prints the string from index 5 to index -2 
print(a[-1:-6])  # Prints the string from index -1 to -6
print(a[0:-1:2]) # Prints the string from index 0 to -1 with 2 steps

a = "Hello"
b = "World"
print(a + b)        #Concatnate a and b
print(a * 2)        # Prints a two times
print("Hello "+b)   # Concatnate to the existing string


a = "it's sunday" 
b = "have a great day"
print(a[:5] + b[5:])  # Prints "it's a great day"
print(b[7:-3] + a[5:]) # Prints "great sunday"