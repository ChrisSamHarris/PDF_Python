from fpdf import FPDF
import pandas as pd
import glob 
from pathlib import Path

filepaths = glob.glob("text_conversion/text_files/*txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    df = pd.read_csv(filepath)
    print(df)
    pdf.add_page()
    filename = Path(filepath).stem
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=filename.title(), align="L", ln=1, border=0)

    pdf.set_font(family="Times", style="", size=10)
    f = open(filepath , "r")
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 5, align = 'L')

pdf.output("text_conversion/converted_txt.pdf")