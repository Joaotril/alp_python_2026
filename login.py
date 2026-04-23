user = input('Digite seu nome de usuário')
senha = input('Digite sua senha')
if user == 'aluno' and senha == 'aluno@ifpi':
    print(f'Seja bem vindo {user}')
else:
    print('Acesso negado')