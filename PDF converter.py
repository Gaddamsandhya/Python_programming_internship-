
from pdf2image import convert_from_path
from docx import Document
import os

def pdf_to_text(pdf_path, output_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    text = ""

    # Extract text from each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()

    # Write the text to a file
    with open(output_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

def pdf_to_images(pdf_path, output_folder):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i+1}.png")
        image.save(image_path, "PNG")

def pdf_to_docx(pdf_path, output_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    docx_document = Document()

    # Extract text from each page and add it to the docx
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        docx_document.add_paragraph(text)

    # Save the docx file
    docx_document.save(output_path)

def main():
    pdf_path = "sample.pdf"  # Path to your PDF file
    text_output_path = "output.txt"
    images_output_folder = "output_images"
    docx_output_path = "output.docx"

    # Convert PDF to text
    pdf_to_text(pdf_path, text_output_path)
    print(f"PDF converted to text and saved to {text_output_path}")

    # Convert PDF to images
    pdf_to_images(pdf_path, images_output_folder)
    print(f"PDF converted to images and saved to {images_output_folder}")

    # Convert PDF to docx
    pdf_to_docx(pdf_path, docx_output_path)
    print(f"PDF converted to docx and saved to {docx_output_path}")

if __name__ == "__main__":
    main()


