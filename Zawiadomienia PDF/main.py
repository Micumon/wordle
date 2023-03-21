import PyPDF2
from pdfminer.high_level import extract_text
from tkinter import filedialog
from tkinter import messagebox
import os

def new_file_name(pdf):
    text = extract_text(pdf)
    text = text.split("Z A W I")
    text.pop(1)
    text = "".join(text)
    text = text.split(".2023r.")
    text.pop(0)
    text = "".join(text)
    text = text.strip()
    text = text.split("\n")
    return text[0]

def mod_path(path):
    path = path[0:path.rfind(r"/")]
    return path

path = filedialog.askopenfilename()
print(path)

reader = PyPDF2.PdfReader(path)
i = 1
for page in range(len(reader.pages)):
    if page % 2 == 1:
        continue
    else:
        output = PyPDF2.PdfWriter()
        output.add_page(reader.pages[page])
        output.add_page(reader.pages[page + 1])
        with open(rf"C:\Users\admin\Desktop\proba\d1\{i}.pdf", "wb") as output_stream:
            output.write(output_stream)
        i += 1
os.remove(path)
path = mod_path(path)
print(path)

try:
    os.chdir(path)
    lista = os.listdir(path)
    for i in range(len(lista)):
        os.rename(lista[i], new_file_name(lista[i]))
except:
    messagebox.showinfo(message='Coś poszło nie tak. Skonsultuj się z kimś.', icon="error")