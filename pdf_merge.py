# import the PyPDF library and built-in os library
import os
from PyPDF2 import PdfWriter, PdfReader

pdf_folder = 'pdfs_to_merge/'
single_super_pdf = "merged_pdf_folder/merged_output.pdf"
merger = PdfWriter()

if os.path.isdir(pdf_folder):
    pdf_files = sorted(
        filename for filename in os.listdir(pdf_folder)
        if filename.lower().endswith(".pdf")
    )
    for pdf in pdf_files:
        reader = PdfReader(
            os.path.join(pdf_folder, pdf),
            strict=False
        )
        for page in reader.pages:
            merger.add_page(page)

    with open(single_super_pdf, "wb") as f:
        merger.write(f)
    print("Merged all pdfs successfully.")
else:
    print("Sorry: Source Pdf folder not found")




