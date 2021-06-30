import PyPDF2 as pdf

pdfFile = open('./with/first.pdf', 'rb')

pdfReader = pdf.PdfFileReader(pdfFile)

info = pdfReader.getDocumentInfo()

authors = info.author.split(';')

for author in authors:
  print(author.lstrip().rstrip())
