import PyPDF2

def combine_pdfs(pdf_list, output_filename):
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Iterate through the PDF list and add each to the writer object
    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    # Write out the combined PDF to a new file
    with open(output_filename, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

# # Example usage
# pdf_files = ['w1.pdf','w5.pdf','w9.pdf','w13.pdf','w17.pdf','w20.pdf',]
# combine_pdfs(pdf_files, 'Complete Logbook week 1-24.pdf')
