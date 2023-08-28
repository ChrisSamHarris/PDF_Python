from fpdf import FPDF
import glob 
from pathlib import Path

filepaths = glob.glob("text_conversion/text_files/*txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:

    with open(filepath, 'r') as file:
        content = file.read()

    pdf.add_page()
    filename = Path(filepath).stem
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=filename.title(), align="L", ln=1, border=0)

    pdf.set_font(family="Times", style="", size=10)
    pdf.multi_cell(h=6, w=190, txt=content)

pdf.output("text_conversion/converted_txt.pdf")