print ("why import module doesn't work???")
import requests
url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
print (response)