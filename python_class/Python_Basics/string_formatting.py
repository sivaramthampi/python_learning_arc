print("Hello welcome {} to python".format("Sivaram"))       #String formatting type 1

print("Hello Welcome {} and {} to python".format("Abhijeet", "Sivaram"))   #String formatting type 2

name1 = "Abhijeet Mohan"
name2 = "Sivaram"
print("Hello {} and {} to Python".format(name1, name2)) #String formatting type 3
print("Name = {1}\nAge = {0}\nPlace = {2}".format(18, "Abhijeet","Pathanamthitta"))  #String formatting type 4
print("Hello {a} and {b}".format(a = name1, b = name2))     #String formatting type 5
print("Hello {a} and {b}".format(a = "Tom",b = "Jerry"))    #String formatting type 6                         
print(f"{name1} and {name2} are awesome!!")    #String formatting type 7

a = 5
b = 4
print(f"2 * (a + b) = {2 * (a + b)}")   #String formatting type 8 (Can do calculations inside the string using formatting)

val = {"name":"Sivaram","number":123456789}
print(f"Name = {val['name']}\nNumber = {val['number']}") #String formatting type 9 (Accessing Dictionary)

val = {"name":"Abhijeet","number":123456789}
print("Name = {data[name]}\nNumber = {data[number]}".format(data=val)) #String formatting type 10 (Accessing Dictionary by ".format")

name='abhijeet'
print('hii this is %s mohan, my number is %s'%(name,12356))     #String formatting type 11 concatenate of a string / %s act as an placeholder for string 

print("Hii my number is %d"%(1234567)) #String formatting type 12 (by using %d. It only accepts digits)

print("The float value is %f"%(23.5)) #String formatting type 12 (by using %f. It only accepts floating values)

print("Floating point is %f and my name is %s"%(23.40,"Sivaram")) #can use multiple placeholders in one string

print("Floating point is %.2f"%23.40) # %.2f only print two digits after decimal part

print("'Hello world'") # to print single quotes in print statement
print('"Hello world"') # to print double quotes in print statement
print("\"Hello world \"!!! How are you") # To insert quotes in the middle of the string