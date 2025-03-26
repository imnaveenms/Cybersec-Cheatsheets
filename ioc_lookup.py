import requests

API_KEY = "your_api_key"
IOC = "8.8.8.8"  # Replace with your IOC

url = f"https://www.virustotal.com/api/v3/ip_addresses/{IOC}"
headers = {"x-apikey": API_KEY}
response = requests.get(url, headers=headers)

print(response.json())  # Output results
