import pyttsx3
import PyPDF2
book = open('filename.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(book)
page = pdf.numPages
print(page)
speak = pyttsx3.init()

for num in range(0,num_pages):
    page = pdf_reader.getPage(num)
    text= page.extractText()
    speak.say(text)
    speak.runAndWait()

