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
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"deposito: valor R$ {valor:.2f}\n"
        else:
            print("Operação falhou, o valor depositado não pode ser negativo")

    elif opcao == "s":
        valor = float(input("Digite um valor para o saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente para a operação")
        elif excedeu_limite:
            print("Você não tem limite suficiente para este saque")
        elif excedeu_limite_saques:
            print("Desculpe, você excedeu o seu limite de saques")
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: valor R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor digitado inválido")

    elif opcao == "e":
        print("\n==================== EXTRATO ====================\n")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo R$ {saldo:.2f}\n")
        print("\n===================================================\n")

    elif opcao == "q":
        break

    else:
        print("Opção Inválida")
