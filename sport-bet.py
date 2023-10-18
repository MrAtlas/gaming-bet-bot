import requests

# Define the API endpoint and your API key
api_endpoint = "https://api.example.com/soccer-data"
api_key = "YOUR_API_KEY"

# Define any parameters or headers required by the API
params = {
    "league": "EPL",  # Replace with the desired league or competition
    "season": "2023",  # Replace with the desired season
}

headers = {
    "Authorization": f"Bearer {api_key}",
}

# Make the API request
response = requests.get(api_endpoint, params=params, headers=headers)

# Check for a successful response
if response.status_code == 200:
    soccer_data = response.json()
    # Process the soccer data as needed
    print(soccer_data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text)
