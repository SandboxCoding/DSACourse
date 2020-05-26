# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

import unidecode

dia = input('Digite qual o dia da semana estamos:')
dia = dia.casefold()

if unidecode.unidecode(dia) == 'domingo' or unidecode.unidecode(dia) == 'sabado':
    print('Hoje é dia de descanso.')
else:
    print('Você precisa trabalhar!')

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

fruits = ['Banana', 'Morango', 'Mamão', 'Pera', 'Abacaxi']
for i in fruits:
    if i == 'Morango':
        print('Morango faz parte desta lista.')

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma
# lista

elements = (6, 8, 10, 12)
result = []
for i in elements:
    mult = i * 2
    result.append(mult)
    print(result)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

for i in range(100, 151, 2):
    print(i)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35,
# imprima as temperaturas na tela

temperatura = 40
while temperatura > 35:
    print(temperatura)
    temperatura = temperatura - 1

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0

while contador < 100:
    if contador == 23:
        break
    else:
        pass
    print(contador)
    contador = contador + 1


# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista

list = []
value = 4

while value <= 20:
    list.append(value)
    print(value)
    value = value + 2

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30
print('Vista roupas leves.')
else
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."