import os
import sys
import ghostscript
from concurrent.futures import ProcessPoolExecutor
from PyPDF2 import PdfReader


def save_image(pdf_file_path, output_file_path, page_number):
    args = [
        "pdf2png",  # actual value doesn't matter
        "-dQUIET",  # Suppress Ghostscript output
        "-dNOPAUSE",
        "-dSAFER",
        "-sDEVICE=png16m",
        "-r300",
        f"-dFirstPage={page_number}",
        f"-dLastPage={page_number}",
        "-sOutputFile=" + output_file_path,
        pdf_file_path
    ]

    with ghostscript.Ghostscript(*args):
        pass


def split_pdf(pdf_file_path):
    # Get the directory and file name without the extension
    directory, file_name_with_ext = os.path.split(pdf_file_path)
    file_name, _ = os.path.splitext(file_name_with_ext)

    # Create a folder for the individual pages
    output_directory = os.path.join(directory, f"{file_name}_pages")
    os.makedirs(output_directory, exist_ok=True)

    # Get the number of pages in the PDF
    pdf_reader = PdfReader(pdf_file_path)
    num_pages = len(pdf_reader.pages)

    # Save the images in the output directory using multiple processes
    with ProcessPoolExecutor() as executor:
        for page_number in range(1, num_pages + 1):
            output_file_path = os.path.join(
                output_directory, f"{file_name}_page_{page_number}.png")
            executor.submit(save_image, pdf_file_path,
                            output_file_path, page_number)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_pdf.py [path/to/pdf/files]")
        sys.exit(1)

    for pdf_file_path in sys.argv[1:]:
        split_pdf(pdf_file_path)
