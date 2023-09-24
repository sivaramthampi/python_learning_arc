from bs4 import BeautifulSoup as bs
import requests
res = requests.get('https://expertzlab.com/index')
val = bs(res.text)
new = val.findAll('div',attrs={'class':'course'})
print(new)
with open('data.txt','w') as f:
    for i in new:
        f.write(i.h4.a.text)