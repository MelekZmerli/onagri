# onagri
A visualization of water reserve evolution in Tunisia from 2014 to 2023

**scraper.py:** scrapes +3000 PDF reports from ONAGRI website and uploads them in *reports* folder

**reader.py:** extracts information from the reports using *PyPDF2* module and inserts them into *data.csv* file

**vision.py:** makes 3 visualizations ( instant / conccurent / timelapse ) of Tunisia's water reserve evolution using *matplotlib* library


> PS: Don't forget to create reports folder to contain scraped PDF reports (~400MB)
