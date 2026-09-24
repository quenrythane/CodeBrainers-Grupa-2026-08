import requests

# potrzebne elementy do wykonania zapytania http:
# metody http
# endpoint
# headers
# body

base_url = "http://127.0.0.1:8000/api"
login_url = f"{base_url}/login"

my_headers = {
  'Content-Type': 'application/json',
}

my_payload = {
  "username": "admin",
  "password": "admin"
}

response = requests.post(
    url=login_url,  # endpoint
    headers=my_headers,  # headers
    json=my_payload  # body
)

print(response.json())
