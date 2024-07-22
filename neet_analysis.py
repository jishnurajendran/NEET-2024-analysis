import fitz  # PyMuPDF
import pandas as pd
import re
import matplotlib.pyplot as plt
import os

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def parse_marks(text):
    marks_data = []
    # Regular expression to find lines with marks
    pattern = re.compile(r"(\d+)\s+(-?\d+)")
    for match in pattern.finditer(text):
        srlno, marks = match.groups()
        marks_data.append((int(srlno), int(marks)))
    return marks_data

def create_dataframe(marks_data, city):
    df = pd.DataFrame(marks_data, columns=["Srlno", "Marks"])
    df['City'] = city
    return df

def process_pdfs(folder_path):
    all_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            city = os.path.splitext(filename)[0]  # Use filename as city name
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)
            marks_data = parse_marks(text)
            df = create_dataframe(marks_data, city)
            all_data.append(df)
    return pd.concat(all_data, ignore_index=True)