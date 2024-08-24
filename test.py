import PyPDF2

def remove_pages_from_pdf(input_pdf_path, output_pdf_path, pages_to_remove):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf:
        pdf_reader = PyPDF2.PdfReader(input_pdf)
        pdf_writer = PyPDF2.PdfWriter()

        # Normalize pages_to_remove to ensure it handles ranges and single pages
        pages_to_remove_set = set(pages_to_remove)

        # Iterate through all the pages in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Add the page to the output PDF if it is not in the pages_to_remove list
            if page_num not in pages_to_remove_set:
                pdf_writer.add_page(pdf_reader.pages[page_num])

        # Write the output PDF
        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

# Example usage
input_pdf_path = './jhs/CAREER-TECHNOLOGY.pdf'  # Path to the input PDF
output_pdf_path = './output/CAREER-TECHNOLOGY.pdf'  # Path to save the new PDF
pages_to_remove = list(range(0,  38))  # Remove pages from 9 to 50 (0-based index)

remove_pages_from_pdf(input_pdf_path, output_pdf_path, pages_to_remove)
