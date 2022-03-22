import os

path = "Z:\$$01_Winkalk\@Winkalk 2022\\009_2022 Moskwa Projektówka\Operat wznowienie\Doręczenia\dorki"
os.chdir(path)
lista = os.listdir(path)
print(lista)
for i in range(len(lista)):
    os.rename(lista[i],str(i)+".pdf")
