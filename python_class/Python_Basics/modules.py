"time module"

# import time
# print(time.localtime(time.time())) # Shows Date, Month, Year, Hours, Minutes, Seconds
# print(time.asctime()) # Shows Date, Month, Year, Hours, Minutes, Seconds in a diffrent format
".........................................................................................................."
# "We can also create a time"
# "..............yyyy, m, d, h, m, s, w, yd, isdst"
# custom_time = (2002, 6, 8, 9, 4, 6, 0, 0, 0)
# Time = time.mktime(custom_time)
# print(time.localtime(Time))
".........................................................................................................."
# import time
# print("Hello")
# time.sleep(1) # Will pause according to the time
# print("World")
# time.sleep(1)
# print("Welcome to Python")
".........................................................................................................."
".........................................................................................................."
"timeit module"

# import timeit
# Time = timeit.timeit('(int(x) for x in range(1, 100))') 
# print(Time) # it will print how long it took to execute the code
".........................................................................................................."
".........................................................................................................."
"calendar module"

# import calendar
# print(calendar.calendar(2023)) # Prints the calender of the mentioned year
# print(calendar.isleap(2024)) # To check if the year is a leapyear or not
# print(calendar.leapdays(2000, 2024)) # Will print how many leapday between these years
# print(calendar.month(2023, 7)) # To print the calender of a particular calender 
# print(calendar.month(2023, 7, 5, 5))
# "calender.month(year,month,width,length)" # Syntax of month function
# print(calendar.weekday(2023, 7, 23)) # Returns what weekday is the particular date
# "calender.weekday(year,month,day)"# Syntax of weekday function
".........................................................................................................."
# import calendar
# print(help(calendar)) # It will print the documentation of the particular module
".........................................................................................................."
".........................................................................................................."
"datetime module"

# import datetime
# print(datetime.date(2022,4,5)) # To print date in a particular format
# dt = datetime.date(2022,4,5)
# # We can call the attributes seperatly
# print("Day =",dt.day) 
# print("Month =",dt.month)
# print("Year =",dt.year)
# # We can save today's date
# tdt = datetime.date.today()
# print("Todays weekday = ",tdt.weekday())
# print("Todays weekday from index 1 = ",tdt.isoweekday())
# add_time = datetime.timedelta(days=4) 
# print(tdt + add_time) # It will show the date after 4 days (we can change the value 4 in the timedelta)
# # We can also minus the dates too
".........................................................................................................."
".........................................................................................................."
"random module"

# import random
# print(random.random()) # Prints a random values between 0 and 1 (float)
# print(random.uniform(1, 10)) # Prints a random values between 1 and 10 (float)
# print(random.randint(1, 20)) # Prints a random values between 1 and 0 (int)
# a = ['Red', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Black']
# print(random.choice(a)) # Prints a random value from the list
# print(random.choices(a, k=2)) # Prints two random values if we mention (key)
# print(random.choices(a,weights=[20,23,33,44,55,66,77],k=2)) # By adding weights the values will pick with a combination of higher weights
".........................................................................................................."
# import random
# a = list(range(1, 21))
# print("Real Values =",a)
# random.shuffle(a) # This function will shuffle values of a list 
# print("Shuffled Values =",a)
".........................................................................................................."
# import random
# a = [x for x in range(1, 11)]
# print(random.sample(a, k=5)) # It will take random 5 values from the list
".........................................................................................................."
"Lottery winner picking (real-time use case) using random"

# from time import sleep
# import random
# alpha = ['E','F','G','H','I','J','K','L','M']
# tickets = []
# for i in range(100):
#     tickets.append(random.choice(alpha)+str(random.randint(10000,99999)))
# winners = random.choices(tickets, k=5)
# print("Picking winners please wait....")
# sleep(2)
# print("Winners are",winners)
".........................................................................................................."
"To create a fake address (Just for study-purpose)"
# import random
# firstname = ["devin","dainty","abin","jessica","ashna","afitha"]
# lastname = ["mathew","mathew","eldhose","josheph","hasif","jabbar"]
# streetname = ["high","low","lose","hola","warks","rody"]
# states = ["AL","KL","ML","CP","EK","DL"]
# fakecities = ["logsow","florida","poland","germany","prague","autsria"]
# for i in range(7):
#     first = random.choice(firstname)
#     last = random.choice(lastname)
#     street = random.choice(streetname)
#     state = random.choice(states)
#     cities = random.choice(fakecities)
#     phone = str(random.randint(9000000000,9999999999))
#     zipcode = str(random.randint(10000,99999))
#     mail = f"{first}{last}{random.randint(1,999)}@gmail.com"
#     print(f"FullName: {first+' '+last} \nFirstName: {first} \nLastName: {last} ")
#     print(f"Full Address: {street} {cities} {state} {zipcode}")
#     print(f"StreetName: {street} \nState: {state} \nCity: {cities} \nPhone No: {phone} \nZipcode: {zipcode} \nMailID: {mail}")
#     print()
".........................................................................................................."
"To check instance of a variable or seq variable"
# x = 3.14
# y = 15
# z = [1,2]
# k = {1,2}
# print(isinstance(x,float))
# print(isinstance(y,int))
# print(isinstance(z,list))
# print(isinstance(k,list))
".........................................................................................................."
".........................................................................................................."
"any() and all()"
"any() will return true is if any value is true"
# a = [False, True, False, True]
# print(any(a))
".........................................................................................................."
"all() will return false if any value is false"
# a = [False, True, False, True]
# print(all(a))
".........................................................................................................."
# a = [0, 0, 0, 0]
# print(any(a))
# a = [1, 1, 1, 0]
# print(all(a))
".........................................................................................................."
# a = ['Hello','','']
# print(any(a))
# a = ['Hello','','']
# print(all(a))
".........................................................................................................."
# a = ['','','', 1]
# print(any(a))
# a = ['Hello','','']
# print(all(a))
".........................................................................................................."
".........................................................................................................."
"abs() - it gives absolute value "
# a = -11
# print(abs(a))
# a = -21.8
# print(abs(a))
".........................................................................................................."