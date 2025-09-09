from fpdf import FPDF
from fpdf.fonts import FontFace

def create_bilingual_pdf(output_filename="bilingual.pdf"):
    # Create PDF object
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # Add a Unicode font that supports Bangla (like Arial Unicode MS, Kalpurush, etc.)
    # You'll need to have the font file in your system or provide the path
    try:
        pdf.add_font("bangla", "", "kalpurush.ttf", uni=True)
    except:
        # Fallback to Arial Unicode MS if Kalpurush not available
        try:
            pdf.add_font("bangla", "", "arialuni.ttf", uni=True)
        except:
            print("Warning: Could not find Bangla font. Using default which may not display Bangla correctly.")
            pdf.add_font("bangla", "", "", uni=True)
    
    # Set English font
    pdf.set_font("Arial", size=12)
    
    # Add title
    pdf.set_font("Arial", size=16, style="B")
    pdf.cell(200, 10, txt="Bilingual Document (English & Bangla)", ln=1, align="C")
    pdf.ln(10)
    
    # English text
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="This is an example of English text in the PDF document. "
                             "The quick brown fox jumps over the lazy dog.", 
                   align="L")
    pdf.ln(10)
    
    # Bangla text
    pdf.set_font("bangla", size=14)
    bangla_text = "এটি একটি বাংলা টেক্সটের উদাহরণ। বাংলা ভাষায় লিখিত এই বাক্যগুলি পিডিএফ ডকুমেন্টে প্রদর্শিত হবে।"
    pdf.multi_cell(0, 10, txt=bangla_text, align="L")
    pdf.ln(10)
    
    # Mixed English and Bangla text
    mixed_text = "This is mixed text: বাংলা এবং English একসাথে।"
    pdf.multi_cell(0, 10, txt=mixed_text, align="L")
    
    # Save the PDF
    pdf.output(output_filename)
    print(f"PDF generated successfully: {output_filename}")

if __name__ == "__main__":
    create_bilingual_pdf()