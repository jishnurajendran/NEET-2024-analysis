"""
Downloads all the PDFs from the NEET website using the provided AJAX
request parameters.

Authoor: Jishnu Rajendran
The script sends a GET request to the base URL with the provided parameters,
parses the JSON response, extracts the CENTNO values, and uses them to
download the corresponding PDFs.

The downloaded PDFs are saved in the current working directory with the
same filename as the CENTNO value.

The script prints the status of the downloads (success or failure) and
prints a final message when all the downloads are complete.
"""

import requests
import pandas as pd
import os


def get_centnos(base_url, params):
    """
    Sends a GET request to the base URL with the provided parameters
    and returns a list of CENTNO values extracted from the JSON response.
    """
    response = requests.get(base_url, params=params)
    data = response.json()
    return [row['CENTNO'] for row in data['data']]


def download_pdfs(centnos, pdf_base_url):
    """
    Downloads the PDFs corresponding to the provided CENTNO values.

    The PDFs are saved in the directory 'pdfs' in the current working directory
    with the same filename as the CENTNO value.

    The function prints the status of the downloads (success or failure)
    and prints a final message when all the downloads are complete.
    """
    os.makedirs('pdfs', exist_ok=True)
    for centno in centnos:
        pdf_url = f"{pdf_base_url}{centno}.pdf"
        pdf_response = requests.get(pdf_url)
        if pdf_response.status_code == 200:
            pdf_path = os.path.join('pdfs', f"{centno}.pdf")
            with open(pdf_path, 'wb') as file:
                file.write(pdf_response.content)
            print(f"Downloaded: {centno}.pdf")
        else:
            print(f"Failed to download: {centno}.pdf")

    print("Completed downloading PDFs.")


if __name__ == "__main__":
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

    centnos = get_centnos(base_url, params)
    download_pdfs(centnos, pdf_base_url)

