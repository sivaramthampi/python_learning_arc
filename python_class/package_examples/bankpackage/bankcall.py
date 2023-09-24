import bank.staff.staffname 
print("Employees are: ")
for i in bank.staff.staffname.names:
    print(i.capitalize())
import income
import bank.staff.staffname as sn
a = [i for i in sn.names]
for i in a:
    income.getincome(i)