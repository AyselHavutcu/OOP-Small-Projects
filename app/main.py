"""Creating main classes for the program"""
from app.flat import Bill, Flatmate
from app.pdf_report import PdfReport


amount = float(input("Please enter the bill amount: "))
period = str(input("Please enter name the bill period: "))
flatmate1_name = str(input("Please enter name of first flatmate: "))
days_of_first_flatmate = int(input("How many days first flatmate stayed in the house: "))
flatmate2_name = str(input("Please enter name of second flatmate: "))
days_of_second_flatmate = int(input("How many days second flatmate stayed in the house: "))

bill = Bill(amount=amount, period=period)

flatmate1 = Flatmate(flatmate1_name, days_of_first_flatmate)
flatmate2 = Flatmate(flatmate2_name, days_of_second_flatmate)

pdf_report = PdfReport('bills.pdf')
pdf_report.generate_pdf(flatmate1, flatmate2, bill)