from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_pdf_with_reportlab(output_filename="bilingual_reportlab.pdf"):
    # Register Bangla font
    try:
        pdfmetrics.registerFont(TTFont('Bangla', 'kalpurush.ttf'))
    except:
        print("Warning: Could not register Bangla font. Using default.")
    
    # Create canvas
    c = canvas.Canvas(output_filename)
    
    # Set English font
    c.setFont("Helvetica", 12)
    
    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 800, "Bilingual Document (English & Bangla)")
    
    # English text
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "This is an example of English text in the PDF document.")
    c.drawString(50, 730, "The quick brown fox jumps over the lazy dog.")
    
    # Bangla text (if font registered)
    try:
        c.setFont("Bangla", 14)
        c.drawString(50, 700, "এটি একটি বাংলা টেক্সটের উদাহরণ।")
        c.drawString(50, 680, "বাংলা ভাষায় লিখিত এই বাক্যগুলি পিডিএফ ডকুমেন্টে প্রদর্শিত হবে।")
    except:
        print("Could not render Bangla text - font not available.")
    
    # Save the PDF
    c.save()
    print(f"PDF generated successfully: {output_filename}")

if __name__ == "__main__":
    create_pdf_with_reportlab()