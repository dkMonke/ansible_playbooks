#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://datacenterdev.service-now.com/api/x_snc_aaasinternal/aaas_matrix_api'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'dinesh.sampath'
pwd = 'Pass@word123('

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers ,data="{\"automation_directory\":\"test\",\"automation_filename\":\"testfilename\",\"managed_filename\":\"testmanage\",\"owners\":\"39c5deeb6f869100c2b67b2f5d3ee4dc,51f2f3314a36231e01d2d928e4299043\"}")

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
