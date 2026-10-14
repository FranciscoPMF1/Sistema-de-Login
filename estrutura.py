print('---------------------')
print('|   Casa de aposta  |')
print('---------------------')

# LOGIN DO ADM
nome2: str = 'Administrador'
login_teste: str = 'admin01'
senha_teste: str = '1234'

# LOGIN DE CADASTRO
nome: str = ''
login: str = ''
senha: str = ''

# Verificar se o usuario esta logado
usuario_logado = False 
usuario_atual = ''

# Verificar o saldo em conta (variaveis da conta)
saldo = 0



opcao = 0
while opcao != 5:
    print('---------------------') # Menu do site para ficar repetindo
    print('        MENU         ')
    print('---------------------')
    print('1. Fazer cadastro')
    print('2. Fazer login')
    print('3. Ver jogos disponiveis')
    print('4. Ver conta')
    print('5. Sair')
    print('---------------------')

    opcao = int(input('Escolha uma opção: ')) # escolha uma opçao do menu, para acessar uma aba
    print()
    
    if opcao == 1:
        print('---------------------')
        print('  TELA DE CADASTRO')
        print('---------------------')
        nome = str(input('Digite seu nome: '))
        login = str(input('Digite o login: '))
        senha = str(input('Digite a senha: '))
        print()
        print('Cadastro feito com sucesso!!')
        print('Bem vindo {} !'.format(nome))

    elif opcao == 2:
        print('---------------------')
        print('   TELA DE LOGIN')
        print('---------------------')
        login_digitado = str(input('Digite o seu login: '))
        senha_digitada = str(input('Digite sua senha: '))
        print()
        
        if login_digitado == login and senha_digitada == senha:
            print('LOGIN FEITO COM SUCESSO!')
            print('Bem vindo novamente, {} !'.format(nome))
            usuario_logado = True # O sistema sabe que tem alguem logado
            usuario_atual = login # O sistema le qual conta esta logada
        
        elif login_digitado == login_teste and senha_digitada == senha_teste:
            print('LOGIN FEITO COM SUCESSO!')
            print('Bem vindo novamente, {} !'.format(nome2))
            usuario_logado = True # O sistema sabe que tem alguem logado
            usuario_atual = login_teste  # O sistema le qual conta esta logada
             
        else:
             print('Senha ou login incorreto!')
             print('Você não possui cadastro feito!')

    elif opcao == 3:
            print('---------------------')
            print('   TELA DOS JOGOS')
            print('---------------------')

            if usuario_logado == True: # O sistema sabe que tem alguem logado
                opcaoj = 0
                while opcaoj != 3:
                    print('Jogos disponíveis:')
                    print('1. Futebol')
                    print('2. Basquete')
                    print('3. Voltar para o MENU')
                    print('---------------------------')

                    opcaoj = int(input('Escolha uma opção: '))
                    print()

                    if opcaoj == 1:
                        print('----FUTEBOL----')

                    elif opcaoj == 2:
                        print('----BASQUETE----')

                    elif opcaoj == 3:
                        print('voltar para o menu...')

                    else:
                        print('Opção invalida, tente novamente.')

            else:
                print('Acesso negado! Você precisa fazer o login primeiro para ver sua conta.')    

    elif opcao == 4:

        if usuario_logado == True: # O sistema sabe que tem alguem logado

            opcao_conta = 0
            while opcao_conta != 4:
                print('---------------------')
                print('    MINHA CONTA')
                print('---------------------')
                print('1. Informações')
                print('2. Saque')
                print('3. Deposito')
                print('4. Voltar para o MENU')
                print('----------------------')

                opcao_conta = int(input('Escolha uma opcao: '))
                print()

                if opcao_conta == 1:

                    if usuario_atual == login_teste:
                        print('----Informações----')
                        print('Usuario:', usuario_atual)
                        print('Nome:', nome2 )
                        print('login:', login_teste)
                        print('Senha:', senha_teste)
                        print('Saldo em conta:', saldo) 

                    elif usuario_atual == login: 

                        print('----Informações----')
                        print('Usuario:', usuario_atual)
                        print('Nome:', nome )
                        print('login:', login)
                        print('Senha:', senha)
                        print('Saldo em conta: R$', saldo)
                    
                elif opcao_conta == 2:
                    print('----SAQUE----')
                    saque = float(input('Qual o valor que deseja sacar: '))

                    if saque > saldo:
                        print('Saque não autorizado!')
                        print('Valor maior que o saldo atual.')
                        print()
                    
                    elif saque <= saldo:
                        print('Saque efetuado com sucesso!!')
                        saldo = saldo - saque
                        print('Saldo: R$', saldo)
                        print()

                elif opcao_conta == 3:
                    print('----DEPOSITO----')
                    deposito = float(input('Qual o valor que deseja depositar: '))
                    saldo = saldo + deposito
                    print('Depósito efetuado com sucesso!!!')
                    print()

                elif opcao_conta == 4:
                    print('Voltando para o menu...')

                else:
                    print('Opção invalida, tente novamente.')

        else:
             print('Acesso negado! Você precisa fazer o login primeiro para ver sua conta.')

    elif opcao == 5:
        print("SAINDO...")
        break

    else:
        print("Opção invalida")
        print('Escolha uma opção valida do menu.')