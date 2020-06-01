print('Selecione o número da operação desejada:\n')
print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão \n' )

opcao = int(input('Digite sua opção (1/2/3/4):'))

if opcao == 1:
    primeiro = float(input('Digite o primeiro número: '))
    segundo = float(input('Digite o segundo número: '))
    print(primeiro + segundo)

elif opcao == 2:
    primeiro = float(input('Digite o primeiro número: '))
    segundo = float(input('Digite o segundo número: '))
    print(primeiro - segundo)

elif opcao == 3:
    primeiro = float(input('Digite o primeiro número: '))
    segundo = float(input('Digite o segundo número: '))
    print(primeiro * segundo)

elif opcao == 4:
    primeiro = float(input('Digite o primeiro número: '))
    segundo = float(input('Digite o segundo número: '))
    print(primeiro / segundo)

else:
    print('Opção inválida.')