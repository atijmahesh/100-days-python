'''
1) Get pdf from current directory
2) Read pdf 
3) Call TTS API
'''
import PyPDF2
from gtts import gTTS
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

pdf_path = 'panama.pdf'
text = extract_text_from_pdf(pdf_path)
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

os.system("open output.mp3")  