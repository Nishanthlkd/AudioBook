import pyttsx3
import PyPDF2
pdf_file=open('c++ interview.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(pdf_file)
pages=pdf_reader.numPages
speech_voice=pyttsx3.init()
page_number=pdf_reader.getPage(7)
extracted_text=page_number.extractText()
speech_voice.say(extracted_text)
speech_voice.runAndWait()
