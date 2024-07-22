import requests
import pandas as pd

# URL to your server-side script
url = "https://neet.ntaonline.in/frontend/web/common-scorecard/getdataresult"

# Make a request to get the data
response = requests.get(url)
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
csv_file_path = "cent_names.csv"
df.to_csv(csv_file_path, index=False)

print(f"Data saved to {csv_file_path}")
