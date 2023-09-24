# JavaScript Object Notation (.json)

# jdata ='''
# {
#     "people":[
#         {
#         "name":"devin",
#         "phone":1234567899,
#         "email":"devin@gmail.com",
#         "has_licence": true 
#         },   
#         {
#         "name":"dainty",
#         "phone":1234444444,
#         "email":null,
#         "has_licence": false    
#         }
#     ]
# }
# '''
# import json
# data = json.loads(jdata)
# print(data)
# print(data['people'])
# print(data['people'][1])
# print(data['people'][0]['name'])
# for i in data['people']:
#     print(i['phone'])
".........................................................................................................."
# jdata ='''
# {
#     "people":[
#         {
#         "name":"devin",
#         "phone":1234567899,
#         "email":"devin@gmail.com",
#         "has_licence": true 
#         },   
#         {
#         "name":"dainty",
#         "phone":1234444444,
#         "email":null,
#         "has_licence": false    
#         }
        
#     ]
# }
# '''
# import json
# data = json.loads(jdata)
# for i in data['people']:
#     del(i['phone'])     # It will del the data fields
# print(data)
".........................................................................................................."
"To read the data and print it as json format using dumps()"
# jdata ='''
# {
#     "people":[
#         {
#         "name":"devin",
#         "phone":1234567899,
#         "email":"devin@gmail.com",
#         "has_licence": true 
#         },   
#         {
#         "name":"dainty",
#         "phone":1234444444,
#         "email":null,
#         "has_licence": false    
#         }
        
#     ]
# }
# '''
# import json
# data = json.loads(jdata)
# new_data = json.dumps(data,indent=2,sort_keys=True)
# print(new_data) 
".........................................................................................................."
"To convert the data into a json format and save it as a json file"
# jdata ='''
# {
#     "people":[
#         {
#         "name":"devin",
#         "phone":1234567899,
#         "email":"devin@gmail.com",
#         "has_licence": true 
#         },   
#         {
#         "name":"dainty",
#         "phone":1234444444,
#         "email":null,
#         "has_licence": false    
#         }
        
#     ]
# }
# '''
# import json
# data = json.loads(jdata)
# with open('new_jdata.json','w') as newfile:
#     data = json.dump(data,newfile,indent=2,sort_keys=True)
".........................................................................................................."
"To open a json file and write it to the another file "
# import json
# with open('states.json') as file:
#     data = json.load(file)   # Convert the file to dict
#     print(data)
#     for i in data['states']:
#         del i['abbreviation']
#         with open('new_states.json','w') as newfile:
#             json.dump(data,newfile,indent=2)
".........................................................................................................."
import requests
import json
res = requests.get("https://jsonplaceholder.typicode.com/todos")
rea = res.text # It will print as how it displays in web
re = json.loads(res.text)
for i in re:
    print(i)
".........................................................................................................."
# import requests   # If requests not found install the module "pip install requests"
# import json
# res = requests.get("https://jsonplaceholder.typicode.com/todos")
# read = json.loads(res.text)
# with open("fetched_json.json",'w') as newfile:
#     json.dump(read,newfile,indent=2)
".........................................................................................................."
