## This block of code downloads all available PDF daily reports from ONAGRI website
import requests
from os import path, getcwd
import pandas as pd
from datetime import datetime


days = pd.date_range(start="2014-07-04",end= datetime.today()).to_pydatetime().tolist() # Reports start from July 4th 2014 
path_loc = path.join(getcwd(), "onagri") # Target Directory to contain all PDF files.


uri = "http://www.onagri.nat.tn/uploads/barrages/"
for day in days:
    url = uri + day.strftime("%#d-%#m-%Y") +'.pdf' # There are some exceptions to this rule (some URLs use [BARRAGES-, barrages, SITUATION DES BARRAGES AU] as a prefix, others use [-1, .XLS, -b, b] before '.pdf')
    response = requests.get(url)
    if 'HTTP Status 404 - Not Found' in response.text: # Report doesn't exist
        print("error")
        continue
    print(url) # Show scraped PDF's URL

    with open(path_loc+'\\'+ day.strftime("%#d-%#m-%Y") +'.pdf', 'wb') as f: # Saves PDF w/ standard file name D-M-YYYY.pdf
        f.write(response.content)
