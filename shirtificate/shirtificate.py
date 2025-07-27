from fpdf import FPDF

name = input("Name: ").title()
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Times", style="B", size=25)
pdf.cell(210, 0, "CS50 Shirtificate", align='C', new_x="LMARGIN", new_y="NEXT")
pdf.image("shirtificate.png", 50, 20, 130)
pdf.set_text_color(255,255,255)
pdf.set_font("Times", style="B", size=15)
pdf.cell(210, 80, f"{name} took CS50", align='C', )
pdf.output("shirtificate.pdf")
