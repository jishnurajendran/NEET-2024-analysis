import requests
import pandas as pd

# Base URLs
base_url = "https://neet.ntaonline.in/frontend/web/common-scorecard/getdataresult"
pdf_base_url = "https://neetfs.ntaonline.in/NEET_2024_Result/"

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
    "length": 100000,  # number of requests, Large number to fetch all entries
    "search[value]": "",
    "search[regex]": False
}

# Make the request to get data
response = requests.get(base_url, params=params)
data = response.json()

# Extract the CENTNO values
centnos = [row['CENTNO'] for row in data['data']]

# Download the PDFs
for centno in centnos:
    pdf_url = f"{pdf_base_url}{centno}.pdf"
    pdf_response = requests.get(pdf_url)
    if pdf_response.status_code == 200:
        with open(f"{centno}.pdf", 'wb') as file:
            file.write(pdf_response.content)
        print(f"Downloaded: {centno}.pdf")
    else:
        print(f"Failed to download: {centno}.pdf")

print("Completed downloading PDFs.")
