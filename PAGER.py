inputpdf = PdfFileReader(open(r'C:\Users\aesnj\OneDrive\Desktop\17-09-19\20190919-125235.pdf', "rb"))
total_no_pages = inputpdf.numPages
for i in range(5):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(path1 + time.strftime("%Y%m%d-%H%M%S") + "document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
