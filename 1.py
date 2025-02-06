import requests

url = "http://127.0.0.1:5000/predict"
data={
  "Recency": 30,
  "Frequency": 5,
  "Age": 30
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)


# Try parsing JSON
try:
    print("JSON Response:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Error: Response is not valid JSON")