from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime

def generate_receipt(customer_name, items_purchased, items_price, total_amount, receipt_number):
    # Create a unique filename for each receipt
    filename = f"receipt.{receipt_number}.pdf"

    c = canvas.Canvas(filename, pagesize=A4)

    c.setFont("Helvetica", 12)

    #receipt content

    c.drawString(220, 790, "LOCAL GROCERY STORE")
    c.drawString(220, 750, "Transaction Receipt")
    c.drawString(175, 730, "-" * 60)

    # Receipt details

    c.drawString(50, 710, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 690, f"Receipt Number: {receipt_number}")
    c.drawString(50, 670, f"Customer Name: {customer_name}")

    # Items purchased
    c.drawString(50, 650, "Items Purchased:")
    c.drawString(300, 650, "Items Price:")
    y_position = 630
    for item in items_purchased:
        c.drawString(70, y_position, f"- {item}")
        y_position -= 20

    for price in items_price:
        c.drawString(320, y_position - -60, f"- {price}")
        y_position -= 20

    # Total amount
    c.drawString(50, y_position - 20, "-" * 60)
    c.drawString(50, y_position - 40, f"Total Amount: Rs.{total_amount}")

    # Save the PDF file
    c.save()

    print(f"Receipt generated: {filename}")

customer_name = "Manish Kumar Mahato"
items_purchased = ["Lays", "Chocolate", "Biscuit"]
items_price =["10", "50", "25"]
total_amount = 85.0
receipt_number = 123456

generate_receipt(customer_name, items_purchased, items_price, total_amount, receipt_number)
