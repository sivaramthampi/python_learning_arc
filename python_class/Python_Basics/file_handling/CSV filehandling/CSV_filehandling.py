# import pandas as pd
# val = pd.read_csv('dataone.csv')
# print(val)
".........................................................................................................."
# import csv
# with open('dataone.csv','r') as f:
#     csv_read = csv.reader(f)
#     print(csv_read)  # this file will store as an object
#     for i in csv_read:
#         print(i)
".........................................................................................................."
"To read a csv file and copy to another"
# import csv 
# with open('dataone.csv','r') as file:    
#     csv_read = csv.reader(file)
#     with open('data.csv','w') as new_file:      
#         csv_write = csv.writer(new_file, delimiter='\t')
#         for line in csv_read:
#             csv_write.writerow(line)
# with open('data.csv','r') as f:
#     print(f.read())
".........................................................................................................."
"To fetch only email"
# import csv
# with open('dataone.csv','r') as f:
#     csV_read = csv.DictReader(f) # it will convert the file into dict
#     for i in csV_read:
#         print(i['email'])
".........................................................................................................."
"Dict writer"
# import csv
# with open('dataone.csv','r') as f:
#     a = csv.DictReader(f) 
#     with open('dict_writer.csv','w') as b:
#         head = ['fname','lname','email']
#         c = csv.DictWriter(b, fieldnames=head)
#         c.writeheader()
#         for line in a:
#             c.writerow(line)
".........................................................................................................."
