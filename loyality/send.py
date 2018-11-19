import requests

url = "http://127.0.0.1:8000/api/token/"

payload = "username=admin&password=logispark123"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
          }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text[-207 : -2])




# headers = {}
# headers['Authorization'] = 'Bearer response.text[-207 : -2])'
# r = requests.get('http://127.0.0.1:8000/offers/', headers=headers)
# print(r.text)