# Import Dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import zipfile
import glob
import time
import os
import io
import re

# Pull text from webpage
base_URL = 'https://s3.amazonaws.com/tripdata/'
time.sleep(2)
html = requests.get(base_URL)
soup = bs(html.text, 'html.parser')

# Find all filenames relating to Jersey City Data (can be altered to pull all files with "citibike-tripdata")
zip_files = soup.find_all(text=re.compile("JC-"))

# Extract and download .csv files
for zip_file in zip_files:
    url = base_URL + zip_file
    # Extract and download .csv files
    r = requests.get(url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("data/temp")

# Once extracted, delete the files you'd like to exclude (I started in 2017, which is what {CitiBike Trend Analysis - Jersey City.twb} is built to analyze)
# 
# Use command terminal or windows powershell to navigate to the temp folder and use command:
# copy *.csv CitiBank_data_JC.csv
#
# This code will merge all the CSV files into one, which you can then pull into Tableau