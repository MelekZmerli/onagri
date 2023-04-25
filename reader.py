## This block of code scrapes total water reserve value from PDF reports and writes them into a .csv file 
from PyPDF2 import PdfReader
import pandas as pd
import csv
from datetime import datetime

with open("data_temp.csv", 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile,delimiter=";") # ; used as delimiter instead of , because total_water_level scraped value contains a comma
        
    # writing the fields 
    csvwriter.writerow(['date','total_water_level']) 
        
    # writing the data rows 
    days = pd.date_range(start="2023-03-29",end= datetime.today()).to_pydatetime().tolist()
    for day in days:
        try:
            print("Processing: "+day.strftime("%#d-%#m-%Y") +'.pdf')
            reader = PdfReader(day.strftime("%#d-%#m-%Y") +'.pdf')
            if len(reader.pages) in [3,1]:
                page = reader.pages[1]
            else: # Some PDF files (~20) don't follow the standard format of reports (6 pages, missing tables ..)
                csvwriter.writerow([day.date(),-1]) # -1 = NULL
                continue
            lines = page.extract_text().split('\n')
            for l in lines:
                if 'TOTAL GENERAL' in l: # This table row contains desired value 
                    stock = l.split()[-5]
                    csvwriter.writerow([day.date(),stock]) 
                    break
        except: # If PDF Report doesn't exist
            csvwriter.writerow([day.date(),-1]) # -1 = NULL