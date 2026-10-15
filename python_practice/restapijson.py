import json
from textwrap import indent

import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/users')

jason_str = json.loads(response.text)
print (jason_str)
with open('data1/companies.csv', 'w')as f:
    writer=csv.writer(f,delimiter=',')
    writer.writerow(['name','city','gpscoordinates','companys'])
    for user in jason_str:
        userinfo=[user['name'],user['address']['city'],user['address']['geo'],user['company']['name']]
        writer.writerow(userinfo)


