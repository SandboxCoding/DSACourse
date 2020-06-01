print('Selecione o número da operação desejada:\n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = int(input('\nDigite sua opção (1/2/3/4):'))

if opcao == 1:
    primeiro = float(input('Digite o primeiro número: '))
    segundo = float(input('Digite o segundo número: '))
    print(primeiro, "+", segundo, "=", primeiro + segundo)

elif opcao == 2:
    primeiro = float(input('Digite o primeiro número: '))
    segundo = float(input('Digite o segundo número: '))
    print(primeiro, "-", segundo, "=", primeiro - segundo)

elif opcao == 3:
    primeiro = float(input('Digite o primeiro número: '))
    segundo = float(input('Digite o segundo número: '))
    print(primeiro, "*", segundo, "=", primeiro * segundo)

elif opcao == 4:
    primeiro = float(input('Digite o primeiro número: '))
    segundo = float(input('Digite o segundo número: '))
    print(primeiro, "/", segundo, "=", primeiro / segundo)

else:
    print('Opção inválida.')