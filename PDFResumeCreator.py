# - Create a python program that will create your personal resume in PDF format
#	- All personal details are stored in a JSON file
#	- Your program should read the JSON file and write the details in the PDF
#	- The output file should be: LASTNAME_FIRSTNAME.pdf

 # Note:
#	- Search for available PDF library that you can use
#	- Search how data is structured using JSON format
#	- Search how to read JSON file
#	- You will create the JSON file manually
#	- Your code should be in github before Feb12
from fpdf import FPDF
import json
json_file = open("Details.json", "r+")
Resume = json.load(json_file)

Name = Resume["Name"]


Pdf = FPDF()
Pdf.add_page()

Pdf.set_font("Arial")
Pdf.set_font_size(12)

Pdf.cell(200, 10, txt = Name, ln = 3, align ='C')

Pdf.output("OLESCO_CRISJULYAN.pdf")
