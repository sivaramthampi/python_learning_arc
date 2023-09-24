from bank.staff.staffname import names as n
dire = {n[0]:20000,n[1]:30000,n[2]:15000,n[3]:9000,n[4]:80000,n[5]:6000}
def getincome(name):
    if name not in n:
        print("Not a valid name")
    else:
        print(f"Income or {name} is {dire[name]}")