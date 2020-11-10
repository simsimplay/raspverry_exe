import requests
from urllib.parse import urlencode, unquote
import json

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
queryParams = '?' + urlencode(
    { 
        'ServiceKey' : unquote('3jIxETzP6bkj2USD7N%2BhvJfgmbD3FNw%2FnKBntwjerH8356bH0KYGxwLzL5ISaFI1iyAgIKAMGwbpQFp6e%2BbptA%3D%3D'),
         'pageNo' : '1', 
         'numOfRows' : '10', 
         'dataType' : 'json', 
         'base_date' : '20201110', 
         'base_time' : '0600', 
         'nx' : '18', 
         'ny' : '1' 
    }
)

response = requests.get(url+queryParams)
print(response)

r_dict = json.loads(response.text)
r_response = r_dict.get("response")
r_body = r_response.get('body')
r_items = r_body.get('items')
r_item  = r_items.get('item')

result = {}

for item in r_item:
    if (item.get('category')=='T1H'):
        result = item
        break

print(result)