import pandas as pd
from fpdf import FPDF

def read_data(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Analyze sales data
def analyze_data(df):
    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    top_product = df.loc[df["Sales"].idxmax(), "Product"]
    
    return total_sales, avg_sales, top_product

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Sales Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_pdf_report(total_sales, avg_sales, top_product, filename="sales_report.pdf"):
    pdf = PDFReport()
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Total Sales: ${total_sales:.2f}", ln=True)
    pdf.cell(200, 10, f"Average Sales: ${avg_sales:.2f}", ln=True)
    pdf.cell(200, 10, f"Top Product: {top_product}", ln=True)
    
    pdf.output(filename)
    print(f"Report saved as {filename}")

if __name__ == "__main__":
    file_name = "data.csv"  
    df = read_data(file_name)
    
    if df is not None:
        total_sales, avg_sales, top_product = analyze_data(df)
        generate_pdf_report(total_sales, avg_sales, top_product)