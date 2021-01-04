from django.shortcuts import render
from .models import ContactDetails
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
import io
from django.http import FileResponse

# Create your views here.


def contact(request):
    """Render the contact html page"""

    contacts = ContactDetails.objects
    return render(request, 'contact_app/contact.html', {"contacts":contacts})


def create_pdf(request):
    """Create the info file about contact methods"""

    contact_info = ContactDetails.objects.iterator()

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pdf_file = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens
    pdf_file.setTitle("Contact Infomation")
    pdf_file.setFont("Helvetica-Bold", 20, leading=None)
    pdf_file.setFillColorRGB(1,0,0)
    pdf_file.drawString( 60, 800, "Stefanos Taramas Contact Information")
    pdf_file.setFillColorRGB(0,0,0)
    pdf_file.setFont("Helvetica", 15, leading=None)

    for index, item in enumerate(contact_info):
        line = str(index + 1) +") " + str(item.contact_name) + ": " + str(item.contact_info)
        column = 50
        row = 750 - 15*index
        pdf_file.drawString(column, row, line)

    # Close the PDF object cleanly
    pdf_file.showPage()
    pdf_file.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='StefanosTaramasContactInfo.pdf')
    
