from fpdf import FPDF
import pandas as pd
import glob 
from pathlib import Path
from datetime import date

today = date.today()
t_date = today.strftime("%d-%m-%Y")
filepaths = glob.glob("excel_conversion/excel_invoices/*xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_number, invoice_date = filename.split("-")
    invoice_date = invoice_date.replace(".", "-")
    # invoice_number = filename[:5]
    
    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=50, h=8, txt=f"Invoice Number: {invoice_number}", align="L", ln=1, border=0)

    pdf.set_font(family="Times", style="", size=10)
    pdf.cell(w=50, h=5, txt=f"Invoice Date: {invoice_date}", align="L", ln=1, border=0)
    pdf.cell(w=50, h=5, txt=f"Generation Date: {t_date}", align="L", ln=1, border=0)

    pdf.output(f"excel_conversion/pdf_invoice/test_{invoice_number}.pdf")
    