import requests

url = "http://127.0.0.1:8000/Carro"
response = requests.get(url) # Changed 'r' to 'response' for better readability
print(response.json())
