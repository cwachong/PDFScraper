import os
from pdf2image import convert_from_path
import pytesseract
import re

# Path of the pdf file 
pdf_file = "File_1.pdf"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text_file = 'out_text.txt'
image_file_list = []

# Convert each page of the pdf to an image
pages = convert_from_path(pdf_file, 500, poppler_path=r"C:\Program Files\poppler-0.68.0\bin")

# Loop through each page and extract the text
for i, page in enumerate(pages):
    # Save the image of the page
    image_file = f"page_{i}.png"
    page.save(os.path.join(r'images' + "\\" + image_file), "PNG")
    image_file_list.append(image_file)

    # Preprocess the image
    # ...

    # Extract the text from the image
    text = pytesseract.image_to_string(image_file, lang='eng', config='--psm 6')

    with open(text_file, "a") as output_file:
        output_file.write(text)