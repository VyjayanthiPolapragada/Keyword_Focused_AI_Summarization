import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        return full_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""