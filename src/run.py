import os
from PyPDF2 import PdfReader, PdfWriter


def read_pdf_metadata(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = PdfReader(file)
        metadata = pdf_reader.metadata
        return metadata


def update_pdf_metadata(input_pdf, output_pdf, new_metadata):
    with open(input_pdf, "rb") as file:
        pdf_reader = PdfReader(file)
        pdf_writer = PdfWriter()

        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        pdf_writer.add_metadata(new_metadata)

        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)


def wait_for_user():
    input("Press any key to continue...")


original_folder = "Original/"
edited_folder = "Edited/"

processed_files = 0

for original_file in os.listdir(original_folder):
    if original_file.endswith(".pdf"):
        original_path = os.path.join(original_folder, original_file)
        edited_path = os.path.join(edited_folder, original_file)

        if os.path.exists(edited_path):
            original_metadata = read_pdf_metadata(original_path)
            update_pdf_metadata(edited_path, edited_path, original_metadata)
            print(f"Updated metadata for: {edited_path}")
            processed_files += 1
        else:
            print(f"Edited file not found for: {original_path}")

print(f"Total files processed: {processed_files}")
wait_for_user()
