from fpdf import FPDF
import pandas as pd
import glob 
from pathlib import Path

filepaths = glob.glob("excel_conversion/excel_invoices/*xlsx")
print(filepaths)

# df_dict = []

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # df_dict.append(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    # invoice_number = filename.split("-")[0]
    invoice_number = filename[:5]
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice Number: {invoice_number}", align="L", ln=1, border=0)
    pdf.output(f"excel_conversion/pdf_invoice/test_{invoice_number}.pdf")


# print(df_dict)

# num = 0
# for i in df_dict:
    
#     pdf.set_auto_page_break(auto=False, margin=0)
#     number_of_pages = 1
    

#     # Header
    
#     pdf.set_text_color(0,0,0)
    
#     pdf.line(x1=10, x2=200, y1=18, y2=18)

#     num += 1
#     