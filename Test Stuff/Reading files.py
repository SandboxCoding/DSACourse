arq1 = open("C:/PythonFundamentos/Cap04/Notebooks/arquivos/arquivo1.txt", "r", encoding='utf8')

print(arq1.read())

print(arq1.tell())

print(arq1.seek(0,0))

print(arq1.read(11))