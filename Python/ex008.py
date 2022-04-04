# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = int(input('Digite um valor em metros: '))
cm = metros * 100
mm = metros * 1000
print(f'{metros} metros são {cm} centimetros e {mm} milimetros')
