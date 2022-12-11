"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

#while range(2):
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite qualquer número real: "))

a = (2*num1)*(num2/2)
b = (3*num1)+(num3)
c = (num3**3)

print(f"resultado item 1{a} item 2 {b} item {c} ")

