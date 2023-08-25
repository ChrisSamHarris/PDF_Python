from fpdf import FPDF
import pandas as pd

data_frame = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

def create_footer(page_height):
    """Creates a footer for your page, on a per page basis"""
    pdf.ln(page_height)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

def create_page_lines():
    """Creates verticle lines every 10mm (pdf declaration) on your page"""
    num = 0
    for i in range(26):
        num += 10
        pdf.line(x1=10, x2=200, y1=18+num, y2=17+num)
    # for i in range(20, 298, 8):
    #     pdf.line(10, i, 200, i)


for index, row in data_frame.iterrows():
    number_of_pages = int(row["Pages"])
    pdf.add_page()
    create_page_lines()
        
    #Header
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(66,133,244)
    pdf.cell(w=0, h=9, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(x1=10, x2=200, y1=18, y2=17)

    #Footer
    create_footer(265)

    for i in range(row["Pages"] - 1):
    # [pdf.add_page() for i in range(number_of_pages - 1)]
        pdf.add_page()

        #Footer
        create_footer(275)

        create_page_lines()
    

pdf.output("output.pdf")