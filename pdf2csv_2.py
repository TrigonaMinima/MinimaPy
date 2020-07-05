import os
import tabula
import configparser
from PyPDF2 import PdfFileReader


def configuration():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["PATHS"]


def get_files(data_dir):
    files = os.listdir(data_dir)
    pdf_files = filter(lambda x: x.lower().endswith(".pdf"), files)
    pdf_paths = [os.path.join(data_dir, pdf_file) for pdf_file in pdf_files]
    return pdf_paths


def create_pdf_extraction_dir(pdf_file, extract_dir):
    pdf_dir = os.path.basename(pdf_file)[:-4]
    pdf_dir_path = os.path.join(extract_dir, pdf_dir)

    if not os.path.isdir(pdf_dir_path):
        os.mkdir(pdf_dir_path)

    return pdf_dir_path


class pdf2csv(object):

    @staticmethod
    def read_pdf_whole(pdf_path, extraction_path):
        try:
            # data = tabula.read_pdf(pdf_path, pages="all", silent=True)
            data = tabula.read_pdf(pdf_path, pages=2, silent=False)
            out_file = pdf_dir = os.path.basename(pdf_file)[:-4]
            out_file_path = os.path.join(extraction_path, out_file + ".csv")
            data.to_csv(out_file_path, index=False)
            print("File-", out_file_path)
            return True
        except:
            print("Error reading the whole file. Switching to page-by-page mode...")
            return False

    @staticmethod
    def read_pdf_page_by_page(pdf_file_path, extraction_path):
        error_pages = []

        # pages = 0
        # try:
        #     pages = PdfFileReader(open(pdf_file_path, 'rb')).getNumPages()
        # except:
        #     print("File can not be read. Please provide a correct file.")

        pages = 5
        for page in range(1, pages):
            try:
                # data = tabula.read_pdf(pdf_file_path, pages=page, silent=True)
                data = tabula.read_pdf(
                    pdf_file_path,
                    pages=page,
                    nospreadsheet=True,
                    area=(210, 20, 691, 573)
                )
            except:
                error_pages.append("|".join([str(page), str(pages)]))
                print("Reading error -", page)
                continue

            if not data.empty:
                out_path = os.path.join(extraction_path, str(page) + ".csv")
                data.to_csv(out_path, index=False)
                print("Page -", page, "(out of", pages, ")", data.shape, out_path)
            else:
                error_pages.append((page, pages))

        error_file = os.path.join(extraction_path, "errors.txt")
        with open(error_file, "w") as f:
            f.writelines(error_pages)


def extract_pdfs(pdf_files, extract_dir):
    # pdf2csv
    for file in pdf_files[:1]:
        output_path = create_pdf_extraction_dir(file, extract_dir)
        if not pdf2csv.read_pdf_whole(file, output_path):
            pdf2csv.read_pdf_page_by_page(file, output_path)

        pdf2csv.read_pdf_page_by_page(file, output_path)
        print("File done-", file)
        print()


if __name__ == '__main__':
    paths = configuration()
    data_dir = paths["data_dir"]
    extract_dir = paths["extract_dir"]

    files = get_files(data_dir)
    # print(files)

    extract_pdfs(files, extract_dir)
