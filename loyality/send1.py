import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQyNjExMzQ1LCJqdGkiOiIxMzQzY2ZmMmQ2NDA0YmJmYTA0ZTRhY2VhNmM2NzczMCIsInVzZXJfaWQiOjF9.2NSg7O2f3wMl8BC6tIPBSptukQRhLQCal-X0Av90KMs'

r = requests.get('http://127.0.0.1:8000/waiters/', headers=headers)
print(r.text)