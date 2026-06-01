from reportlab.pdfgen import canvas

def generate_report():

    pdf = canvas.Canvas("report.pdf")

    pdf.drawString(
        100,
        750,
        "Electronic Records Report"
    )

    pdf.save()
