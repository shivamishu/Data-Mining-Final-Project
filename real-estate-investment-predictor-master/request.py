import requests

# URL
url = 'http://localhost:5000/api/'

# Change the value of experience that you want to test
payload = {
	'price':235252
}

r = requests.post(url,json=payload)

print(r.json())
