import requests

url = "https://reqres.in/api/users?page=2"

# Send Get request
response = requests.get(url)
print(response)
print()

# Display response content
print(response.content)
print()


# Validate status code
print(response.status_code)
assert response.status_code == 200
print()


print(response.headers)
print()
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch cookies
print(response.cookies)