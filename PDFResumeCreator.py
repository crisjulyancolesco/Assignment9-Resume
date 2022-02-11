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
Skill1 = Resume["Skill1"]
Skill2 = Resume["Skill2"]
Skill3 = Resume["Skill3"]
Title4 = Resume["Title4"]
Work1 = Resume["Work1"]
Work2 = Resume["Work2"]
Work3 = Resume["Work3"]
Title5 = Resume["Title5"]
Project1 = Resume["Project1"]
Desc1 = Resume["Desc1"]
Project2 = Resume["Project2"]
Desc2 = Resume["Desc2"]
Title6 = Resume["Title6"]
Ref = Resume["Ref"]

# PDF
Pdf = FPDF("P", "cm", "Letter")
Pdf.add_page()

#Spaces
Pdf.set_font("Arial", "", 15)
Pdf.cell(0,0.4, align = "L", ln=1)

#Personal info
Pdf.set_font("Times", "B", 18)
Pdf.cell(0,1, Name, align = "L", ln=True)

Pdf.set_font("Times","", 15)
Pdf.cell(0,0.5, Address, align = "L", ln=1)
Pdf.cell(0,1, Contact, align = "L",ln=1)
Pdf.cell(0,0.5, Email, align = "L", ln=1)

#Picture
Pdf.image( "144x144px.jpg", 15, 0.5, 6 )

# Objective
Pdf.set_font("Times", "BU", 15)
Pdf.cell(0,2, Title1, align = "L", ln=1)


#Education
Pdf.set_font("Times", "BU", 15)
Pdf.cell(0,2, Title2, align = "L", ln=1)

Pdf.set_font("Times", "", 15)
Pdf.cell(0,0.5, Course, align = "L", ln=2)
Pdf.cell(0,1, School, align = "l",ln=True)
Pdf.cell(0,0.5, Year, align = "L", ln=True)

#Skills
Pdf.set_font("Times", "BU", 15)
Pdf.cell(0,2, Title3, align = "L", ln=1)

Pdf.set_font("Times", "", 15)
Pdf.cell(0,0.5, Skill1, align = "L", ln=1)
Pdf.cell(0,1, Skill2, align = "L", ln=1)
Pdf.cell(0,0.5, Skill3, align = "L", ln=1)

#Working Experience
Pdf.set_font("Times", "BU", 15)
Pdf.cell(0,2, Title4, align = "L", ln=1)

Pdf.set_font("Times", "", 15)
Pdf.cell(0,0.5, Work1, align = "L", ln=1)

Pdf.set_font("Times", "", 15)
Pdf.cell(0,1, Work2, align = "L", ln=2)

Pdf.set_font("Times", "", 15)
Pdf.cell(0,0.5, Work3, align = "L", ln=3)

#Projects
Pdf.set_font("Times", "BU", 15)
Pdf.cell(0,2, Title5, align = "L", ln=1)

Pdf.set_font("Times", "BI", 15)
Pdf.cell(0,0.5, Project1, align = "L", ln=3)
Pdf.set_font("Times", "", 15)
Pdf.cell(0,1, Desc1, align = "L", ln=3)

Pdf.set_font("Times", "BI", 15)
Pdf.cell(0,1, Project2, align = "L", ln=3)
Pdf.set_font("Times", "", 15)
Pdf.cell(0,0.5, Desc2, align = "L", ln=3)

#Char Ref
Pdf.set_font("Times", "BU", 15)
Pdf.cell(0,2, Title6, align = "L", ln=1)

Pdf.set_font("Times", "", 15)
Pdf.cell(0,0.5, Ref, align = "L", ln=1)


Pdf.output("OLESCO_CRISJULYAN.pdf")