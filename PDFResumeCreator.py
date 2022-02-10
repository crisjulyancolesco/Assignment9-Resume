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
Address = Resume["Address"]
Contact = Resume["Contact No."]
Email = Resume["Email Address"]
Title1 = Resume["Title1"]
Title2 = Resume["Title2"]
Course = Resume["Course"]
School = Resume["School"]
Year = Resume["Year"]
Title3 = Resume["Title3"]
Skills = Resume["Skills"]
Title4 = Resume["Title4"]
Work1 = Resume["Work1"]
Date1 = Resume["Date1"]
Position1 = Resume["Position1"]
Work2 = Resume["Work2"]
Date2 = Resume["Date2"]
Position2 = Resume["Position2"]
Work3 = Resume["Work3"]
Date3 = Resume["Date3"]
Position3 = Resume["Position3"]
Title5 = Resume["Title5"]
Ref = Resume["Ref"]

Pdf = FPDF("P", "mm", "Legal")
Pdf.add_page()

Pdf.set_font("Arial", "B", 15)
Pdf.cell(0,0, Name, align = "L", ln=True)

Pdf.set_font("Arial","", 12)
Pdf.cell(40,10, Address, align = "L", ln=1)
Pdf.cell(40,10, Contact, align = "L",ln=1)
Pdf.cell(40,10, Email, align = "L", ln=1)







Pdf.output("OLESCO_CRISJULYAN.pdf")
