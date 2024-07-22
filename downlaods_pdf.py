import requests
import pandas as pd

# Base URL
base_url = "https://neet.ntaonline.in/frontend/web/common-scorecard/getdataresult"

# Parameters for the AJAX request (initial load)
params = {
    "draw": 1,
    "columns[0][data]": "SrNo",
    "columns[0][name]": "",
    "columns[0][searchable]": True,
    "columns[0][orderable]": True,
    "columns[0][search][value]": "",
    "columns[0][search][regex]": False,
    # Add other column parameters similarly if needed
    "order[0][column]": 0,
    "order[0][dir]": "asc",
    "start": 0,
    "length": 100000,  # Large number to fetch all entries
    "search[value]": "",
    "search[regex]": False
}

# Make the request to get data
response = requests.get(base_url, params=params)
data = response.json()

# Extract the necessary columns
rows = []
for item in data['data']:
    row = {
        "CENTNO": item['CENTNO'],
        "CENT_STATE": item['CENT_STATE'],
        "CENT_CITY": item['CENT_CITY'],
        "CENT_NAME": item['CENT_NAME']
    }
    rows.append(row)

# Create a DataFrame
df = pd.DataFrame(rows)

# Save to CSV
csv_file_path = "cent_data.csv"
df.to_csv(csv_file_path, index=False)

print(f"Data saved to {csv_file_path}")
