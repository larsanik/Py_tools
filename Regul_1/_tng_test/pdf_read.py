#!/usr/bin/python
import fitz

pdf_document = "e3.pdf"
doc = fitz.open(pdf_document)
pages = doc.pageCount
print("number of pages: %i" % pages + '\n')
f_name = 'pdf_pages.txt'
f_w = open(f_name, 'w', encoding='UTF8')

for p in range(pages):
    f_w.write('************************* Page ' + str(p+1) + ' *************************' + '\n')
    page = doc.load_page(p)
    pagetext = page.get_text("text")
    f_w.write(pagetext)
    f_w.write('\n')

f_w.close
