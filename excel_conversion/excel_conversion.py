from fpdf import FPDF
import pandas as pd
import glob 
from pathlib import Path
from datetime import date

today = date.today()
t_date = today.strftime("%d-%m-%Y")
filepaths = glob.glob("excel_conversion/excel_invoices/*xlsx")

for filepath in filepaths:
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

    pdf.cell(w=50, h=8, txt="", align="L", ln=1, border=0)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    table_titles = [i.replace("_", " ").title() for i in list(df.columns)]
    print(table_titles)

    # Add Header
    pdf.set_font(family="Times", style="B", size=10)
    pdf.cell(w=20, h=8, txt=str(table_titles[0]), border=1, align="C")
    pdf.cell(w=50, h=8, txt=str(table_titles[1]), border=1, align="C")
    pdf.cell(w=35, h=8, txt=str(table_titles[2]), border=1, align="C")
    pdf.cell(w=25, h=8, txt=str(table_titles[3]), border=1, align="C")
    pdf.cell(w=20, h=8, txt=str(table_titles[4]), border=1, align="C", ln=1)


    for index, row in df.iterrows():
        pdf.set_font(family="Times", style="", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=20, h=8, txt=str(row["product_id"]), border=1, align="C")
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1, align="C")
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1, align="C")
        pdf.cell(w=25, h=8, txt=str(row["price_per_unit"]), border=1, align="C")
        pdf.cell(w=20, h=8, txt=str(row["total_price"]), border=1, align="C", ln=1)

    total_sum_invoice = df["total_price"].sum()
    # format the sum to 2 decimal places 
    total_sum_invoice = "{:.2f}".format(total_sum_invoice)

    pdf.set_font(family="Times", style="", size=10)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=20, h=8, txt="", border=1, align="C")
    pdf.cell(w=50, h=8, txt="", border=1, align="C")
    pdf.cell(w=35, h=8, txt="", border=1, align="C")
    pdf.cell(w=25, h=8, txt="", border=1, align="C")
    pdf.cell(w=20, h=8, txt=str(total_sum_invoice), border=1, align="C", ln=1)

    # Whitespace followed by Amount Due 
    pdf.cell(w=50, h=8, txt="", align="L", ln=1, border=0)
    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=50, h=8, txt=f"Total Amount Due: £{total_sum_invoice}", align="L", ln=1, border=0)

    # Company name and logo 
    pdf.cell(w=25, h=8, txt="Chris Tech", align="L", border=0)
    pdf.image("excel_conversion/pythonhow.png", w=5, h=6)
    
    print(df)
    print("######")

    pdf.output(f"excel_conversion/pdf_invoice/test_{invoice_number}.pdf")
    