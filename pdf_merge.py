# import the PyPDF library for PDF manipulation and the built-in os library to help us with
# the paths to our folders and files
import os
from PyPDF2 import PdfWriter, PdfReader

#setup the paths for the different folders and needed files
pdf_folder = 'pdfs_to_merge/'
single_super_pdf = "merged_pdf_folder/merged_output.pdf"
our_watermark_pdf = "watermarked_pdf_folder/watermark.pdf"
merger = PdfWriter()

#funtion that watermarks the merged pdf
def watermark_pdf(option):
    if option == "Y" or option == "y":

        read_single_super_pdf = PdfReader(single_super_pdf, strict=False)
        read_watermarked_pdf = PdfReader(our_watermark_pdf, strict=False)
        output = PdfWriter()
        total_pages = len(read_single_super_pdf.pages)
        watermark_page = read_watermarked_pdf.pages[0]

        for num in range(total_pages):
            read_page = read_single_super_pdf.pages[num]
            read_page.merge_page(watermark_page)
            output.add_page(read_page)
        with open("watermarked_pdf_folder/watermarked_merged_final.pdf", "wb") as file:
            output.write(file)

        print("Merged all pdfs successfully.", end="\n")
        print("And you have also watermarked this merged pdf file")
    else:
        print("Merged all pdfs successfully.", end="\n")
        print("You have decided not to watermark the merged pdf file")

#funtion that merges the pdfs in the pdfs_to_merge folder
def merge_pdfs(folder, merged_pdf_file):
    if os.path.isdir(folder):
        pdf_files = sorted(
            filename for filename in os.listdir(folder)
            if filename.lower().endswith(".pdf")
        )
        for pdf in pdf_files:
            reader = PdfReader(
                os.path.join(folder, pdf),
                strict=False
            )
            for page in reader.pages:
                merger.add_page(page)

        with open(merged_pdf_file, "wb") as f:
            merger.write(f)
        should_we_watermark = input("Do you want to watermark the merged pdf? (Y/N): ")
        watermark_pdf(should_we_watermark)
    else:
        print("Sorry: Source Pdf folder which contains pdfs for merging does not found")

#call the function to merge the pdfs
merge_pdfs(pdf_folder, single_super_pdf)


