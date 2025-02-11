
import os

IDX = 11

import os
from pypdf import PdfReader, PdfWriter

def split_pdf(input_pdf, output_folder, ranges):
    pdf_reader = PdfReader(input_pdf)
    for range_name, (start, end) in ranges.items():
        pdf_writer = PdfWriter()

        for page in range(start - 1 + IDX, end + IDX):
            print(page)
            pdf_writer.add_page(pdf_reader.pages[page])
        output_pdf_path = os.path.join(output_folder, f"{range_name}.pdf")
        with open(output_pdf_path, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)
        print(f"Created: {output_pdf_path}")


input_pdf = os.path.join('static', 'Resonances-v7.pdf')
output_folder = os.path.join('static', 'split_pdfs')
os.makedirs(output_folder, exist_ok=True)
ranges = {
    'Unit1_Chapter1_Music_in_Human_Life': (2, 22),
    'Unit1_Chapter2_The_Elements_of_Music': (23, 43),
    'Unit2_Chapter3_Music_and_Characterization': (44, 77),
    'Unit2_Chapter4_Sung_and_Danced_Drama': (78, 128),
    'Unit2_Chapter5_Song': (129, 169),
    'Unit2_Chapter6_Stories_without_Words_Introduction': (170, 212),
    'Unit3_Chapter7_Listening_at_Public_Concerts_Introduction': (213, 258),
    'Unit3_Chapter8_Listening_at_Home_and_at_Court_Introduction': (259, 306),
}

split_pdf(input_pdf, output_folder, ranges)
