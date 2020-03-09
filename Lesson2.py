import requests
import json
url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
print (response)
