from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(filename, url, data):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    
    c.drawString(50, 750, f"Security Analysis Report for {url}")
    c.drawString(50, 730, "-----------------------------------")
    
    y = 700
    for section, result in data.items():
        c.drawString(50, y, f"{section}:")
        y -= 20
        if isinstance(result, dict):
            for key, val in result.items():
                c.drawString(70, y, f"{key}: {val}")
                y -= 20
        else:
            c.drawString(70, y, str(result))
            y -= 20
        y -= 10
    
    c.save()
