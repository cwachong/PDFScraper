import os
from pdf2image import convert_from_path
import pytesseract
import re
import os
import glob

directory = "images/"
pdf_files = glob.glob(os.path.join(directory, "*.pdf"))
text_file = 'out_text.txt'
file_counter = 0

# Path of the pdf file 
for pdf_file in pdf_files:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    image_file_list = []

    # Convert each page of the pdf to an image
    pages = convert_from_path(pdf_file, 500, poppler_path=r"C:\Program Files\poppler-0.68.0\bin")
    file_counter += 1
    # Loop through each page and extract the text
    for i, page in enumerate(pages):
        # Save the image of the page
        image_file = "img" + str(file_counter) + "_" + f"page{i+1}" + ".png"
        page.save(os.path.join(r'output_images' + "\\" + image_file), "PNG")
        image_file_list.append(image_file)

        # Extract the text from the image
        text = pytesseract.image_to_string(os.path.join(r'output_images' + "\\" + image_file), lang='eng', config='--psm 6')

        with open(text_file, "a") as output_file:
            output_file.write(text)