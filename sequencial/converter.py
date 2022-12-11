"""#Faça um Programa que converta metros para centímetros.
numero = input("Digite um número: ")
#numero.isnumeric()
while True:
    if numero.isdigit():
       print (input(f'O seu número em centímetros é:{numero*100}'))
    else:
        print("Você digitou número inválido. Digite Novamente: ")
    break"""

def leiafloat(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = float (n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido: ')
        if ok:
            break
    return valor

n = leiafloat ('Digite um númro: ')
print(f'O número m centímetro é: {n*100}cm')
