#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = float(input("Digite a nota de 0 a 10: "))

while True:
    if nota <= 10 and nota >= 0:
        print("Número válido")
        break
    else: 
        nota = float(input("Digite a nota de 0 a 10: "))
        if nota <= 10 and nota >= 0:
            print("Número válido")
            break
       
   
