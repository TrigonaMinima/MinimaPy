import os
import tabula


files = os.listdir()
pdf_files = list(filter(lambda x: x.endswith(".pdf"), files))


for file in pdf_files:
    try:
        data = tabula.read_pdf(file, spreadsheet=True, pages='all')
        data.to_csv(file.replace(".pdf", ".csv"),
                    index=False, quoting=1, encoding='utf8')
        print("File done-", file)
        print()
    except:
        print("Reading error -", file)
        print()
