from PyPDF2 import PdfReader

def main(pdf_path: str) -> None:
    reader = PdfReader(pdf_path)

    fields = reader.get_form_text_fields()

    for field_name, value in fields.items():
        print(f"{field_name}: {value}")

if __name__ == '__main__':
    pdf_path = r'test\testing_file.pdf'
    main(pdf_path)