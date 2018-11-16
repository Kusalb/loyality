import requests

url = "http://127.0.0.1:8000/api/token/"

payload = "username=admin&password=logispark123"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
          }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


# headers = {}
# # headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQyMjc0OTE4LCJqdGkiOiJjNjllNmY1YmMzNjA0ZGZlYThiNWNhNmMzOWI1MDBlNCIsInVzZXJfaWQiOjF9.fVJ7czuqQx2k4fzFLNHVKwM4DqTiqG-oJtsQQHQ8wb4'
#
#
# # r = requests.get('http://127.0.0.1:8000/offers/', headers=headers)
# print(r)