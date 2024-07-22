# NEET Examination Analysis

This project aims to analyze the NEET examination data from the official website. The data includes marks obtained by students in various centers. The project includes the following files:

## Scripts and Notebooks

1. `download_pdf.py`: This file contains the code to download the pdf files from the NEET website.

2. `neet_analysis.py`: This file contains methods for processing pdfs and creating appropriate DataFrame.

3. `names_cent_state_city.py`: Extracts the **State**, **City**, and **Center Name** from *center code* (same as the pdf file name in `/pdfs`)

4. `neet_analysis.ipynb`: This jupyter notebook contains the interactive code with all the analysis done till now

## Data files 

1. `city_marks_data.csv`: This file contains the whole data for total marks of each student center-wise.

2. `cent_data.csv`: This file contains the state, city, and center name with its serial number

The purpose of this project is to study and find any malpractice and fraud across examination centers. The analysis is done using the downloaded data and the code in the `neet_analysis` folder.
## Requirements

`pip install pymupdf pandas matplotlib numpy seaborn scipy scikit-learn`
