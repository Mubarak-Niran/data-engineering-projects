import os
import requests
import json
from datetime import datetime

# Load API Key from Environment Variables
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxx"
BASE_URL = "https://api.tapfiliate.com/1.6/conversions/"
RAW_DATA_FILE = "raw_conversions.json"

def fetch_all_conversions_data():
    headers = {"Api-Key": API_KEY}
    page = 1
    all_conversions = []

    while True:
        url = f"{BASE_URL}?page={page}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if not response_data:
                break  

            all_conversions.extend(response_data)
            print(f"Fetched {len(response_data)} conversions, Total: {len(all_conversions)}")
            page += 1  
        else:
            print(f"Error {response.status_code}: {response.text}")
            break  

    return all_conversions

if __name__ == "__main__":
    conversions_data = fetch_all_conversions_data()

    if conversions_data:
        with open(RAW_DATA_FILE, "w") as f:
            json.dump(conversions_data, f, indent=4)
        print(f"Extracted data saved to {RAW_DATA_FILE}")
    else:
        print("No data fetched.")

