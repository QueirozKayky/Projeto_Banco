#Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
#esse Banco deseja modernizar suas operacoes e para isso escolheu a linguagem Python. 

#1 - Para primeira versão do sistema devemos implementar apenas 3 operacões. 
#DEPÓSITO / SAQUE / EXTRATO BANCARIO. 


#inciando e dando as boas vindas ao Banco.

print("====================================")
print("      Seja bem vindo ao Banco!")
print("====================================")

print("---------------------------")
print("Selecione o modo bancario! ")
print("---------------------------")

print("[1] Deposito de Dinheiro.")
print("[2] Saque de Dinheiro.")
print("[3] Extrato Bancario.")
print("[4] Sair do Banco!")
print('')

caixa = []  # Lista para armazenar os depósitos
saldo = 0 # Variavel para armazenar o saldo total do usuario. 


# Inicio do modo Deposito.
def deposito():
    print("---------------------------------------")
    print('   Olá, Seja Bem vindo ao Modo Deposito!')
    print("---------------------------------------")
    global saldo
    while True: 
        dinheiro = int(input('Quantos Reais você quer depositar? R$: '))
        caixa.append(dinheiro)
        saldo += dinheiro #atualizando o saldo. 
        resposta = input('Deseja depositar mais dinheiro? [S/N]: ').strip().upper()
        if resposta == 'N':
            break
    print('')
    print(f'Total depositado: {sum(caixa)}')
    print(f'Valores depositados: {caixa}')
    print('')

    
#Inicio do modo Saque.
def saque():
    print("---------------------------------------")
    print('   Olá, Seja Bem vindo ao Modo Saque!')
    print("---------------------------------------")
    global saldo
    if saldo == 0:
        print('Infelizmente nao tem nada no seu caixa... voce precisa depositar dinhero!')
        return
    
    while True:
        print('')
        print(f'Saldo disponível: R${saldo}')
        sacar = int(input("Qual o valor que voce deseja sacar? R$: "))
        if sacar <= 0:
            print('Ops, acho que voce digitou errado!')
        elif sacar >= saldo:
            print('Saldo insuficiente... Tente um valor menor!')
        else:
            caixa.append(-sacar)  # Armazena o saque como valor negativo
            saldo -= sacar #atualiza o saldo novamente. 
            print('')
            print(f'Saque de R${sacar} realizado com sucesso.')
            print('')
            break 

#Inicio do modo Extrato bancario. 
def extrato_bancario():
    print("------------------------------------------------")
    print('  Olá, Seja bem-vindo ao Modo Extrato Bancário!')
    print("------------------------------------------------")
    print('')
    print(f'Transações: {caixa}')
    print(f'Saldo atual: R$ {saldo}')
    print('')
    
    
    
    
#Estrutura de Repeticao para o usuario decidir qual modo deseja usar ou sair. 
while True:
    """print("---------------------------")
    print("Selecione o modo bancário! ")
    print("---------------------------")
    print("[1] Depósito de Dinheiro.")
    print("[2] Saque de Dinheiro.")
    print("[3] Extrato Bancário.")
    print("[4] Sair.")"""

    modo = int(input("Qual seria o modo desejado? [1], [2], [3] ou [4]: "))

    if modo == 1:
        deposito()
    elif modo == 2:
        saque()
    elif modo == 3:
        extrato_bancario()
    elif modo == 4:
        print("Obrigado por usar nosso banco. Até logo!")
        break  
    else:
        print("Opção inválida! Escolha entre [1], [2], [3] ou [4].")