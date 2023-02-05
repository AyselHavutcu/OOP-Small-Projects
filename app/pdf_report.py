from fpdf import FPDF
import webbrowser
import os

class PdfReport:

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2)))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1)))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        #pdf.image('app/files/house.png')
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=200, h=80, txt='Flatmates Bills', border=1, align='C', ln=1)
        pdf.cell(w=100, h=48, txt="Period: ", border=1)
        pdf.cell(w=150, h=48, txt=bill.period, border=1, ln=1)

        #flatmate1 info
        pdf.cell(w=100, h=48, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=48, txt=flatmate1_pay, border=1, ln=1)

        # flatmate2 info
        pdf.cell(w=100, h=48, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=48, txt=flatmate2_pay, border=1, ln=1)

        #os.chdir('files')
        pdf.output(self.filename)

        webbrowser.open(self.filename)