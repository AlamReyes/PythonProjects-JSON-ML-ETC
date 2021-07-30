import requests
r = requests.get("https://www.google.com")
print("status code" + r.status_code)

print("r.headers" + r.headers)
print("r.text" + r.text)

