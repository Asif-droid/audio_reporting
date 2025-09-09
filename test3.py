from borb.pdf import Document, Page, SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.font.simple_font.font_type_1 import StandardType1Font
from borb.pdf.canvas.font.font import Font

def create_pdf_with_borb():
    # Create document
    doc = Document()
    page = Page()
    doc.add_page(page)
    layout = SingleColumnLayout(page)
    
    # Add content
    layout.add(Paragraph("Bilingual Document (English & Bangla)",
                        font="Helvetica-Bold",
                        font_size=20))
    
    # English text
    layout.add(Paragraph("This is an example of English text in the PDF document.",
                        font_size=12))
    layout.add(Paragraph("The quick brown fox jumps over the lazy dog.",
                        font_size=12))
    
    # Bangla text
    try:
        layout.add(Paragraph("এটি একটি বাংলা টেক্সটের উদাহরণ।",
                            font="Helvetica",
                            font_size=14))
    except:
        print("Could not render Bangla text with default font")
    
    # Save
    with open("borb_output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)
    print("PDF generated with borb")

if __name__ == "__main__":
    create_pdf_with_borb()