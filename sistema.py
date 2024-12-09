menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor de depósito:\n"))

        if valor <= 0:
            print("Error: Valor inválido - valor de depósito deve ser positivo.")
            continue

        saldo += valor
        extrato += f'''
            Depósito realizado no valor de      R$ {valor:10.2f}+
                saldo após este lançamento:     R$ {saldo: 10.2f}
        '''

        print("Depósito realizado com sucesso!")
    elif opcao == "s":
        falha_saque = 'Falha ao realizar saque'

        if numero_saques == LIMITE_SAQUES:
            print("Error: Não é possível realizar mais saques, quantidade de saques diário excedido!")
            continue

        valor = float(input("Digite o valor de saque:\n"))
        if valor <= 0:
            print("Error: Valor inválido - valor deve ser positivo.")
            continue

        if valor > limite:
            print(f'{falha_saque}: valor acima do limite por saque!')
        elif valor > saldo:
            print(f'{falha_saque}: saldo insuficiente!')
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f'''
            Saque realizado no valor de         R$ {valor:10.2f}-
                saldo após este lançamento:     R$ {saldo: 10.2f}
                    '''
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("Exibindo extrato".center(100,'='))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("".center(100, '='))


    elif opcao == "q":
        print("Operação encerrada pelo usuário.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")