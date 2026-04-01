from fpdf import FPDF
import datetime

def generate_pdf_bytes(title):
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("Arial", "B", 36)
    pdf.cell(0, 50, "Certificate of Excellence", ln=True, align="C")

    pdf.set_font("Arial", "", 20)
    pdf.cell(0, 20, "This certificate is awarded to the following paper:", ln=True, align="C")

    pdf.set_font("Arial", "B", 28)
    pdf.cell(0, 20, title, ln=True, align="C")

    pdf.set_font("Arial", "", 18)
    pdf.cell(0, 20, "This paper is free from gender-biased language.", ln=True, align="C")

    today = datetime.date.today().strftime("%B %d, %Y")
    pdf.set_font("Arial", "", 14)
    pdf.cell(0, 20, f"Date: {today}", ln=True, align="C")

    # FPDF in your version returns a bytearray already when dest='S'
    pdf_bytes = pdf.output(dest="S")
    # Ensure we return plain bytes (Flask's send_file is fine with bytes or bytearray)
    if isinstance(pdf_bytes, bytearray):
        pdf_bytes = bytes(pdf_bytes)
    return pdf_bytes