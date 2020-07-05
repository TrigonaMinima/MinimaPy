# Converts PDF to CSV, psge by page.
import os
import subprocess
import tabula
from PyPDF2 import PdfFileReader


output_dir = ""
dir_path = ""
pdf_files = os.listdir(dir_path)
pdf_file_paths = [os.path.join(dir_path, pdf_file) for pdf_file in pdf_files]


def read_pdf(pdf_file_path):
    pdf_dir = pdf_file_path[-10:-7]
    pdf_dir_path = os.path.join(output_dir, pdf_dir)

    try:
        os.mkdir(pdf_dir_path)
    except OSError:
        pass

    # try:
    #     data = tabula.read_pdf(pdf_file_path, pages="all", silent=True)
    #     out_path = os.path.join(pdf_dir_path, pdf_dir+".csv")
    #     data.to_csv(out_path, index=False)
    #     print("File-", pdf_file_path)
    # except:
    #     print("Error reading the whole file. Switching to page-by-page mode...")
    #     pass

    error_pages = []
    pages = PdfFileReader(open(pdf_file_path, 'rb')).getNumPages()
    for page in range(pages, pages + 1):
        try:
            data = tabula.read_pdf(pdf_file_path, pages=page, silent=True)
        except:
            error_pages.append("%s|%s" % (page, pages))
            print("Reading error -", page)
            continue

        if not (data is None or data.empty):
            out_path = os.path.join(output_dir, pdf_dir, str(page) + ".csv")
            data.to_csv(out_path, index=False)
            print("Page -", page, "(out of", pages, ")", data.shape, out_path)
        else:
            error_pages.append("%s|%s" % (page, pages))

    error_file = os.path.join(pdf_dir_path, "errors.txt")
    with open(error_file, "w") as f:
        f.writelines(error_pages)


def extract_pdfs(pdf_files):
    for file in pdf_files[10:]:
        read_pdf(file)
        print("File done-", file)
        print()


if __name__ == '__main__':
    extract_pdfs(pdf_file_paths)
