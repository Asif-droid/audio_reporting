from fpdf import FPDF

import re
import json
def extract_and_convert_json(ai_response):
    # Remove triple backticks and JSON language hint
    cleaned_text = re.sub(r'```json|```', '', ai_response).strip()

    # Parse JSON
    try:
        parsed_json = json.loads(cleaned_text)
        print(parsed_json)
        return parsed_json,200
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return f"Error parsing JSON: {e}", 450

data = {
    "Name": "Rahim",
    "District": "Barisal",
    "Contact Number": "N/A",
    "Location": "Barisal",
    "Gender": "Male",
    "Occupation": "Farmer",
    "Village/Area": "N/A",
    "GPS Coordinate": "N/A",
    "Disaster Type": "Salinity",
    "Damages": "Infertile land, Water contamination",
    "Loss": "N/A"
}

# Create a PDF
# def create_report(data):
#     data=extract_and_convert_json(data)
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.cell(200, 10, txt="Disaster Report", ln=True, align='C')
#     pdf.ln(10)  # Add a line break

#     # Add key-value pairs
#     for key, value in data.items():
#         pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

#     # Save the PDF
#     pdf.output("new_report.pdf")


