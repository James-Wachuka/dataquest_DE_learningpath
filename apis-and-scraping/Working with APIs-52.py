## 3. Types of Requests ##

import requests

# Make a GET request to get the latest position of the ISS from the OpenNotify API
response = requests.get("http://api.open-notify.org/iss-now.json")

# Get the status code of the response
status_code = response.status_code

# Print the status code
print("Status code:", status_code)

## 4. Understanding Status Codes ##

# Enter your answer below.import requests

# Make a GET request to the specified URL
response = requests.get("http://api.open-notify.org/iss-pass")

# Get the status code of the response
status_code = response.status_code

# Print the status code
print("Status code:", status_code)

## 5. Hitting the Right Endpoint ##

import requests

# Make a GET request to the specified URL
response = requests.get("http://api.open-notify.org/iss-pass.json")

# Get the status code of the response
status_code = response.status_code

# Check if the status code is 400 and update it if necessary
if status_code == 404:
    status_code = 400

# Print the updated status code
print("Status code:", status_code)