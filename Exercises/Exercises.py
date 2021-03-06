#Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
#Result: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

objects = ["Pen", "Pencil", "Eraser", "Sulphite Sheet", "Drawing Tablet"]
print(objects)
#Result: ['Pen', 'Pencil', 'Eraser', 'Sulphite Sheet', 'Drawing Tablet']

#Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

a = "Abiel"
m = " Machioni"
am = a + m
print(am)
#Result: Abiel Machioni

#Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
#objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tuple = ("1", "2", "2", "3", "4", "4", "4", "5")
print(tuple.count("4"))
#Result: 3

#Exercício 5 - Crie um dicionário vazio e imprima na tela

dict = {}
print(dict)
#Result: {}
#Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dict_members = {"Abiel":28, "Paulo":60, "Abner":34}
print(dict_members)
#Result: {'Abiel': 28, 'Paulo': 60, 'Abner': 34}

#Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

dict_members2 = {"Mari":54}
dict_members.update(dict_members2)
print(dict_members)
#Result: {'Abiel': 28, 'Paulo': 60, 'Abner': 34, 'Mari': 54}

#Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
#Imprima o dicionário na tela.

dict_members_approx = {"Abiel":28, "Paulo":60, "Abner":34}
dict_members_approx["Abiel"] = ["28", "29"]
print(dict_members_approx)
#Result: {'Abiel': ['28', '29'], 'Paulo': 60, 'Abner': 34}

#Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
#o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
#o quarto elemento um valor do tipo float.
#Imprima a lista na tela.

a = "Abiel"
qm = ("Queiroz", "Machioni")
dict_birthdate = {"Month":9, "Year":1991}
birthday = float(11)
list_members_family = [a, qm, dict_birthdate, birthday]
print(list_members_family)
#Result: ['Abiel', ('Queiroz', 'Machioni'), {'Month': 9, 'Year': 1991}, 11.0]

#Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
#frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:18])
#Result: Cientista de Dados