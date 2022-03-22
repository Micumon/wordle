from pdfminer.high_level import extract_text
import os

path = "Z:\$$01_Winkalk\@Winkalk 2022\\009_2022 Moskwa Projektówka\Operat wznowienie\Doręczenia\\13aMarcin Waś.pdf"
text = extract_text(path)
file = path.split("\\")[len(path.split("\\"))-1]
path_list = path.split("\\")
current = ""
for i in range(len(path_list)-1):
    current = current + path_list[i]+"\\"
index1 = text.find("Nazwa")
index2 = text.find("Nazwa cd")
print(str(index1) + " " + str(index2))
text2 = ""
for i in range(index1 + 11, index2):
    text2 += text[i]
text2 = text2.lstrip()
text2 = text2.rstrip()
c = int(len(text2) / 2)
text3 = ""
for i in range(c):
    text3 += text2[i]
text3 += ".pdf"
os.chdir(current)
os.rename(file, text3)
print(current+text3)
