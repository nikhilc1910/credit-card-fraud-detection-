import requests

url = "https://credit-card-fraud-detection-4mjn.onrender.com/predict/"

payload = {
    "step": 10,
    "types": 1,
    "amount": 500,
    "oldbalanceorig": 1000,
    "newbalanceorig": 500,
    "oldbalancedest": 200,
    "newbalancedest": 700,
    "isflaggedfraud": 0
}

print("\nSending request to backend...\n")

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)

try:
    print("Response JSON:", response.json())
except Exception as e:
    print("Error parsing JSON:", e)
    print("Raw Response:", response.text)
