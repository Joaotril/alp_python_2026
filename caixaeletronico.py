senha = 123456
tentativas = 0

while tentativas < 3:
    login = int(input('Digite sua senha: '))

    if login == senha:
        print('Olá, <SEUNOME>. Seja bem-vindo ao nosso banco!')
        break

    tentativas += 1

    if tentativas == 1:
        print('Senha incorreta! Você ainda tem 2 tentativas.')

    elif tentativas == 2:
        print('Senha incorreta! Você ainda tem 1 tentativa.')

    elif tentativas == 3:
        print('Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.')