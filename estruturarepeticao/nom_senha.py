#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    if senha == nome:
        nome = input("Erro. Nome igual a senha \nDigite seu nome: ")
        senha = input("Digite sua senha: ")
    else:
        print("Validado")
        #False
        break


